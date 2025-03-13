<template>
  <div class="bg-gray-50 min-h-screen">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <h1 class="text-2xl sm:text-3xl font-bold text-primary-600 text-center mb-8">CV Creator Service</h1>
      
      <div class="bg-white rounded-xl shadow-sm p-6 sm:p-8 mb-8 transition-shadow duration-300 hover:shadow-md">
        <CVForm @cv-submit="handleFormSubmit" :is-generating="isGeneratingCV" />
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

      <div v-if="isLoading" class="flex justify-center items-center py-8">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-600"></div>
        <p class="ml-4 text-gray-600">Generating your CV...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { generateCV } from '../services/api';
import CVForm from '../components/CvForm.vue';

const router = useRouter();
const userText = ref('');
const userData = ref(null);
const isLoading = ref(false);
const error = ref('');
const isGeneratingCV = ref(false);

// Listen for the cv-submit event from the CVForm component
onMounted(() => {
  document.addEventListener('cv-submit', (event) => {
    const { userData: formData, formattedText } = event.detail;
    userData.value = formData;
    userText.value = formattedText;
    handleGenerateClick();
  });
});

// Handle form submission from the CVForm component
const handleFormSubmit = (data) => {
  isGeneratingCV.value = true; // Set loading state immediately
  userData.value = data.userData;
  userText.value = data.formattedText;
  handleGenerateClick();
};

const handleGenerateClick = async () => {
  if (!userText.value) {
    error.value = 'Please complete the CV form with your information.';
    isGeneratingCV.value = false;
    return;
  }

  isLoading.value = true;
  error.value = '';
  isGeneratingCV.value = true;

  try {
    const response = await generateCV(userText.value);
    // After successful CV generation, redirect to download page
    router.push({
      name: 'download-ready',
      params: {},
      query: {
        content: encodeURIComponent(response),
        userText: encodeURIComponent(userText.value)
      }
    });
  } catch (err) {
    error.value = 'Error generating CV. Please try again.';
    console.error('Error:', err);
    isGeneratingCV.value = false;
  } finally {
    isLoading.value = false;
  }
};
</script>
