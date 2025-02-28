<template>
  <div class="download-ready-page">
    <h1>Thank you for your payment!</h1>
    <p>Preparing your CV download, please wait...</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'; // Import useRouter
import { downloadCvPdf } from '../services/api';

const router = useRouter(); // Use useRouter

onMounted(async () => {
  const userText = localStorage.getItem('cv_user_text'); // Get userText from localStorage

  if (userText) {
    try {
      await downloadCvPdf(userText); // Call downloadCvPdf to initiate download
      // No further action needed here, downloadCvPdf handles redirection
    } catch (error) {
      console.error("Error initiating download from DownloadReadyView:", error);
      // Optional: Handle error more visibly in the UI, e.g., display an error message
      // or redirect back to service page with error query param
      // router.push('/service?error=download_failed');
    }
  } else {
    console.error("userText not found in localStorage. Download cannot be initiated.");
    // Optional: Redirect user back to service page with error message
    // router.push('/service?error=user_text_missing');
  }
});
</script>

<style scoped>
/* You can add styling here later if needed */
</style>
