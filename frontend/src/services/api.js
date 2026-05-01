import axios from 'axios';

// 1. Create a "Base Instance" so you don't repeat the URL everywhere
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Your Python Backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// 2. Define the specific "Courier Task" for predictions
export const getRiskPrediction = async (formData) => {
  try {
    // This sends all 28 parameters to the /predict endpoint
    const response = await apiClient.post('api/v1/predict', formData);
    return response.data; // This returns the score and 5 reasons
  } catch (error) {
    console.error("API Error:", error);
    throw error; // Pass the error back to the UI to show a warning
  }
};