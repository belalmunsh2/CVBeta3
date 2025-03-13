<template>
  <div class="education-page">
    <h2 class="section-title">Education</h2>
    <p class="section-description">Add your educational background. List your most recent or relevant education first.</p>

    <div v-if="formErrors.length > 0" class="error-summary">
      <FormErrorMessage 
        v-for="(error, index) in formErrors" 
        :key="index" 
        :message="error" 
      />
    </div>

    <div class="blocks-container">
      <EducationBlock 
        v-for="(education, index) in educations" 
        :key="index"
        :education="education"
        :show-remove-button="educations.length > 1"
        @update="updateEducation(index, $event)"
        @remove="removeEducation(index)"
      />
    </div>

    <button
      type="button"
      class="btn-add"
      @click="addEducation"
    >
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5 mr-2">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
      </svg>
      Add Education
    </button>

    <div class="navigation-buttons">
      <button 
        @click="$emit('prev-page')" 
        class="btn-secondary"
      >
        Previous: Work Experience
      </button>
      <button 
        @click="goToNextPage" 
        class="btn-primary"
      >
        Next: Skills & Summary
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import EducationBlock from './EducationBlock.vue';
import FormErrorMessage from './FormErrorMessage.vue';

const props = defineProps({
  formData: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update-form-data', 'prev-page', 'next-page']);

// Local array to store education entries
const educations = ref([]);

// Track form-level errors
const formErrors = ref([]);

// Initialize with data from props or create a default empty education entry
onMounted(() => {
  if (props.formData.educations && props.formData.educations.length > 0) {
    educations.value = [...props.formData.educations];
  } else {
    // Add one empty education block by default
    educations.value = [
      {
        degreeEarned: '',
        institutionName: '',
        graduationDate: '',
        description: ''
      }
    ];
    
    // Update parent's formData
    updateFormData();
  }
});

// Watch for changes to formData.educations
watch(() => props.formData.educations, (newValue) => {
  if (newValue && JSON.stringify(newValue) !== JSON.stringify(educations.value)) {
    educations.value = [...newValue];
  }
}, { deep: true });

// Add a new education block
const addEducation = () => {
  educations.value.push({
    degreeEarned: '',
    institutionName: '',
    graduationDate: '',
    description: ''
  });
  updateFormData();
};

// Update a specific education entry
const updateEducation = (index, updatedEducation) => {
  educations.value[index] = updatedEducation;
  updateFormData();
};

// Remove an education entry
const removeEducation = (index) => {
  educations.value.splice(index, 1);
  updateFormData();
};

// Update parent component's formData
const updateFormData = () => {
  emit('update-form-data', {
    ...props.formData,
    educations: [...educations.value]
  });
};

// Validate form data before proceeding
const validateForm = () => {
  // Clear previous errors
  formErrors.value = [];

  // Check if there are any education entries
  if (educations.value.length === 0) {
    formErrors.value.push('At least one education entry is required');
    return false;
  }

  // Validate each education entry
  let isValid = true;
  let hasAtLeastOneValid = false;

  educations.value.forEach((edu, index) => {
    // Check for required fields
    if (!edu.degreeEarned || edu.degreeEarned.trim() === '') {
      formErrors.value.push(`Education #${index + 1}: Degree is required`);
      isValid = false;
    }

    if (!edu.institutionName || edu.institutionName.trim() === '') {
      formErrors.value.push(`Education #${index + 1}: Institution name is required`);
      isValid = false;
    }

    if (!edu.graduationDate || edu.graduationDate.trim() === '') {
      formErrors.value.push(`Education #${index + 1}: Graduation date is required`);
      isValid = false;
    }

    // Check if this education entry is valid
    if (edu.degreeEarned && edu.institutionName && edu.graduationDate) {
      hasAtLeastOneValid = true;
    }
  });

  // If no valid education entries were found
  if (!hasAtLeastOneValid && educations.value.length > 0) {
    formErrors.value.push('Please complete at least one education entry with all required fields');
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
.education-page {
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
  .education-page {
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
