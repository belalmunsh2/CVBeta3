import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

interface CVTextInput {
    user_text: string;
}

export async function generateCV(payload: { user_text: string }): Promise<string> {
    try {
        const response = await axios.post(`${API_BASE_URL}/generate-cv/`, payload);
        return response.data;
    } catch (error) {
        console.error('Error generating CV:', error);
        throw error;
    }
};

export async function downloadCvPdf(payload: { user_text: string }): Promise<Blob> {
    try {
        const response = await axios.post(`${API_BASE_URL}/download-cv-pdf/`, payload, {
            responseType: 'blob', // Important for handling binary data (PDF)
        });
        return response.data;
    } catch (error) {
        console.error("Error calling download-cv-pdf API:", error);
        throw error;
    }
};

export async function createPaymentSession(payload: { user_text: string }): Promise<any> {
    try {
        const response = await axios.post(`${API_BASE_URL}/create-payment-session`, payload);
        return response.data;
    } catch (error) {
        console.error("Error calling create-payment-session API:", error);
        throw error; // Re-throw to handle in component
    }
};