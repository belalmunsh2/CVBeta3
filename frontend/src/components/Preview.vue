<template>
  <div class="mb-8">
    <h2 class="text-xl sm:text-2xl font-semibold text-gray-800 mb-5 flex items-center">
      <svg class="w-6 h-6 mr-2 text-primary-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      CV Preview
    </h2>
    
    <div class="flex flex-col items-center">
      <button 
        @click="getPreview" 
        :disabled="loading || !hasUserText"
        class="bg-primary-600 hover:bg-primary-700 focus:ring-primary-500 text-white font-medium rounded-lg px-6 py-3 mb-6 text-base transition-all duration-200 shadow-sm hover:shadow flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <svg v-if="loading" class="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <span v-if="loading">Generating Preview...</span>
        <span v-else>Show Preview</span>
      </button>
      
      <div v-if="loading" class="text-gray-600 text-center mb-4">
        Creating your CV preview, please wait...
      </div>
      
      <div v-if="previewUrl" class="preview-container border border-gray-200 rounded-lg shadow-md overflow-hidden max-w-full">
        <img :src="previewUrl" alt="Blurred CV Preview" class="max-w-full h-auto" />
        <div class="p-4 bg-gray-50 border-t border-gray-200">
          <p class="text-gray-700 text-sm">
            <span class="font-semibold">Note:</span> This is a preview with the bottom half blurred. 
            <span class="text-primary-700">Purchase to download the complete CV.</span>
          </p>
        </div>
      </div>
      
      <div v-if="error" class="mt-4 p-4 bg-red-50 text-red-700 rounded-lg border border-red-100 text-sm">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps, defineExpose } from 'vue';
import { getCvPreview } from '../services/api';

const props = defineProps({
  userText: {
    type: String,
    required: true
  }
});

const previewUrl = ref('');
const loading = ref(false);
const error = ref('');

const hasUserText = computed(() => {
  return props.userText && props.userText.trim().length > 0;
});

const getPreview = async () => {
  if (!hasUserText.value) {
    error.value = 'Please provide your CV text first.';
    return;
  }
  
  loading.value = true;
  error.value = '';
  
  try {
    const blob = await getCvPreview(props.userText);
    previewUrl.value = URL.createObjectURL(blob);
  } catch (err) {
    console.error('Error fetching preview:', err);
    error.value = 'Failed to load preview. Please try again.';
  } finally {
    loading.value = false;
  }
};

// Expose the getPreview method to parent components
defineExpose({
  getPreview
});
</script>

<style scoped>
.preview-container {
  max-width: 100%;
  width: 100%;
  /* max-height: 700px; */
  transition: all 0.2s ease-in-out;
}

.preview-container:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

img {
  display: block;
  margin: 0 auto;
}
</style>