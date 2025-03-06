<template>
  <div class="skills-summary-page">
    <h2 class="section-title">Skills & Professional Summary</h2>
    <p class="section-description">Add your skills and write a professional summary to highlight your expertise.</p>

    <div class="form-group">
      <div class="label-container">
        <label for="skills">Skills</label>
      </div>
      <div class="skills-input-container">
        <input 
          type="text" 
          id="skill-input"
          v-model="newSkill"
          @keydown.enter.prevent="addSkill"
          @keydown.tab.prevent="addSkill"
          @keydown.comma.prevent="addSkill"
          placeholder="Type a skill and press Enter, Tab, or comma to add"
          class="form-input"
        />
        <div class="skills-tags">
          <div 
            v-for="(skill, index) in localSkills" 
            :key="index" 
            class="skill-tag"
          >
            {{ skill }}
            <button 
              @click="removeSkill(index)" 
              class="tag-remove-btn" 
              type="button"
              aria-label="Remove skill"
            >
              &times;
            </button>
          </div>
        </div>
        <p class="hint-text">Add your key skills one at a time, such as "JavaScript", "Project Management", or "Data Analysis"</p>
      </div>
    </div>

    <div class="form-group">
      <div class="label-container">
        <label for="professionalSummary" class="recommended-field">
          Professional Summary
          <svg xmlns="http://www.w3.org/2000/svg" class="lightbulb-icon" viewBox="0 0 20 20" fill="currentColor">
            <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
          </svg>
        </label>
      </div>
      <textarea 
        id="professionalSummary"
        v-model="localFormData.professionalSummary"
        placeholder="Write a brief professional summary or career objective that highlights your experience, skills, and career goals. This will appear at the top of your CV."
        class="form-textarea recommended-input"
        rows="5"
        @input="updateFormData"
      ></textarea>
      <p class="hint-text">A strong professional summary helps recruiters quickly understand your value (3-5 sentences recommended)</p>
    </div>

    <div class="navigation-buttons">
      <button 
        @click="$emit('prev-page')" 
        class="btn-secondary"
      >
        Previous: Education
      </button>
      <button 
        @click="goToNextPage" 
        class="btn-primary"
      >
        Next: Certifications & More
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
  formData: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update-form-data', 'next-page', 'prev-page']);

// Local form data
const localFormData = ref({
  professionalSummary: ''
});

// Skills handling
const localSkills = ref([]);
const newSkill = ref('');

// Initialize local data from props
onMounted(() => {
  localFormData.value = {
    professionalSummary: props.formData.professionalSummary || ''
  };
  
  // Initialize skills
  if (props.formData.skills && Array.isArray(props.formData.skills)) {
    localSkills.value = [...props.formData.skills];
  }
});

// Watch for changes to formData props
watch(() => props.formData, (newValue) => {
  if (newValue) {
    localFormData.value = {
      professionalSummary: newValue.professionalSummary || localFormData.value.professionalSummary
    };
    
    if (newValue.skills && Array.isArray(newValue.skills)) {
      localSkills.value = [...newValue.skills];
    }
  }
}, { deep: true });

// Add a new skill
const addSkill = () => {
  const skill = newSkill.value.trim();
  
  if (skill && !localSkills.value.includes(skill)) {
    localSkills.value.push(skill);
    newSkill.value = '';
    updateFormData();
  }
};

// Remove a skill
const removeSkill = (index) => {
  localSkills.value.splice(index, 1);
  updateFormData();
};

// Update parent component's formData
const updateFormData = () => {
  emit('update-form-data', {
    ...props.formData,
    ...localFormData.value,
    skills: [...localSkills.value]
  });
};

// Navigate to next page
const goToNextPage = () => {
  updateFormData();
  emit('next-page');
};
</script>

<style scoped>
.skills-summary-page {
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

.form-group {
  margin-bottom: 1.5rem;
}

.label-container {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

label {
  display: inline-block;
  font-weight: 500;
  color: #4a5568;
  font-size: 0.95rem;
}

.lightbulb-icon {
  width: 1rem;
  height: 1rem;
  margin-left: 0.25rem;
  color: #f6ad55;
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

.recommended-field::after {
  content: " (Recommended)";
  color: #3498DB;
  font-size: 0.85rem;
  font-weight: normal;
}

.recommended-input {
  border-left: 3px solid #3498DB;
}

.skills-input-container {
  margin-bottom: 1rem;
}

.skills-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.skill-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  background-color: #edf2f7;
  color: #2d3748;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}

.skill-tag:hover {
  background-color: #e2e8f0;
}

.tag-remove-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin-left: 0.25rem;
  font-size: 1.25rem;
  line-height: 0.75rem;
  color: #718096;
  padding: 0.125rem 0.25rem;
}

.tag-remove-btn:hover {
  color: #e53e3e;
}

.hint-text {
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: #718096;
  font-style: italic;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
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
  .skills-summary-page {
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
