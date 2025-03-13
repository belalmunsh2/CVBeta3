<template>
  <div class="bg-gray-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <h1 class="text-2xl sm:text-3xl font-bold text-primary-600 text-center mb-8">CV Creator Service</h1>
      
      <div class="bg-white rounded-xl shadow-sm p-6 sm:p-8 mb-8 transition-shadow duration-300 hover:shadow-md">
        <!-- CV Form Component -->
        <CVForm v-if="showForm" @cv-submit="handleFormSubmit" :is-generating="isGeneratingCV" />
        
        <!-- Show when form is hidden -->
        <div v-else class="text-center py-4">
          <button 
            @click="showForm = true" 
            class="text-primary-600 hover:text-primary-700 font-medium text-sm underline focus:outline-none"
          >
            Edit Information
          </button>
        </div>
      </div>

      <div 
        v-if="error" 
        class="bg-red-50 text-red-700 p-5 rounded-lg mb-8 text-sm sm:text-base border border-red-100 shadow-sm"
      >
        <div class="flex items-start">
          <svg class="h-5 w-5 text-red-600 mt-0.5 mr-2 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
          </svg>
          <span>{{ error }}</span>
        </div>
      </div>

      <div v-if="cvContent" class="bg-white rounded-xl shadow-sm p-6 sm:p-8 mb-8 transition-shadow duration-300 hover:shadow-md">
        <h2 class="text-xl sm:text-2xl font-semibold text-gray-800 mb-5">Generated CV Content:</h2>
        <div class="bg-gray-50 rounded-lg p-5 sm:p-6 text-sm sm:text-base font-mono whitespace-pre-wrap border border-gray-200 shadow-inner">
          {{ cvContent }}
        </div>
      </div>

      <!-- CV Preview Component -->
      <div class="preview-component">
        <Preview v-if="cvContent" :userText="userText" />
      </div>

      <div v-if="cvContent" class="bg-white rounded-xl shadow-sm p-6 sm:p-8 transition-shadow duration-300 hover:shadow-md">
        <h2 class="text-xl sm:text-2xl font-semibold text-gray-800 mb-5">Complete Your Order</h2>
        <div class="text-base sm:text-lg font-medium text-gray-700 mb-6">
          <p>Base Price: <span class="text-primary-600 font-semibold">${{ (currentAmount / 100).toFixed(2) }}</span></p>
        </div>

        <PromoCode 
          :amount="currentAmount" 
          @discountApplied="handleDiscountApplied" 
        />

        <button 
          @click="handlePayNowClick" 
          class="bg-primary-600 hover:bg-primary-700 focus:ring-primary-500 text-white font-medium rounded-lg px-6 py-4 w-full mt-8 text-sm sm:text-base transition-all duration-200 shadow-sm hover:shadow flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-70 disabled:cursor-not-allowed"
        >
          <span class="mr-2">Pay Now</span>
          <span class="font-semibold">
            {{ discountedAmount ? `$${(finalAmount / 100).toFixed(2)}` : `$${(currentAmount / 100).toFixed(2)}` }}
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { generateCV, createPaymentSession } from '../services/api';
import PromoCode from '../components/PromoCode.vue';
import CVForm from '../components/CvForm.vue';
import Preview from '../components/Preview.vue'; // Import the Preview component

const userText = ref('');
const userData = ref(null);
const cvContent = ref('');
const isLoading = ref(false);
const error = ref('');
const currentAmount = ref(1001); // Base price in cents
const discountedAmount = ref(null);
const isDownloadButtonVisible = ref(false);
const showForm = ref(true); // Add showForm state
const isGeneratingCV = ref(false);

// Listen for the cv-submit event from the CVForm component
onMounted(() => {
  document.addEventListener('cv-submit', (event) => {
    const { userData: formData, formattedText } = event.detail;
    userData.value = formData;
    userText.value = formattedText;
    showForm.value = false; // Hide the form after submission
    handleGenerateClick();
  });
});

const handleDiscountApplied = (discountData) => {
  console.log("Discount Applied in ServiceView:", discountData);
  discountedAmount.value = discountData.discountedAmount;
  // Update the amount that will be used for payment
};

