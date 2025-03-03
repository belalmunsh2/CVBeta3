<template>
  <div class="bg-gray-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 py-6 sm:py-10">
      <h1 class="text-2xl sm:text-3xl font-bold text-primary-600 text-center mb-6">CV Creator Service</h1>
      
      <div class="bg-white rounded-xl shadow-soft p-4 sm:p-6 mb-6">
        <h2 class="text-lg sm:text-xl font-semibold text-gray-800 mb-4">Enter your information</h2>
        <textarea
          v-model="userText"
          placeholder="Enter your experience, skills, and other relevant information..."
          :disabled="isLoading"
          class="w-full min-h-[150px] sm:min-h-[200px] p-3 sm:p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-300 focus:border-primary-500 transition duration-200 outline-none resize-y text-sm sm:text-base"
        ></textarea>
        
        <div class="flex flex-col sm:flex-row gap-3 mt-4">
          <button 
            @click="handleGenerateClick" 
            :disabled="isLoading" 
            class="btn btn-primary py-2 sm:py-3 flex-1 text-sm sm:text-base"
          >
            <span v-if="isLoading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Generating...
            </span>
            <span v-else>Generate CV</span>
          </button>
          <button 
            v-if="false" 
            @click="handleDownloadClick" 
            :disabled="isLoading" 
            class="btn btn-secondary py-2 sm:py-3 flex-1 text-sm sm:text-base"
          >
            Download PDF
          </button>
        </div>
      </div>

      <div 
        v-if="error" 
        class="bg-red-50 text-red-700 p-4 rounded-lg mb-6 text-sm sm:text-base"
      >
        {{ error }}
      </div>

      <div v-if="cvContent" class="bg-white rounded-xl shadow-soft p-4 sm:p-6 mb-6">
        <h2 class="text-lg sm:text-xl font-semibold text-gray-800 mb-4">Generated CV Content:</h2>
        <div class="bg-gray-50 rounded-lg p-3 sm:p-4 text-sm sm:text-base font-mono whitespace-pre-wrap">
          {{ cvContent }}
        </div>
      </div>

      <div v-if="cvContent" class="bg-white rounded-xl shadow-soft p-4 sm:p-6">
        <h2 class="text-lg sm:text-xl font-semibold text-gray-800 mb-4">Complete Your Order</h2>
        <div class="text-base sm:text-lg font-medium text-gray-700 mb-6">
          <p>Base Price: <span class="text-primary-600">${{ (currentAmount / 100).toFixed(2) }}</span></p>
        </div>

        <PromoCode 
          :amount="currentAmount" 
          @discountApplied="handleDiscountApplied" 
        />

        <button 
          @click="handlePayNowClick" 
          class="btn btn-primary w-full py-3 mt-6 text-sm sm:text-base flex items-center justify-center"
        >
          <span class="mr-2">Pay Now</span>
          <span class="font-medium">
            {{ discountedAmount ? `$${(finalAmount / 100).toFixed(2)}` : `$${(currentAmount / 100).toFixed(2)}` }}
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { generateCV, downloadCvPdf, createPaymentSession } from '../services/api';
import PromoCode from '../components/PromoCode.vue';

const userText = ref('');
const cvContent = ref('');
const isLoading = ref(false);
const error = ref('');
const currentAmount = ref(1001); // Base price in cents
const discountedAmount = ref(null);
const isDownloadButtonVisible = ref(false);

const handleDiscountApplied = (discountData) => {
  console.log("Discount Applied in ServiceView:", discountData);
  discountedAmount.value = discountData.discountedAmount;
  // Update the amount that will be used for payment
};

const finalAmount = computed(() => {
  return discountedAmount.value || currentAmount.value;
});

const handleGenerateClick = async () => {
  if (!userText.value) {
    error.value = 'Please enter some text about your experience and skills.';
    return;
  }

  isLoading.value = true;
  error.value = '';
  isDownloadButtonVisible.value = false;

  try {
    const response = await generateCV(userText.value);
    cvContent.value = response;
    isDownloadButtonVisible.value = true;
  } catch (err) {
    error.value = 'Error generating CV. Please try again.';
    console.error('Error:', err);
    isDownloadButtonVisible.value = false;
  } finally {
    isLoading.value = false;
  }
};

const handleDownloadClick = async () => {
  try {
    await downloadCvPdf(userText.value);
  } catch (err) {
    console.error('Error downloading PDF:', err);
    error.value = 'Error downloading PDF. Please try again.';
  }
};

let testPaymentCounter = 0;

const handlePayNowClick = async () => {
  testPaymentCounter++;
  const testEmail = 'test' + testPaymentCounter + '@example.com';
  const testFirstName = 'Test' + testPaymentCounter;
  const testLastName = 'User' + testPaymentCounter;
  const itemDescription = 'AI-Powered CV Generation Test ' + testPaymentCounter;
  const amount = finalAmount.value; // Amount in cents

  try {
    isLoading.value = true;
    error.value = '';

    // Store user text in localStorage for later use in DownloadReadyView
    localStorage.setItem('cv_user_text', userText.value);

    const response = await createPaymentSession({
      amount: amount,
      user_text: userText.value, // Pass user_text to backend
      billing_data: {
        email: testEmail,
        first_name: testFirstName,
        last_name: testLastName,
        phone_number: "+201234567890",
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
      error.value = 'Failed to initiate payment. Please try again.';
    }
  } catch (e) {
    error.value = 'Payment initiation failed. Please check your connection and try again.';
  } finally {
    isLoading.value = false;
  }
};
</script>
