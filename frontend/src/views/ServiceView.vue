<template>
  <div class="service-page">
    <h1>CV Creator Service Page</h1>
    
    <textarea v-model="userText" placeholder="Enter your experience and skills here..." rows="10" cols="80"></textarea><br>
    <button @click="generateCvClicked">Generate CV</button>
    <button @click="handleDownloadPdfClick">Download PDF CV</button>
    <button @click="handlePayNowClick">Pay Now</button>

    <div v-if="generatedCvContent" class="cv-output">
      <h2>Generated CV Content:</h2>
      <pre>{{ generatedCvContent }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { generateCV, downloadCvPdf } from '../services/api';
import { createPaymentSession } from '../services/api'; // Adjust path if needed

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

const handlePayNowClick = async () => {
  try {
    const response = await createPaymentSession({ user_text: userText.value }); // Call your API function
    console.log('Payment session created successfully!', response.data);

    const publicKey = response.data.public_key;
    const clientSecret = response.data.client_secret;
    const unifiedCheckoutBaseUrl = response.data.payment_url;
    const paymentPageUrl = `${unifiedCheckoutBaseUrl}?publicKey=${publicKey}&clientSecret=${clientSecret}`;

    window.location.href = paymentPageUrl; // Redirect to Paymob Payment Page!

  } catch (error) {
    console.error('Error creating payment session:', error);
    // Handle error (e.g., display error message to user)
  }
};
</script>

<style scoped>
.service-page {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}
</style>