const finalAmount = computed(() => {
  return discountedAmount.value || currentAmount.value;
});

// Handle form submission from the CVForm component
const handleFormSubmit = (data) => {
  userData.value = data.userData;
  userText.value = data.formattedText;
  showForm.value = false; // Hide the form after submission
  handleGenerateClick();
};

const handleGenerateClick = async () => {
  if (!userText.value) {
    error.value = 'Please complete the CV form with your information.';
    return;
  }

  isLoading.value = true;
  error.value = '';
  isDownloadButtonVisible.value = false;
  isGeneratingCV.value = true;

  try {
    const response = await generateCV(userText.value);
    cvContent.value = response;
    isDownloadButtonVisible.value = true;
    
    // Scroll to the preview section automatically
    setTimeout(() => {
      const previewElement = document.querySelector('.preview-component');
      if (previewElement) {
        previewElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 500);
  } catch (err) {
    error.value = 'Error generating CV. Please try again.';
    console.error('Error:', err);
    isDownloadButtonVisible.value = false;
  } finally {
    isLoading.value = false;
    isGeneratingCV.value = false;
  }
};

// Note: Removing handleDownloadClick function as it's no longer needed
// Downloads are now handled directly in DownloadReadyView.vue

let testPaymentCounter = 0;

const handlePayNowClick = async () => {
  testPaymentCounter++;
  const testEmail = userData.value?.email || 'test' + testPaymentCounter + '@example.com';
  const testFirstName = userData.value?.firstName || 'Test' + testPaymentCounter;
  const testLastName = userData.value?.lastName || 'User' + testPaymentCounter;
  const itemDescription = 'AI-Powered CV Generation Test ' + testPaymentCounter;
  const amount = finalAmount.value; // Amount in cents

  try {
    isLoading.value = true;
    error.value = '';

    // Store user text in localStorage for later use in DownloadReadyView
    localStorage.setItem('cv_user_text', userText.value);
    
    // Store structured user data if available
    if (userData.value) {
      localStorage.setItem('cv_user_data', JSON.stringify(userData.value));
    }

    // Check internet connection before making the request
    if (!navigator.onLine) {
      error.value = 'You appear to be offline. Please check your internet connection and try again.';
      return;
    }

    const response = await createPaymentSession({
      amount: amount,
      user_text: userText.value, // Pass user_text to backend
      billing_data: {
        email: testEmail,
        first_name: testFirstName,
        last_name: testLastName,
        phone_number: userData.value?.phone || "+201234567890",
        country: "EGY"
      },
      items: [
        {
          name: "CV Generation Service",
          amount: amount,
          description: itemDescription
        }
      ]
    });

    if (response && response.client_secret) {
      const publicKey = response.public_key;
      const clientSecret = response.client_secret;
      const unifiedCheckoutBaseUrl = response.payment_url;
      
      // Store download_token in localStorage if available
      if (response.download_token) {
        localStorage.setItem('download_token', response.download_token);
        console.log("Download token stored in localStorage:", response.download_token);
      }
      
      // Construct the payment URL with download_token as a query parameter
      const unifiedCheckoutURL = `${unifiedCheckoutBaseUrl}?publicKey=${publicKey}&clientSecret=${clientSecret}`;
      
      // Add download_token as a query parameter to the payment URL
      // This will be passed back to our callback endpoint by Paymob
      const finalCheckoutURL = response.download_token 
        ? `${unifiedCheckoutURL}&download_token=${response.download_token}` 
        : unifiedCheckoutURL;
      
      window.location.href = finalCheckoutURL;
    } else {
      error.value = 'Failed to initiate payment. Please try again later.';
    }
  } catch (e) {
    if (e.response && e.response.data && e.response.data.detail) {
      // Display the specific error message from the backend if available
      error.value = `Payment error: ${e.response.data.detail}`;
      
      if (e.response.data.detail.includes('Failed to connect to Paymob')) {
        error.value = 'Payment service is currently unavailable. Please try again later or contact support.';
      }
    } else {
      error.value = 'Payment initiation failed. Please check your connection and try again.';
    }
    console.error('Payment Error:', e);
  } finally {
    isLoading.value = false;
  }
};
</script>
