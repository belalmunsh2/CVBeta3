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
    } catch (error: any) {
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
  } catch (error: any) {
    console.error("Error fetching download URL:", error);
    if (axios.isAxiosError(error) && error.response) {
      console.error("Server response:", error.response.data);
    }
    return null;
  }
};

export async function getCvPreview(userText: string): Promise<Blob> {
  try {
    console.log("Requesting CV preview with text length:", userText.length);
    const response = await axios.post(`${API_BASE_URL}/api/preview`, {
      user_text: userText
    }, {
      responseType: 'blob'
    });
    
    console.log("CV preview response received, type:", response.headers['content-type']);
    return response.data;
  } catch (error: any) {
    console.error("Error fetching CV preview:", error);
    if (axios.isAxiosError(error) && error.response) {
      console.error("Server response:", error.response.data);
    }
    throw error;
  }
};

export async function createPaymentSession(payload: any): Promise<any> {
    try {
        console.log("Requesting payment session with payload:", JSON.stringify(payload));
        const response = await axios.post(`${API_BASE_URL}/api/create-payment-session`, payload);
        console.log("Payment session response:", response.data);
        return response.data;
    } catch (error: any) {
        console.error("Error calling create-payment-session API:", error);
        if (axios.isAxiosError(error) && error.response) {
            console.error("Server response:", error.response.data);
        }
        throw error; // Re-throw to handle in component 
    }
};