<template>
  <div class="download-container">
    <h2>Your CV is ready!</h2>
    <button @click="downloadPDF">Download PDF</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const downloadToken = route.params.token;

const downloadPDF = async () => {
  // **IMPORTANT: Make sure to replace this with your *actual* backend cloud URL if it's different!**
  const backendURL = `https://cuddly-engine-pjwvppv46rqgf7q7j-8000.app.github.dev/api/download-cv-pdf/${downloadToken}`;

  try {
    const response = await fetch(backendURL);
    if (!response.ok) {
      console.error('HTTP error!', response.status);
      throw new Error(`HTTP error! status: ${response.status}`); // Improved error handling
    }
    const blob = await response.blob();

    // Create download link
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "generated_cv.pdf";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (error) {
    console.error("Failed to download PDF:", error);
    // Consider showing an error message to the user in the template if needed.
    alert("Failed to download PDF. Please try again later."); // Basic error alert for user
  }
};
</script>

<style scoped>
.download-container {
  text-align: center;
  margin-top: 50px;
}
button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  font-size: 18px;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #45a049;
}
</style>
