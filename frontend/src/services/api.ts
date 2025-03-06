import axios from 'axios';

// Define the base URL for the API
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

interface CVTextInput {
    user_text: string;
}

export async function generateCV(userText: string): Promise<string> {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/generate-cv/`, { user_text: userText });
        console.log("CV generation response:", response.data);
        return response.data;
    } catch (error) {
        console.error('Error generating CV:', error);
        if (axios.isAxiosError(error) && error.response) {
            console.error("Server response:", error.response.data);
        }
        throw error;
    }
};

export async function getDownloadUrl(userText: string, downloadToken?: string): Promise<string | null> {
  try {
    const payload = {
      user_text: userText,
      ...(downloadToken && { download_token: downloadToken })
    };
    console.log("Requesting download URL with payload:", JSON.stringify(payload));
    
    const response = await axios.post(`${API_BASE_URL}/api/get-download-url/`, payload);
    console.log("Download URL response:", response.data);
    
    return response.data.download_url as string; // Type assertion to string
  } catch (error) {
    console.error("Error fetching download URL:", error);
    if (axios.isAxiosError(error) && error.response) {
      console.error("Server response:", error.response.data);
    }
    return null;
  }
};

/**
 * Initiates the download of a CV PDF file by obtaining a download URL from the server
 * and redirecting the browser to that URL.
 * This implementation is independent of browser detection utilities.
 * 
 * @param userText - The user's CV text content
 * @param downloadToken - Optional token for authentication
 */
export async function downloadCvPdf(userText: string, downloadToken?: string): Promise<void> {
    try {
        if (!userText || userText.trim().length === 0) {
            throw new Error("User text is required for download");
        }

        console.log("Initiating download with token:", downloadToken ? "Present" : "Not present");

        const response = await fetch(`/api/download-cv-pdf/${downloadToken}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`Server responded with ${response.status}`);
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `cv_${downloadToken?.substring(0, 8) || 'cv'}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);

        console.log('CV download initiated successfully (downloadCvPdf)');

    } catch (error) {
        console.error("Error initiating PDF download:", error);
        alert("There was a problem downloading your CV. Please try again.");
    }
};

export async function createPaymentSession(payload: any): Promise<any> {
    try {
        console.log("Requesting payment session with payload:", JSON.stringify(payload));
        const response = await axios.post(`${API_BASE_URL}/api/create-payment-session`, payload);
        console.log("Payment session response:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error calling create-payment-session API:", error);
        if (axios.isAxiosError(error) && error.response) {
            console.error("Server response:", error.response.data);
        }
        throw error; // Re-throw to handle in component 
    }
};