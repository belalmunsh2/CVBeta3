<template>
  <div class="promo-code-container">
    <div class="input-group">
      <input 
        type="text" 
        v-model="promoCode"
        placeholder="Enter promo code"
        class="promo-input"
        :disabled="loading"
      />
      <button 
        @click="applyPromoCode" 
        class="apply-button"
        :disabled="loading || !promoCode"
      >
        {{ loading ? 'Applying...' : 'Apply Promo' }}
      </button>
    </div>

    <!-- Error Message -->
    <div v-if="errorMessage" class="message error">
      {{ errorMessage }}
    </div>

    <!-- Success Message -->
    <div v-if="discountedPrice && !errorMessage" class="message success">
      <div class="discount-details">
        <p>Discount applied: {{ discountPercentage }}%</p>
        <p class="price-breakdown">
          <span class="original-price">Original: ${{ (originalAmount / 100).toFixed(2) }}</span>
          <span class="discounted-price">New Price: ${{ (discountedPrice / 100).toFixed(2) }}</span>
        </p>
        <p class="savings">You save: ${{ ((originalAmount - discountedPrice) / 100).toFixed(2) }}</p>
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

<style scoped>
.promo-code-container {
  max-width: 400px;
  margin: 1rem auto;
  padding: 1rem;
}

.input-group {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.promo-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.apply-button {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.apply-button:hover:not(:disabled) {
  background-color: #45a049;
}

.apply-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.message {
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
}

.error {
  background-color: #ffebee;
  color: #c62828;
  border: 1px solid #ffcdd2;
}

.success {
  background-color: #e8f5e9;
  color: #2e7d32;
  border: 1px solid #c8e6c9;
}

.discount-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.price-breakdown {
  display: flex;
  justify-content: space-between;
  margin: 0.5rem 0;
}

.original-price {
  text-decoration: line-through;
  color: #666;
}

.discounted-price {
  font-weight: bold;
}

.savings {
  font-weight: bold;
  color: #2e7d32;
}
</style>
