import axios from 'axios';

// Define the base URL for the API
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

interface CVTextInput {
    user_text: string;
}

export async function generateCV(userText: string): Promise<string> {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/generate-cv/`, { user_text: userText });
        return response.data;
    } catch (error) {
        console.error('Error generating CV:', error);
        throw error;
    }
};

export const getDownloadUrl = async (userText: string): Promise<string | null> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/get-download-url/`, { user_text: userText });
    return response.data.download_url as string; // Type assertion to string
  } catch (error) {
    console.error("Error fetching download URL:", error);
    return null;
  }
};

export async function downloadCvPdf(userText: string, downloadToken?: string): Promise<void> {
    try {
        const downloadUrl = await getDownloadUrl(userText);
        
        if (downloadUrl) {
            window.location.href = downloadUrl; // Redirect to download URL
        } else {
            console.error("Failed to get download URL from backend.");
            // Optionally, throw an error to signal failure to calling component:
            // throw new Error("Failed to get download URL.");
        }
    } catch (error) {
        console.error("Error initiating PDF download:", error);
        // Optionally, re-throw the error to propagate it:
        // throw error;
    }
};

export async function createPaymentSession(payload: any): Promise<any> {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/create-payment-session`, payload);
        return response.data;
    } catch (error) {
        console.error("Error calling create-payment-session API:", error);
        throw error; // Re-throw to handle in component 
    }
};