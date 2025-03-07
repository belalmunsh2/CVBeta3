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
          
          <!-- Debug Download Buttons Section -->
          <div class="mt-8 pt-4 border-t border-gray-200">
            <p class="text-sm text-gray-500 mb-2 text-center">Experiencing issues with the download? Try these alternative options:</p>
            <div class="space-y-3">
              <button @click="downloadCVFile" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition duration-200 flex items-center justify-center">
                <span>Try File Download</span>
              </button>
              <button @click="downloadCVDebug" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded-lg transition duration-200 flex items-center justify-center">
                <span>Try Enhanced Download</span>
              </button>
            </div>
          </div>
          
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
        <h2 class="text-xl font-semibold text-primary-800 mb-4">Share Your Success!</h2>
        <p class="text-primary-700 mb-6">Help your friends and colleagues create professional CVs too.</p>
        
        <div class="flex flex-wrap gap-3 mb-6">
          <button class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 flex items-center">
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
            </svg>
            Facebook
          </button>
          <button class="bg-blue-400 hover:bg-blue-500 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 flex items-center">
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723 10.1 10.1 0 01-3.127 1.184 4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.937 4.937 0 004.604 3.417 9.868 9.868 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.054 0 13.999-7.496 13.999-13.986 0-.209 0-.42-.015-.63a9.936 9.936 0 002.46-2.548l-.047-.02z" />
            </svg>
            Twitter
          </button>
          <button class="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 flex items-center">
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
            </svg>
            WhatsApp
          </button>
          <button class="bg-blue-700 hover:bg-blue-800 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 flex items-center">
            <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
            </svg>
            LinkedIn
          </button>
        </div>
        
        <div class="bg-white rounded-lg p-4 border border-primary-100">
          <h3 class="text-lg font-medium text-gray-800 mb-2">Refer a friend & get 20% off your next purchase!</h3>
          <div class="flex">
            <input 
              type="text" 
              value="www.cv-generator.com/ref?code=YOUR123" 
              readonly 
              class="flex-1 px-3 py-2 bg-gray-50 border border-gray-200 rounded-l-lg focus:ring-1 focus:ring-primary-300 focus:border-primary-300 outline-none text-sm"
            />
            <button class="bg-primary-600 text-white px-4 py-2 rounded-r-lg text-sm font-medium hover:bg-primary-700 transition-colors duration-200">
              Copy
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { downloadCvPdf } from '../services/api';

// Get the route object to access URL parameters
const route = useRoute();
const transactionId = ref('TXN' + Math.floor(Math.random() * 1000000).toString().padStart(6, '0'));
const paymentAmount = ref(1000); // Default amount in cents
const downloadToken = ref('');

onMounted(() => {
  // Get the download token from the URL parameter
  if (route.params.token) {
    downloadToken.value = route.params.token.toString();
  } else {
    // Try to get it from localStorage as a fallback
    const storedToken = localStorage.getItem('download_token');
    if (storedToken) {
      downloadToken.value = storedToken;
    }
  }
  
  // Get the amount from the URL parameter
  if (route.query.amount) {
    paymentAmount.value = parseInt(route.query.amount.toString(), 10);
  }
  
  // Get the transaction ID from the URL parameter
  if (route.query.transaction_id) {
    transactionId.value = route.query.transaction_id.toString();
  } else if (route.query.id) {
    transactionId.value = 'TXN' + route.query.id.toString();
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
    
    try {
      const response = await fetch(`/api/download-cv-pdf/${downloadToken.value}`, {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `cv_${downloadToken.value.substring(0, 8)}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
      console.log('CV download initiated successfully (direct fetch)');
    } catch (downloadErr) {
      console.log('Direct download failed, falling back to original method');
      await downloadCvPdf(userText, downloadToken.value); // Keep fallback for now
    }
  } catch (err) {
    console.error('Error downloading PDF:', err);
    alert('Error downloading your CV. Please try again.');
  } finally {
    // Reset button state
    const downloadButton = document.querySelector('.download-btn');
    if (downloadButton) {
      downloadButton.removeAttribute('disabled');
      downloadButton.querySelector('span').textContent = 'Download Your CV';
    }
  }
};

// New methods for debugging alternative download methods
const downloadCVFile = async () => {
  // Try the FileResponse-based endpoint
  const userText = localStorage.getItem('cv_user_text');
  
  if (!userText) {
    alert('Sorry, your CV content is not available. Please generate a new CV.');
    return;
  }

  try {
    const response = await fetch(`/api/download-cv-pdf-file/${downloadToken.value}`, {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`);
    }

    const blob = await response.blob();
    console.log('Received file blob:', blob.size, 'bytes, type:', blob.type);
    
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `cv_file_${downloadToken.value.substring(0, 8)}.pdf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
    console.log('File-based download initiated successfully');
  } catch (err) {
    console.error('Error with file-based download:', err);
    alert('Error downloading your CV using file method. Please try again.');
  }
};

const downloadCVDebug = async () => {
  // Try the enhanced debug endpoint
  const userText = localStorage.getItem('cv_user_text');
  
  if (!userText) {
    alert('Sorry, your CV content is not available. Please generate a new CV.');
    return;
  }

  try {
    console.log('Attempting enhanced debug download');
    const response = await fetch(`/api/download-cv-pdf-debug/${downloadToken.value}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/pdf',
      },
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}: ${await response.text()}`);
    }

    // Log response headers for debugging
    console.log('Response headers:');
    response.headers.forEach((value, key) => {
      console.log(`${key}: ${value}`);
    });

    const blob = await response.blob();
    console.log('Received debug blob:', blob.size, 'bytes, type:', blob.type);
    
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `cv_debug_${downloadToken.value.substring(0, 8)}.pdf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
    console.log('Debug download initiated successfully');
  } catch (err) {
    console.error('Error with debug download:', err);
    alert('Error downloading your CV using debug method. Please try again.');
  }
};
</script>
