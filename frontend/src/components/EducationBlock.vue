<template>
  <div class="education-block">
    <div class="block-header">
      <h3 class="block-title">Education Entry</h3>
      <button 
        v-if="showRemoveButton" 
        type="button" 
        class="btn-remove" 
        @click="$emit('remove')"
        aria-label="Remove education"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <div class="form-group">
      <label for="degreeEarned" class="essential-field">Degree Earned</label>
      <input 
        id="degreeEarned"
        type="text"
        v-model="educationData.degreeEarned"
        placeholder="e.g., Bachelor of Science in Computer Science"
        class="form-input essential-input"
        @input="updateData"
        required
      />
    </div>

    <div class="form-group">
      <label for="institutionName" class="essential-field">Institution Name</label>
      <input 
        id="institutionName"
        type="text"
        v-model="educationData.institutionName"
        placeholder="e.g., Massachusetts Institute of Technology"
        class="form-input essential-input"
        @input="updateData"
        required
      />
    </div>

    <div class="form-group">
      <label class="essential-field">Graduation Date</label>
      <SelectDateBox 
        :initial-date="educationData.graduationDate"
        @date-selected="onGraduationDateSelected"
      />
    </div>

    <div class="form-group">
      <label for="description">Additional Information (Optional)</label>
      <textarea 
        id="description"
        v-model="educationData.description"
        placeholder="Relevant coursework, honors, activities, etc."
        class="form-textarea"
        rows="3"
        @input="updateData"
      ></textarea>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import SelectDateBox from './SelectDateBox.vue';

const props = defineProps({
  education: {
    type: Object,
    required: true
  },
  showRemoveButton: {
    type: Boolean,
    default: true
  }
});

const emit = defineEmits(['update', 'remove']);

// Create a local copy of the education data
const educationData = ref({
  degreeEarned: '',
  institutionName: '',
  graduationDate: '',
  description: ''
});

// Initialize local data from props
onMounted(() => {
  educationData.value = {
    degreeEarned: props.education.degreeEarned || '',
    institutionName: props.education.institutionName || '',
    graduationDate: props.education.graduationDate || '',
    description: props.education.description || ''
  };
});

// Watch for changes to the education prop
watch(() => props.education, (newValue) => {
  if (newValue) {
    educationData.value = {
      degreeEarned: newValue.degreeEarned || educationData.value.degreeEarned,
      institutionName: newValue.institutionName || educationData.value.institutionName,
      graduationDate: newValue.graduationDate || educationData.value.graduationDate,
      description: newValue.description || educationData.value.description
    };
  }
}, { deep: true });

// Handle date selection
const onGraduationDateSelected = (date) => {
  educationData.value.graduationDate = date;
  updateData();
};

// Update parent component with changes
const updateData = () => {
  emit('update', educationData.value);
};
</script>

<style scoped>
.education-block {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  transition: all 0.2s ease-in-out;
}

.education-block:hover {
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

@media (max-width: 640px) {
  .education-block {
    padding: 1rem;
  }
}
</style>
