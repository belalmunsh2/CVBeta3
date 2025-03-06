<template>
  <div class="work-experience-page">
    <h2 class="section-title">Work Experience</h2>
    <p class="section-description">Add your relevant work experience. You can add multiple entries and arrange them in order of importance.</p>

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

const props = defineProps({
  formData: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update-form-data', 'next-page', 'prev-page']);

// Local array to store work experiences
const workExperiences = ref([]);

// Initialize with data from props or create a default empty experience
onMounted(() => {
  if (props.formData.workExperiences && props.formData.workExperiences.length > 0) {
    workExperiences.value = [...props.formData.workExperiences];
  } else {
    // Add one empty experience block by default
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

// Go to the next page
const goToNextPage = () => {
  // Ensure form data is updated before navigating
  updateFormData();
  emit('next-page');
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
  width: 100%;
  padding: 0.75rem;
  background-color: #edf2f7;
  border: 1px dashed #a0aec0;
  color: #3498DB;
  font-weight: 500;
  border-radius: 0.375rem;
  margin-bottom: 2rem;
  transition: all 0.2s ease;
  cursor: pointer;
}

.btn-add:hover {
  background-color: #e2e8f0;
  border-color: #3498DB;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.btn-primary {
  background-color: #3498DB;
  color: white;
  font-weight: 500;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.btn-secondary {
  background-color: white;
  color: #3498DB;
  font-weight: 500;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  border: 1px solid #3498DB;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background-color: #f7fafc;
}

@media (max-width: 640px) {
  .work-experience-page {
    padding: 1rem;
  }
  
  .navigation-buttons {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .btn-primary, .btn-secondary {
    width: 100%;
  }
}
</style>
