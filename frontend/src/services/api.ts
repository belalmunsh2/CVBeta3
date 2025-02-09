import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL; // Simplified API_BASE_URL definition

export const generateCV = async (userText: string): Promise<string> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/generate-cv/`, { user_text: userText });
    return response.data; // Assuming backend sends plain text CV content in response body
  } catch (error: any) {
    console.error("Error calling backend API:", error);
    return "Error generating CV. Please try again."; // Basic error message for frontend
  }
};