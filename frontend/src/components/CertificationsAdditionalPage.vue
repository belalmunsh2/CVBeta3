<template>
  <div class="certifications-additional-page">
    <h2 class="section-title">Certifications & Additional Details</h2>
    <p class="section-description">Add certifications, projects, and additional information to enhance your CV.</p>

    <div v-if="formErrors.length > 0" class="error-summary">
      <FormErrorMessage 
        v-for="(error, index) in formErrors" 
        :key="index" 
        :message="error" 
      />
    </div>

    <!-- Certifications Section -->
    <div class="section-container">
      <h3 class="subsection-title">Certifications & Licenses</h3>
      
      <div v-for="(certification, index) in certifications" :key="index" class="certification-container">
        <div class="block-header">
          <h4 class="block-subtitle">Certification {{ index + 1 }}</h4>
          <button 
            v-if="certifications.length > 1"
            type="button" 
            class="btn-remove" 
            @click="removeCertification(index)"
            aria-label="Remove certification"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="form-group">
          <label for="certification-name-${index}">Certification/License Name</label>
          <input 
            :id="`certification-name-${index}`"
            type="text"
            v-model="certification.name"
            placeholder="e.g., AWS Certified Solutions Architect"
            class="form-input"
            @input="updateFormData"
          />
        </div>
        
        <div class="form-group">
          <label for="certification-organization-${index}">Issuing Organization</label>
          <input 
            :id="`certification-organization-${index}`"
            type="text"
            v-model="certification.organization"
            placeholder="e.g., Amazon Web Services"
            class="form-input"
            @input="updateFormData"
          />
        </div>
        
        <div class="form-group">
          <label>Date Issued</label>
          <SelectDateBox 
            :initial-date="certification.date"
            @date-selected="date => updateCertificationDate(index, date)"
          />
        </div>
      </div>
      
      <button
        type="button"
        class="btn-add"
        @click="addCertification"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5 mr-2">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Add Certification
      </button>
    </div>
    
    <!-- Projects/Portfolio Section -->
    <div class="section-container">
      <h3 class="subsection-title">Projects & Portfolio</h3>
      
      <div v-for="(project, index) in projects" :key="index" class="project-container">
        <div class="block-header">
          <h4 class="block-subtitle">Project {{ index + 1 }}</h4>
          <button 
            v-if="projects.length > 1"
            type="button" 
            class="btn-remove" 
            @click="removeProject(index)"
            aria-label="Remove project"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="form-group">
          <label for="project-name-${index}">Project Name</label>
          <input 
            :id="`project-name-${index}`"
            type="text"
            v-model="project.name"
            placeholder="e.g., E-commerce Website"
            class="form-input"
            @input="updateFormData"
          />
        </div>
        
        <div class="form-group">
          <label for="project-url-${index}">Link URL</label>
          <input 
            :id="`project-url-${index}`"
            type="url"
            v-model="project.url"
            placeholder="e.g., https://myproject.com"
            class="form-input"
            @input="updateFormData"
          />
        </div>
        
        <div class="form-group">
          <label for="project-description-${index}">Short Description</label>
          <textarea 
            :id="`project-description-${index}`"
            v-model="project.description"
            placeholder="Briefly describe the project, your role, and technologies used."
            class="form-textarea"
            rows="3"
            @input="updateFormData"
          ></textarea>
        </div>
      </div>
      
      <button
        type="button"
        class="btn-add"
        @click="addProject"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5 mr-2">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Add Project
      </button>
    </div>
    
    <!-- LinkedIn Profile -->
    <div class="section-container">
      <h3 class="subsection-title">Social & Professional Links</h3>
      
      <div class="form-group">
        <label for="linkedin">LinkedIn Profile URL</label>
        <input 
          id="linkedin"
          type="url"
          v-model="localFormData.linkedin"
          placeholder="e.g., https://linkedin.com/in/yourname"
          class="form-input"
          @input="updateFormData"
        />
        <p class="hint-text">If provided, should be a valid LinkedIn profile URL</p>
      </div>
    </div>
    
    <div class="navigation-buttons">
      <button 
        @click="$emit('prev-page')" 
        class="btn-secondary"
      >
        Previous: Skills & Summary
      </button>
      <button 
        @click="submitForm" 
        class="btn-submit"
      >
        Generate CV!
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import SelectDateBox from './SelectDateBox.vue';
import FormErrorMessage from './FormErrorMessage.vue';

