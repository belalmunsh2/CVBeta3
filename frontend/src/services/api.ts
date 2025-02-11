import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL; // Simplified API_BASE_URL definition

export const generateCV = async (userText: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/generate-cv/`, { user_text: userText }, { responseType: 'blob' });
    return response;
  } catch (error) {
    console.error('Error generating CV:', error);
    throw error;
  }
};