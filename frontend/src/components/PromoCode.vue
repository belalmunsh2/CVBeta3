<template>
  <div class="promo-code-section">
    <!-- Marketing Titles -->
    <div class="mb-8">
      <div class="bg-primary-50 rounded-lg p-4 mb-4 border-l-4 border-primary-500 shadow-sm">
        <h3 class="text-lg sm:text-xl font-bold text-primary-700 mb-1 flex items-center">
          <svg class="w-5 h-5 mr-2 text-primary-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M5 2a2 2 0 00-2 2v14l3.5-2 3.5 2 3.5-2 3.5 2V4a2 2 0 00-2-2H5zm4.707 3.707a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L8.414 9.5l2.293-2.293z" clip-rule="evenodd" />
          </svg>
          Get 20% Off: Suggest to a Friend!
        </h3>
        <p class="text-primary-600 text-sm">Share this tool and help your friends create professional CVs too.</p>
      </div>
      
      <div class="bg-blue-50 rounded-lg p-4 mb-4 border-l-4 border-blue-500 shadow-sm">
        <h3 class="text-lg sm:text-xl font-bold text-blue-700 mb-1 flex items-center">
          <svg class="w-5 h-5 mr-2 text-blue-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
          Unlimited Edits (Within Your Subscription Period)
        </h3>
        <p class="text-blue-600 text-sm">Revise and perfect your CV as many times as you need.</p>
      </div>
      
      <div class="bg-indigo-50 rounded-lg p-4 mb-4 border-l-4 border-indigo-500 shadow-sm">
        <h3 class="text-lg sm:text-xl font-bold text-indigo-700 mb-1 flex items-center">
          <svg class="w-5 h-5 mr-2 text-indigo-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
          </svg>
          Generate Professional CVs in Minutes with AI Power!
        </h3>
        <p class="text-indigo-600 text-sm">Let AI technology transform your experience into an employer-ready CV.</p>
      </div>
    </div>
    
    <!-- Promo Code Section -->
    <div class="bg-white rounded-lg shadow-sm p-6 border border-gray-100">
      <h3 class="text-lg font-semibold text-gray-800 mb-4">Have a promo code?</h3>
      
      <div class="flex flex-col sm:flex-row gap-3 mb-4">
        <input 
          type="text" 
          v-model="promoCode"
          placeholder="Enter promo code"
          class="flex-1 px-4 py-2.5 border border-gray-200 rounded-lg focus:ring-2 focus:ring-primary-300 focus:border-primary-500 transition-all duration-200 outline-none text-sm sm:text-base shadow-sm"
          :disabled="loading"
        />
        <button 
          @click="applyPromoCode" 
          class="bg-primary-600 hover:bg-primary-700 focus:ring-primary-500 text-white font-medium rounded-lg px-5 py-2.5 text-sm sm:text-base transition-all duration-200 shadow-sm hover:shadow focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-70 disabled:cursor-not-allowed"
          :disabled="loading || !promoCode"
        >
          <span v-if="loading" class="flex items-center justify-center">
            <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Applying...
          </span>
          <span v-else>Apply Code</span>
        </button>
      </div>

      <!-- Error Message -->
      <div v-if="errorMessage" class="bg-red-50 text-red-700 p-4 rounded-lg mb-4 text-sm border border-red-100">
        <div class="flex items-start">
          <svg class="h-5 w-5 text-red-600 mt-0.5 mr-2 flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414-1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
          </svg>
          <span>{{ errorMessage }}</span>
        </div>
      </div>

      <!-- Success Message -->
      <div v-if="discountedPrice && !errorMessage" class="bg-green-50 text-green-700 p-4 rounded-lg mb-4 border border-green-100">
        <div class="flex flex-col">
          <div class="flex items-center font-medium mb-2">
            <svg class="h-5 w-5 text-green-600 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
            <span>Discount applied: {{ discountPercentage }}%</span>
          </div>
          <div class="pl-7 text-sm">
            <p class="mb-1">
              <span class="line-through text-gray-500">Original: ${{ (originalAmount / 100).toFixed(2) }}</span>
            </p>
            <p class="font-bold text-green-700 text-base">
              New Price: ${{ (discountedPrice / 100).toFixed(2) }}
            </p>
            <p class="mt-1 text-green-600">
              You save: ${{ ((originalAmount - discountedPrice) / 100).toFixed(2) }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { API_BASE_URL } from '../services/api'

// Props
const props = defineProps({
  amount: {
    type: Number,
    required: true,
    default: 1000 // Default amount in cents
  }
})

// Emits
const emit = defineEmits(['discountApplied'])

// Reactive state
const promoCode = ref('')
const errorMessage = ref('')
const discountedPrice = ref(null)
const discountPercentage = ref(null)
const originalAmount = ref(props.amount)
const loading = ref(false)

// Methods
const applyPromoCode = async () => {
  if (!promoCode.value || loading.value) return

  loading.value = true
  errorMessage.value = ''
  discountedPrice.value = null
  discountPercentage.value = null

  try {
    const response = await axios.post(`${API_BASE_URL}/api/apply-coupon`, {
      promo_code: promoCode.value,
      amount: props.amount
    })

    if (response.data.error) {
      errorMessage.value = response.data.error
    } else {
      discountedPrice.value = response.data.discounted_amount
      discountPercentage.value = response.data.discount_percentage
      originalAmount.value = response.data.original_amount
      
      // Emit the discounted price to parent component
      emit('discountApplied', {
        discountedAmount: response.data.discounted_amount,
        discountPercentage: response.data.discount_percentage,
        originalAmount: response.data.original_amount
      })
    }
  } catch (error) {
    console.error('Error applying promo code:', error)
    errorMessage.value = error.response?.data?.error || 'Failed to apply promo code'
  } finally {
    loading.value = false
  }
}
</script>
