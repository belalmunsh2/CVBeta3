<template>
  <div class="welcome-page">
    <div class="hero-section">
      <h1>Welcome to CV Builder!</h1>
      <p>Create your professional CV easily with our AI-powered CV Builder. Get started below!</p>
      <router-link to="/service" class="get-started-button">Get Started</router-link>
    </div>
    <textarea v-model="userText" placeholder="Enter your experience and skills here..." rows="10" cols="80"></textarea><br>
    <button @click="generateCvClicked">Generate CV</button>
    <button @click="handleDownloadPdfClick">Download PDF CV</button>

    <div v-if="generatedCvContent" class="cv-output">
      <h2>Generated CV Content:</h2>
      <pre>{{ generatedCvContent }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { generateCV, downloadCvPdf } from '../services/api';

const userText = ref('');
const generatedCvContent = ref('');

const generateCvClicked = async () => {
  console.log("Generate CV button clicked!");
  console.log("userText value:", userText.value);

  try {
    const response = await generateCV(userText.value);
    console.log("Full response object (before Blob):", response);
    console.log("API response received:", response);

    generatedCvContent.value = response;

  } catch (error) {
    console.error("Error in generateCvClicked:", error);
  }
  console.log("generatedCvContent value after API call (now irrelevant for PDF download):", generatedCvContent.value);
};

const handleDownloadPdfClick = async () => {
  try {
    const pdfBlob = await downloadCvPdf({ user_text: userText.value });
    const pdfUrl = URL.createObjectURL(pdfBlob);
    const downloadLink = document.createElement('a');
    downloadLink.href = pdfUrl;
    downloadLink.download = 'cv.pdf';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
    URL.revokeObjectURL(pdfUrl);
  } catch (error) {
    console.error("Error downloading PDF:", error);
  }
};
</script>

<style scoped>
.welcome-page {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f0f0;
}

.hero-section {
  text-align: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.hero-section h1 {
  color: #333;
}

.hero-section p {
  color: #666;
  margin-bottom: 20px;
}

.get-started-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.get-started-button:hover {
  background-color: #0056b3;
}
</style>
