<template>
  <div v-if="message" class="error-message" role="alert">
    <svg xmlns="http://www.w3.org/2000/svg" class="error-icon" viewBox="0 0 20 20" fill="currentColor">
      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
    </svg>
    <span>{{ message }}</span>
  </div>
</template>

<script setup>
defineProps({
  message: {
    type: String,
    default: ''
  }
});
</script>

<style scoped>
.error-message {
  display: flex;
  align-items: center;
  color: #e53e3e;
  font-size: 0.875rem;
  margin-top: 0.5rem;
  animation: fadeIn 0.3s ease-in-out;
}

.error-icon {
  width: 1rem;
  height: 1rem;
  margin-right: 0.375rem;
  flex-shrink: 0;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-5px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
