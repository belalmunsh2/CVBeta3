<template>
  <div class="certifications-additional-page">
    <h2 class="section-title">Certifications & Additional Details</h2>
    <p class="section-description">Add certifications, projects, and additional information to enhance your CV.</p>

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

// Initialize local data from props
onMounted(() => {
  localFormData.value = {
    linkedin: props.formData.linkedin || ''
  };
  
  // Initialize certifications
  if (props.formData.certifications && Array.isArray(props.formData.certifications)) {
    certifications.value = [...props.formData.certifications];
  } else {
    // Add one empty certification by default
    addCertification();
  }
  
  // Initialize projects
  if (props.formData.projects && Array.isArray(props.formData.projects)) {
    projects.value = [...props.formData.projects];
  } else {
    // Add one empty project by default
    addProject();
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

// Submit the form
const submitForm = () => {
  updateFormData();
  emit('submit-form');
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
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.section-container:last-of-type {
  border-bottom: none;
}

.subsection-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 1rem;
}

.block-subtitle {
  font-size: 1rem;
  font-weight: 500;
  color: #4a5568;
}

.certification-container,
.project-container {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.25rem;
  margin-bottom: 1rem;
  transition: all 0.2s ease-in-out;
}

.certification-container:hover,
.project-container:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border-color: #cbd5e0;
}

.block-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
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
  width: 100%;
  padding: 0.75rem;
  background-color: #edf2f7;
  border: 1px dashed #a0aec0;
  color: #3498DB;
  font-weight: 500;
  border-radius: 0.375rem;
  margin-top: 0.5rem;
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
  margin-top: 2rem;
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

.btn-submit {
  background-color: #38a169;
  color: white;
  font-weight: 500;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
}

.btn-submit:hover {
  background-color: #2f855a;
}

@media (max-width: 640px) {
  .certifications-additional-page {
    padding: 1rem;
  }
  
  .navigation-buttons {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .btn-secondary, .btn-submit {
    width: 100%;
  }
}
</style>
