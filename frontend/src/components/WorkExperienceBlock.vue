<template>
  <div class="work-experience-block">
    <div class="block-header">
      <h3 class="block-title">Work Experience</h3>
      <button 
        v-if="showRemoveButton" 
        type="button" 
        class="btn-remove" 
        @click="$emit('remove')"
        aria-label="Remove work experience"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <div class="form-group">
      <label for="jobTitle" class="essential-field">Job Title</label>
      <input 
        id="jobTitle"
        type="text"
        v-model="experienceData.jobTitle"
        placeholder="e.g., Senior Frontend Developer"
        class="form-input essential-input"
        @input="updateData"
        required
      />
    </div>

    <div class="form-group">
      <label for="companyName" class="essential-field">Company Name</label>
      <input 
        id="companyName"
        type="text"
        v-model="experienceData.companyName"
        placeholder="e.g., Acme Corporation"
        class="form-input essential-input"
        @input="updateData"
        required
      />
    </div>

    <div class="date-fields">
      <div class="form-group date-field">
        <label class="essential-field">Start Date</label>
        <SelectDateBox 
          :initial-date="experienceData.startDate"
          @date-selected="onStartDateSelected"
        />
      </div>

      <div class="form-group date-field">
        <div class="date-field-header">
          <label class="essential-field">End Date</label>
          <div class="current-checkbox">
            <input 
              type="checkbox" 
              id="currentPosition" 
              v-model="experienceData.currentPosition"
              @change="handleCurrentPositionChange"
            />
            <label for="currentPosition" class="current-label">Current position</label>
          </div>
        </div>
        <SelectDateBox 
          v-if="!experienceData.currentPosition"
          :initial-date="experienceData.endDate"
          @date-selected="onEndDateSelected"
          :disabled="experienceData.currentPosition"
        />
        <div v-else class="present-indicator">Present</div>
      </div>
    </div>

    <div class="form-group">
      <label for="responsibilities" class="essential-field">Responsibilities & Achievements</label>
      <textarea 
        id="responsibilities"
        v-model="experienceData.responsibilities"
        placeholder="Enter your responsibilities and achievements, using bullet points or short sentences. Press Enter for each new point."
        class="form-textarea essential-input"
        rows="5"
        @input="updateData"
        required
      ></textarea>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import SelectDateBox from './SelectDateBox.vue';

const props = defineProps({
  experience: {
    type: Object,
    required: true
  },
  showRemoveButton: {
    type: Boolean,
    default: true
  }
});

const emit = defineEmits(['update', 'remove']);

// Create a local copy of the experience data
const experienceData = ref({
  jobTitle: '',
  companyName: '',
  startDate: '',
  endDate: '',
  currentPosition: false,
  responsibilities: ''
});

// Initialize local data from props
onMounted(() => {
  experienceData.value = {
    jobTitle: props.experience.jobTitle || '',
    companyName: props.experience.companyName || '',
    startDate: props.experience.startDate || '',
    endDate: props.experience.endDate || '',
    currentPosition: props.experience.currentPosition || false,
    responsibilities: props.experience.responsibilities || ''
  };
});

// Watch for changes to the experience prop
watch(() => props.experience, (newValue) => {
  if (newValue) {
    experienceData.value = {
      jobTitle: newValue.jobTitle || experienceData.value.jobTitle,
      companyName: newValue.companyName || experienceData.value.companyName,
      startDate: newValue.startDate || experienceData.value.startDate,
      endDate: newValue.endDate || experienceData.value.endDate,
      currentPosition: newValue.currentPosition || experienceData.value.currentPosition,
      responsibilities: newValue.responsibilities || experienceData.value.responsibilities
    };
  }
}, { deep: true });

// Handle "Current position" checkbox change
const handleCurrentPositionChange = () => {
  if (experienceData.value.currentPosition) {
    // If checked as current position, clear end date
    experienceData.value.endDate = '';
  }
  updateData();
};

// Handle date selections
const onStartDateSelected = (date) => {
  experienceData.value.startDate = date;
  updateData();
};

const onEndDateSelected = (date) => {
  experienceData.value.endDate = date;
  updateData();
};

// Update parent component with changes
const updateData = () => {
  emit('update', experienceData.value);
};
</script>

<style scoped>
.work-experience-block {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  transition: all 0.2s ease-in-out;
}

.work-experience-block:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border-color: #cbd5e0;
}

.block-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.block-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #2d3748;
}

.btn-remove {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.25rem;
  border-radius: 0.375rem;
  background-color: transparent;
  color: #e53e3e;
  border: 1px solid #e53e3e;
  transition: all 0.2s ease;
}

.btn-remove:hover {
  background-color: #e53e3e;
  color: white;
}

.form-group {
  margin-bottom: 1.25rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #4a5568;
  font-size: 0.95rem;
}

.essential-field::after {
  content: "*";
  color: #e53e3e;
  margin-left: 0.25rem;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.625rem 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-size: 0.95rem;
  transition: all 0.2s ease-in-out;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #3498DB;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.15);
}

.essential-input {
  background-color: rgba(253, 230, 138, 0.1);
  border-left: 3px solid #3498DB;
}

.date-fields {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.date-field {
  flex: 1;
}

.date-field-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.current-checkbox {
  display: flex;
  align-items: center;
}

.current-label {
  margin: 0 0 0 0.375rem;
  font-size: 0.875rem;
  color: #4a5568;
}

.present-indicator {
  padding: 0.625rem 0.75rem;
  background-color: #edf2f7;
  border-radius: 0.375rem;
  color: #4a5568;
  font-size: 0.95rem;
  border: 1px solid #e2e8f0;
}

@media (max-width: 640px) {
  .date-fields {
    flex-direction: column;
    gap: 0;
  }
  
  .date-field {
    margin-bottom: 1.25rem;
  }
}
</style>
