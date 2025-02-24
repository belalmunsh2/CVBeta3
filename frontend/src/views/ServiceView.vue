<template>
  <div class="service-page">
    <h1>CV Creator Service</h1>
    
    <div class="input-section">
      <textarea
        v-model="userText"
        placeholder="Enter your experience, skills, and other relevant information..."
        :disabled="isLoading"
      ></textarea>
      
      <div class="button-group">
        <button @click="handleGenerateClick" :disabled="isLoading">
          {{ isLoading ? 'Generating...' : 'Generate CV' }}
        </button>
        <button @click="handleDownloadClick" :disabled="!cvContent || isLoading">
          Download PDF
        </button>
      </div>
    </div>

    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <div v-if="cvContent" class="cv-preview">
      <h2>Generated CV Content:</h2>
      <div class="content">{{ cvContent }}</div>
    </div>

    <div class="payment-section" v-if="cvContent">
      <h2>Complete Your Order</h2>
      <div class="price-info">
        <p>Base Price: ${{ (currentAmount / 100).toFixed(2) }}</p>
      </div>

      <PromoCode 
        :amount="currentAmount" 
        @discountApplied="handleDiscountApplied" 
      />

      <button 
        @click="handlePayNowClick" 
        class="pay-button"
      >
        Pay Now {{ discountedAmount ? `$${(finalAmount / 100).toFixed(2)}` : `$${(currentAmount / 100).toFixed(2)}` }}
      </button>
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

  try {
    const response = await generateCV(userText.value);
    cvContent.value = response;
  } catch (err) {
    error.value = 'Error generating CV. Please try again.';
    console.error('Error:', err);
  } finally {
    isLoading.value = false;
  }
};

const handleDownloadClick = async () => {
  try {
    const pdfBlob = await downloadCvPdf({ user_text: userText.value });
    const url = window.URL.createObjectURL(pdfBlob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'cv.pdf');
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  } catch (err) {
    console.error('Error downloading PDF:', err);
    error.value = 'Error downloading PDF. Please try again.';
  }
};

let testPaymentCounter = 0;

const handlePayNowClick = async () => {
  testPaymentCounter++;
  const testEmail = 'test' + testPaymentCounter + '@example.com';
  const amount = finalAmount.value; // Amount in cents

  try {
    isLoading.value = true;
    error.value = '';

    const response = await createPaymentSession({
      amount: amount, // Assuming 'amount' is already correctly set (e.g., from finalAmount.value)
      billing_data: {
        email: testEmail,
        first_name: "Test",
        last_name: "User",
        phone_number: "+201234567890",
        country: "EGY"
      }
    });

    if (response && response.payment_url) {
      window.location.href = response.payment_url;
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

<style scoped>
.service-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.input-section {
  margin: 2rem 0;
}

textarea {
  width: 100%;
  min-height: 200px;
  padding: 1rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  resize: vertical;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: none;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover:not(:disabled) {
  background-color: #45a049;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff0000;
  margin: 1rem 0;
  padding: 1rem;
  background-color: #ffebee;
  border-radius: 4px;
}

.cv-preview {
  margin: 2rem 0;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.content {
  white-space: pre-wrap;
  font-family: monospace;
  padding: 1rem;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.payment-section {
  margin-top: 2rem;
  padding: 2rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.price-info {
  margin: 1rem 0;
  font-size: 1.2rem;
}

.pay-button {
  margin-top: 1rem;
  width: 100%;
  padding: 1rem;
  font-size: 1.2rem;
  background-color: #2196F3;
}

.pay-button:hover:not(:disabled) {
  background-color: #1976D2;
}
</style>
