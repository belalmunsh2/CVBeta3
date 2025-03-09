<template>
  <div class="bg-gray-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 py-12 sm:py-16">
      <div class="bg-white rounded-xl shadow-sm p-6 sm:p-8 mb-8 transition-shadow duration-300 hover:shadow-md">
        <div class="text-center mb-8">
          <div class="mb-4 inline-flex items-center justify-center w-16 h-16 bg-primary-50 rounded-full">
            <svg class="w-8 h-8 text-primary-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h1 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-2">Your CV is Ready!</h1>
          <p class="text-gray-600 text-base sm:text-lg max-w-lg mx-auto">
            Thank you for using our service. Your professional CV has been generated and is ready for download.
          </p>
        </div>

        <div class="border-t border-b border-gray-100 py-6 mb-6">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between">
            <div class="mb-4 md:mb-0">
              <h2 class="text-lg font-semibold text-gray-800 mb-1">Order Summary</h2>
              <p class="text-gray-600 text-sm">Transaction ID: {{ transactionId }}</p>
            </div>
            <div class="bg-primary-50 px-4 py-2 rounded-lg">
              <p class="text-primary-700 font-medium">
                <span class="text-sm">Total Paid:</span> 
                <span class="ml-1 text-lg">${{ formatPrice(paymentAmount) }}</span>
              </p>
            </div>
          </div>
        </div>

        <div class="mb-8">
          <div class="bg-gray-50 rounded-lg p-5 border border-gray-100">
            <h3 class="text-lg font-semibold text-gray-800 mb-4 flex items-center">
              <svg class="w-5 h-5 mr-2 text-primary-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              Your CV Details
            </h3>
            <ul class="space-y-3 text-gray-600">
              <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                <span>Format: Professional PDF</span>
              </li>
              <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                <span>ATS Optimized Content</span>
              </li>
              <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                <span>Professional Layout</span>
              </li>
              <li class="flex items-start">
                <svg class="w-5 h-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                <span>AI-Enhanced Content</span>
              </li>
            </ul>
          </div>
        </div>

        <div class="flex flex-col items-center justify-center">
          <button 
            @click="downloadCV" 
            class="bg-primary-600 hover:bg-primary-700 focus:ring-primary-500 text-white font-medium rounded-lg px-8 py-4 mb-4 text-base transition-all duration-200 shadow-sm hover:shadow-md flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-offset-2 w-full sm:w-auto download-btn"
          >
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
            <span>Download Your CV</span>
          </button>
          
          <router-link 
            to="/" 
            class="text-primary-600 hover:text-primary-800 font-medium"
          >
            <svg class="w-4 h-4 mr-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
            </svg>
            Return to Home
          </router-link>
        </div>
      </div>
      
      <!-- Share & Feedback Section -->
      <div class="bg-primary-50 rounded-xl shadow-sm p-6 sm:p-8 border border-primary-100">
        <h2 class="text-xl font-semibold text-primary-800 mb-4">Share and Recommend Pro CV!</h2>
        <p class="text-primary-700 mb-6">Help your friends and colleagues create professional CVs too.</p>
        
        <div class="bg-white rounded-lg p-4 border border-primary-100 flex items-center justify-between">
          <a 
            :href="projectURL" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-primary-600 hover:text-primary-800 font-medium transition-colors duration-200"
          >
            {{ projectURL }}
          </a>
          <button 
            @click="copyToClipboard" 
            class="bg-primary-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-primary-700 transition-colors duration-200 ml-3"
          >
            Copy
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

// Get the route object to access URL parameters
const route = useRoute();
const transactionId = ref('TXN' + Math.floor(Math.random() * 1000000).toString().padStart(6, '0'));
const paymentAmount = ref(1000); // Default amount in cents
const downloadToken = ref('');
const projectURL = ref('https://pro-cv.myvnc.com/'); // Project URL for sharing

onMounted(() => {
  // Get the download token from the URL parameter or localStorage
  if (route.params.token) {
    downloadToken.value = route.params.token.toString();
  } else {
    // Try to get token from localStorage
    const storedToken = localStorage.getItem('download_token');
    if (storedToken) {
      downloadToken.value = storedToken;
    }
  }

  // Get payment amount from URL parameter
  if (route.params.amount) {
    paymentAmount.value = parseInt(route.params.amount.toString());
  }

  // Auto-download the CV PDF when page loads
  if (downloadToken.value) {
    // Create a temporary link element to trigger the download
    const downloadLink = document.createElement('a');
    downloadLink.href = `${import.meta.env.VITE_API_BASE_URL}/api/download-cv-pdf-file/${downloadToken.value}`;
    downloadLink.download = 'your_cv.pdf';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  }
});

const formatPrice = (amount) => {
  return (amount / 100).toFixed(2);
};

const downloadCV = async () => {
  // Get the user_text from localStorage
  const userText = localStorage.getItem('cv_user_text');
  
  if (!userText) {
    alert('Sorry, your CV content is not available. Please generate a new CV.');
    return;
  }
  
  try {
    // Update button state to show loading
    const downloadButton = document.querySelector('.download-btn');
    if (downloadButton) {
      downloadButton.setAttribute('disabled', 'true');
      downloadButton.querySelector('span').textContent = 'Downloading...';
    }
    
    // Use the full backend URL instead of a relative path
    const backendURL = `https://cuddly-engine-pjwvppv46rqgf7q7j-8000.app.github.dev/api/download-cv-pdf/${downloadToken.value}`;
    
    // Simplify the download by using a direct redirect instead of fetch/blob handling
    window.location.href = backendURL;
    console.log('CV download initiated successfully');
    
    // Since we're redirecting, we can't reset the button state after download
    // The page will reload when the user navigates back anyway
    setTimeout(() => {
      // Reset button state after a short delay
      if (downloadButton) {
        downloadButton.removeAttribute('disabled');
        downloadButton.querySelector('span').textContent = 'Download Your CV';
      }
    }, 3000); // Give time for the download to start before resetting the button
  } catch (err) {
    console.error('Error downloading PDF:', err);
    alert('Error downloading your CV. Please try again.');
    
    // Reset button state
    const downloadButton = document.querySelector('.download-btn');
    if (downloadButton) {
      downloadButton.removeAttribute('disabled');
      downloadButton.querySelector('span').textContent = 'Download Your CV';
    }
  }
};

const copyToClipboard = () => {
  navigator.clipboard.writeText(projectURL.value);
  alert('Copied to clipboard!');
};
</script>
