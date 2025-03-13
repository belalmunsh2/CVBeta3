<template>
  <div class="mb-8">
    <h2 class="text-xl sm:text-2xl font-semibold text-gray-800 mb-5 flex items-center">
      <svg class="w-6 h-6 mr-2 text-primary-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      CV Preview
    </h2>
    
    <div class="flex flex-col items-center">
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

<script>
import { getCvPreview } from '../services/api';

export default {
  name: 'Preview',
  props: {
    userText: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      previewUrl: '',
      loading: false,
      error: ''
    };
  },
  computed: {
    hasUserText() {
      return this.userText && this.userText.trim().length > 0;
    }
  },
  mounted() {
    // Automatically get preview when component is mounted
    if (this.hasUserText) {
      this.getPreview();
    }
  },
  methods: {
    async getPreview() {
      if (!this.hasUserText) {
        this.error = 'Please provide your CV text first.';
        return;
      }
      
      this.loading = true;
      this.error = '';
      
      try {
        const blob = await getCvPreview(this.userText);
        this.previewUrl = URL.createObjectURL(blob);
      } catch (error) {
        console.error('Error fetching preview:', error);
        this.error = 'Failed to load preview. Please try again.';
      } finally {
        this.loading = false;
      }
    }
  }
};
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