const props = defineProps({
  formData: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update-form-data', 'prev-page', 'submit-form']);

// Local form data
const localFormData = ref({
  linkedin: ''
});

// Arrays for certifications and projects
const certifications = ref([]);
const projects = ref([]);

// Form errors
const formErrors = ref([]);

// Initialize local data from props
onMounted(() => {
  localFormData.value = {
    linkedin: props.formData.linkedin || ''
  };
  
  // Initialize certifications
  if (props.formData.certifications && Array.isArray(props.formData.certifications)) {
    certifications.value = [...props.formData.certifications];
  } else {
    certifications.value = [];
  }
  
  // Initialize projects
  if (props.formData.projects && Array.isArray(props.formData.projects)) {
    projects.value = [...props.formData.projects];
  } else {
    projects.value = [];
  }
});

// Watch for changes to formData props
watch(() => props.formData, (newValue) => {
  if (newValue) {
    localFormData.value = {
      linkedin: newValue.linkedin || localFormData.value.linkedin
    };
    
    if (newValue.certifications && Array.isArray(newValue.certifications)) {
      certifications.value = [...newValue.certifications];
    }
    
    if (newValue.projects && Array.isArray(newValue.projects)) {
      projects.value = [...newValue.projects];
    }
  }
}, { deep: true });

// Certification methods
const addCertification = () => {
  certifications.value.push({
    name: '',
    organization: '',
    date: ''
  });
  updateFormData();
};

const removeCertification = (index) => {
  certifications.value.splice(index, 1);
  updateFormData();
};

const updateCertificationDate = (index, date) => {
  certifications.value[index].date = date;
  updateFormData();
};

// Project methods
const addProject = () => {
  projects.value.push({
    name: '',
    url: '',
    description: ''
  });
  updateFormData();
};

const removeProject = (index) => {
  projects.value.splice(index, 1);
  updateFormData();
};

// Update parent component's formData
const updateFormData = () => {
  emit('update-form-data', {
    ...props.formData,
    ...localFormData.value,
    certifications: [...certifications.value],
    projects: [...projects.value]
  });
};

// Validate the form data
const validateForm = () => {
  // Reset errors
  formErrors.value = [];
  
  let isValid = true;
  
  // Validate LinkedIn URL format if provided
  if (localFormData.value.linkedin && localFormData.value.linkedin.trim() !== '') {
    const linkedinRegex = /^(https?:\/\/)?(www\.)?linkedin\.com\/in\/[\w-]+\/?$/;
    if (!linkedinRegex.test(localFormData.value.linkedin)) {
      formErrors.value.push('Please enter a valid LinkedIn profile URL (e.g., https://linkedin.com/in/yourname)');
      isValid = false;
    }
  }
  
  // Validate essential fields from previous pages
  if (!props.formData.fullName || props.formData.fullName.trim() === '') {
    formErrors.value.push('Please complete your personal information (Full Name is required)');
    isValid = false;
  }
  
  if (!props.formData.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(props.formData.email)) {
    formErrors.value.push('Please complete your personal information with a valid email address');
    isValid = false;
  }
  
  if (!props.formData.phone || props.formData.phone.trim() === '') {
    formErrors.value.push('Please complete your personal information (Phone number is required)');
    isValid = false;
  }
  
  if (!props.formData.headline || props.formData.headline.trim() === '') {
    formErrors.value.push('Please complete your personal information (Professional headline is required)');
    isValid = false;
  }
  
  // Validate work experiences
  if (!props.formData.workExperiences || !props.formData.workExperiences.length) {
    formErrors.value.push('At least one work experience entry is required');
    isValid = false;
  } else {
    const validExperience = props.formData.workExperiences.some(exp => 
      exp.jobTitle && exp.jobTitle.trim() !== '' && 
      exp.companyName && exp.companyName.trim() !== '' &&
      exp.startDate && exp.startDate.trim() !== ''
    );
    
    if (!validExperience) {
      formErrors.value.push('Please complete at least one work experience entry with all required fields');
      isValid = false;
    }
  }
  
  // Validate education
  if (!props.formData.educations || !props.formData.educations.length) {
    formErrors.value.push('At least one education entry is required');
    isValid = false;
  } else {
    const validEducation = props.formData.educations.some(edu => 
      edu.degreeEarned && edu.degreeEarned.trim() !== '' && 
      edu.institutionName && edu.institutionName.trim() !== '' &&
      edu.graduationDate && edu.graduationDate.trim() !== ''
    );
    
    if (!validEducation) {
      formErrors.value.push('Please complete at least one education entry with all required fields');
      isValid = false;
    }
  }
  
  // Validate skills
  if (!props.formData.skills || !props.formData.skills.length) {
    formErrors.value.push('At least one skill is required');
    isValid = false;
  }
  
  return isValid;
};

// Submit the form
const submitForm = () => {
  // Ensure form data is updated
  updateFormData();
  
  // Validate before submitting
  if (validateForm()) {
    emit('submit-form');
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
.certifications-additional-page {
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

.section-container {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background-color: #f8fafc;
  border-radius: 0.5rem;
}

.subsection-title {
  font-size: 1.25rem;
  font-weight: 500;
  color: #2d3748;
  margin-bottom: 1rem;
}

.certification-container,
.project-container {
  padding: 1rem;
  margin-bottom: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  background-color: white;
}

.block-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.block-subtitle {
  font-size: 1rem;
  font-weight: 500;
  color: #4a5568;
  margin: 0;
}

.btn-remove {
  background: none;
  border: none;
  color: #718096;
  cursor: pointer;
  padding: 0.25rem;
  transition: color 0.2s ease;
}

.btn-remove:hover {
  color: #e53e3e;
}

.btn-remove svg {
  width: 1rem;
  height: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #4a5568;
  font-size: 0.95rem;
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

.btn-add {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #EBF5FB;
  color: #3498DB;
  border: 1px dashed #3498DB;
  border-radius: 0.375rem;
  padding: 0.625rem 1rem;
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
  margin-top: 2rem;
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

.btn-submit {
  background-color: #48bb78;
  color: white;
  font-weight: 500;
  border-radius: 0.375rem;
  padding: 0.75rem 1.5rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-submit:hover {
  background-color: #38a169;
}

.error-summary {
  background-color: #FEF2F2;
  border: 1px solid #FCA5A5;
  border-radius: 0.375rem;
  padding: 1rem;
  margin-bottom: 1.5rem;
}

.hint-text {
  font-size: 0.8rem;
  color: #718096;
  margin-top: 0.375rem;
}

@media (max-width: 640px) {
  .certifications-additional-page {
    padding: 1rem;
  }
  
  .section-container {
    padding: 1rem;
  }
  
  .navigation-buttons {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .btn-secondary,
  .btn-submit {
    width: 100%;
  }
}
</style>
