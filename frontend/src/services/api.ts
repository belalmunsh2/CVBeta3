import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

interface CVTextInput {
    user_text: string;
}

export const generateCV = async (userText: string): Promise<string> => {
    try {
        const response = await axios.post(`${API_BASE_URL}/generate-cv/`, { user_text: userText });
        return response.data;
    } catch (error) {
        console.error('Error generating CV:', error);
        throw error;
    }
};

export const downloadCvPdf = async (cvTextInput: CVTextInput): Promise<Blob> => {
    const response = await fetch(`${API_BASE_URL}/download-cv-pdf/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(cvTextInput),
    });
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.blob();
};