<template>
  <div class="download-ready-page">
    <h1>Thank you for your payment!</h1>
    <p>Preparing your CV download, please wait...</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { downloadCvPdf } from '../services/api';

const router = useRouter();

onMounted(async () => {
  console.log("DownloadReadyView.vue - onMounted: Component mounted");

  const userText = localStorage.getItem('cv_user_text');
  console.log("DownloadReadyView.vue - onMounted: Retrieved userText from localStorage:", userText);

  if (userText) {
    console.log("DownloadReadyView.vue - onMounted: userText found, proceeding to download initiation");
    try {
      console.log("DownloadReadyView.vue - onMounted: Calling downloadCvPdf(userText)");
      await downloadCvPdf(userText);
      console.log("DownloadReadyView.vue - onMounted: downloadCvPdf call completed (redirection should have happened)");
    } catch (error) {
      console.error("DownloadReadyView.vue - onMounted: Error initiating download:", error);
      // Optional: Handle error more visibly in the UI, e.g., display an error message
      // or redirect back to service page with error query param
      // router.push('/service?error=download_failed');
    }
  } else {
    console.error("DownloadReadyView.vue - onMounted: userText NOT found in localStorage. Download cannot be initiated.");
    // Optional: Redirect user back to service page with error message
    // router.push('/service?error=user_text_missing');
  }

  console.log("DownloadReadyView.vue - onMounted: onMounted hook finished execution");
});
</script>

<style scoped>
/* You can add styling here later if needed */
</style>
