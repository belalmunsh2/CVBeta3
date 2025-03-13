<template>
  <div class="work-experience-page">
    <h2 class="section-title">Work Experience</h2>
    <p class="section-description">Add your relevant work experience. You can add multiple entries and arrange them in order of importance.</p>

    <div v-if="formErrors.length > 0" class="error-summary">
      <FormErrorMessage 
        v-for="(error, index) in formErrors" 
        :key="index" 
        :message="error" 
      />
    </div>

    <div class="blocks-container">
      <WorkExperienceBlock 
        v-for="(experience, index) in workExperiences" 
        :key="index"
        :experience="experience"
        :show-remove-button="workExperiences.length > 1"
        @update="updateExperience(index, $event)"
        @remove="removeExperience(index)"
      />
    </div>

    <button
      type="button"
      class="btn-add"
      @click="addExperience"
    >
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5 mr-2">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
      </svg>
      Add Work Experience
    </button>

    <div class="navigation-buttons">
      <button 
        @click="$emit('prev-page')" 
        class="btn-secondary"
      >
        Previous: Personal Information
      </button>
      <button 
        @click="goToNextPage" 
        class="btn-primary"
      >
        Next: Education
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import WorkExperienceBlock from './WorkExperienceBlock.vue';
import FormErrorMessage from './FormErrorMessage.vue';

const props = defineProps({
  formData: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update-form-data', 'prev-page', 'next-page']);

// Local state for work experiences
const workExperiences = ref([]);

// Track form-level errors
const formErrors = ref([]);

// Initialize work experiences
onMounted(() => {
  if (props.formData.workExperiences && props.formData.workExperiences.length > 0) {
    workExperiences.value = [...props.formData.workExperiences];
  } else {
    // Initialize with a single empty experience if none exist
    workExperiences.value = [
      {
        jobTitle: '',
        companyName: '',
        startDate: '',
        endDate: '',
        currentPosition: false,
        responsibilities: ''
      }
    ];
    
    // Update parent's formData with the initial empty experience
    updateFormData();
  }
});

// Watch for changes to formData.workExperiences
watch(() => props.formData.workExperiences, (newValue) => {
  if (newValue && JSON.stringify(newValue) !== JSON.stringify(workExperiences.value)) {
    workExperiences.value = [...newValue];
  }
}, { deep: true });

// Add a new experience block
const addExperience = () => {
  workExperiences.value.push({
    jobTitle: '',
    companyName: '',
    startDate: '',
    endDate: '',
    currentPosition: false,
    responsibilities: ''
  });
  updateFormData();
};

// Update a specific experience
const updateExperience = (index, updatedExperience) => {
  workExperiences.value[index] = updatedExperience;
  updateFormData();
};

// Remove an experience
const removeExperience = (index) => {
  workExperiences.value.splice(index, 1);
  updateFormData();
};

// Update parent component's formData
const updateFormData = () => {
  emit('update-form-data', {
    ...props.formData,
    workExperiences: [...workExperiences.value]
  });
};

// Validate form data before proceeding
const validateForm = () => {
  // Clear previous errors
  formErrors.value = [];

  // Check if there are any work experiences
  if (workExperiences.value.length === 0) {
    formErrors.value.push('At least one work experience is required');
    return false;
  }

  // Validate each work experience entry
  let isValid = true;
  let hasAtLeastOneValid = false;

  workExperiences.value.forEach((exp, index) => {
    // Check for required fields
    if (!exp.jobTitle || exp.jobTitle.trim() === '') {
      formErrors.value.push(`Experience #${index + 1}: Job title is required`);
      isValid = false;
    }

    if (!exp.companyName || exp.companyName.trim() === '') {
      formErrors.value.push(`Experience #${index + 1}: Company name is required`);
      isValid = false;
    }

    if (!exp.startDate || exp.startDate.trim() === '') {
      formErrors.value.push(`Experience #${index + 1}: Start date is required`);
      isValid = false;
    }

    if (!exp.currentPosition && (!exp.endDate || exp.endDate.trim() === '')) {
      formErrors.value.push(`Experience #${index + 1}: End date is required when not a current position`);
      isValid = false;
    }

    if (!exp.responsibilities || exp.responsibilities.trim() === '') {
      formErrors.value.push(`Experience #${index + 1}: Responsibilities are required`);
      isValid = false;
    }

    // Check if this experience is valid
    if (exp.jobTitle && exp.companyName && exp.startDate && 
        (exp.currentPosition || exp.endDate) && exp.responsibilities) {
      hasAtLeastOneValid = true;
    }
  });

  // If no valid experiences were found
  if (!hasAtLeastOneValid && workExperiences.value.length > 0) {
    formErrors.value.push('Please complete at least one work experience with all required fields');
    return false;
  }

  return isValid;
};

// Go to the next page
const goToNextPage = () => {
  // Ensure form data is updated before validation
  updateFormData();
  
  // Validate form before proceeding
  if (validateForm()) {
    // Proceed to next page if validation passes
    emit('next-page');
  } else {
    // Scroll to error summary for better UX
    const errorSummary = document.querySelector('.error-summary');
    if (errorSummary) {
      errorSummary.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
};
</script>

<style scoped>
.work-experience-page {
  max-width: 720px;
  margin: 0 auto;
  padding: 1.5rem;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 0.5rem;
}

.section-description {
  color: #4a5568;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.blocks-container {
  margin-bottom: 1.5rem;
}

.btn-add {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #EBF5FB;
  color: #3498DB;
  border: 1px dashed #3498DB;
  border-radius: 0.375rem;
  padding: 0.625rem 1rem;
  margin-bottom: 2rem;
  width: 100%;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-add:hover {
  background-color: #D6EAF8;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1.5rem;
}

.btn-secondary {
  background-color: #EBF5FB;
  color: #3498DB;
  font-weight: 500;
  border-radius: 0.375rem;
  padding: 0.75rem 1.5rem;
  border: 1px solid #3498DB;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background-color: #D6EAF8;
}

.btn-primary {
  background-color: #3498DB;
  color: white;
  font-weight: 500;
  border-radius: 0.375rem;
  padding: 0.75rem 1.5rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.error-summary {
  background-color: #FEF2F2;
  border: 1px solid #FCA5A5;
  border-radius: 0.375rem;
  padding: 1rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 640px) {
  .work-experience-page {
    padding: 1rem;
  }
  
  .navigation-buttons {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .btn-secondary,
  .btn-primary {
    width: 100%;
  }
}
</style>
