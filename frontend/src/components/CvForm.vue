<template>
  <div class="cv-form">
    <ProgressBar :progress="progress" />
    
    <div class="form-container">
      <!-- Personal Info Page -->
      <PersonalInfoPage 
        v-if="currentPage === 1"
        :form-data="formData"
        @update-form-data="updateFormData"
        @next-page="nextPage"
      />
      
      <!-- Work Experience Page -->
      <WorkExperiencePage 
        v-if="currentPage === 2"
        :form-data="formData"
        @update-form-data="updateFormData"
        @prev-page="prevPage"
        @next-page="nextPage"
      />
      
      <!-- Education Page -->
      <EducationPage 
        v-if="currentPage === 3"
        :form-data="formData"
        @update-form-data="updateFormData"
        @prev-page="prevPage"
        @next-page="nextPage"
      />
      
      <!-- Skills & Summary Page -->
      <SkillsSummaryPage 
        v-if="currentPage === 4"
        :form-data="formData"
        @update-form-data="updateFormData"
        @prev-page="prevPage"
        @next-page="nextPage"
      />
      
      <!-- Certifications & Additional Page -->
      <CertificationsAdditionalPage 
        v-if="currentPage === 5"
        :form-data="formData"
        :is-generating="props.isGenerating"
        @update-form-data="updateFormData"
        @prev-page="prevPage"
        @submit-form="submitForm"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue';
import ProgressBar from './ProgressBar.vue';
import PersonalInfoPage from './PersonalInfoPage.vue';
import WorkExperiencePage from './WorkExperiencePage.vue';
import EducationPage from './EducationPage.vue';
import SkillsSummaryPage from './SkillsSummaryPage.vue';
import CertificationsAdditionalPage from './CertificationsAdditionalPage.vue';

const props = defineProps({
  isGenerating: Boolean
});

const TOTAL_PAGES = 5;

// Current page state
const currentPage = ref(1);

// Form data state
const formData = ref({
  // Personal Info
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  location: '',
  jobTitle: '',
  
  // Work Experience
  workExperiences: [],
  
  // Education
  educations: [],
  
  // Skills & Summary
  skills: [],
  summary: '',
  
  // Certifications & Additional
  certifications: [],
  projects: [],
  linkedin: ''
});

// Computed progress percentage
const progress = computed(() => {
  return ((currentPage.value - 1) / (TOTAL_PAGES - 1)) * 100;
});

// Navigation methods
const nextPage = () => {
  if (currentPage.value < TOTAL_PAGES) {
    currentPage.value++;
    window.scrollTo(0, 0);
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    window.scrollTo(0, 0);
  }
};

// Form data update method
const updateFormData = (newData) => {
  formData.value = { ...newData };
};

// Form submission method
const submitForm = () => {
  const formDataToSubmit = { ...formData.value };
  // Format the data and emit it to parent component
  const payload = {
    userData: formDataToSubmit
  };
  
  // Create a formatted text representation of the CV for API submission
  const formattedCV = formatCVData(formDataToSubmit);
  
  // Emit the event with the formatted data
  const event = new CustomEvent('cv-submit', { 
    detail: { 
      userData: formDataToSubmit,
      formattedText: formattedCV 
    } 
  });
  document.dispatchEvent(event);
};

// Helper function to format CV data into a text representation
const formatCVData = (data) => {
  let formatted = '';
  
  // Personal Information
  formatted += `${data.firstName} ${data.lastName}\n`;
  formatted += `${data.jobTitle}\n`;
  formatted += `${data.email} | ${data.phone} | ${data.location}\n\n`;
  
  // Professional Summary
  if (data.summary) {
    formatted += `PROFESSIONAL SUMMARY\n`;
    formatted += `${data.summary}\n\n`;
  }
  
  // Work Experience
  if (data.workExperiences && data.workExperiences.length > 0) {
    formatted += `WORK EXPERIENCE\n`;
    data.workExperiences.forEach(job => {
      formatted += `${job.title} at ${job.company}\n`;
      
      // Format dates
      const startDate = job.startDate || 'N/A';
      const endDate = job.endDate || 'Present';
      formatted += `${startDate} - ${endDate}\n`;
      
      // Format responsibilities
      if (job.responsibilities) {
        formatted += `${job.responsibilities}\n`;
      }
      formatted += '\n';
    });
  }
  
  // Education
  if (data.educations && data.educations.length > 0) {
    formatted += `EDUCATION\n`;
    data.educations.forEach(edu => {
      formatted += `${edu.degree} - ${edu.institution}\n`;
      formatted += `Graduated: ${edu.graduationDate || 'N/A'}\n\n`;
    });
  }
  
  // Skills
  if (data.skills && data.skills.length > 0) {
    formatted += `SKILLS\n`;
    formatted += `${Array.isArray(data.skills) ? data.skills.join(', ') : data.skills}\n\n`;
  }
  
  // Certifications
  if (data.certifications && data.certifications.length > 0) {
    formatted += `CERTIFICATIONS\n`;
    data.certifications.forEach(cert => {
      if (cert.name) {
        formatted += `${cert.name}`;
        if (cert.organization) {
          formatted += ` - ${cert.organization}`;
        }
        if (cert.date) {
          formatted += ` (${cert.date})`;
        }
        formatted += '\n';
      }
    });
    formatted += '\n';
  }
  
  // Projects
  if (data.projects && data.projects.length > 0) {
    formatted += `PROJECTS\n`;
    data.projects.forEach(project => {
      if (project.name) {
        formatted += `${project.name}`;
        if (project.url) {
          formatted += ` - ${project.url}`;
        }
        if (project.description) {
          formatted += `\n${project.description}`;
        }
        formatted += '\n\n';
      }
    });
  }
  
  // LinkedIn
  if (data.linkedin) {
    formatted += `LinkedIn: ${data.linkedin}\n`;
  }
  
  return formatted;
};
</script>

<style scoped>
.cv-form {
  max-width: 800px;
  margin: 0 auto;
  padding: 1.5rem;
}

.form-container {
  background-color: white;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  margin-top: 1.5rem;
  overflow: hidden;
}

@media (max-width: 640px) {
  .cv-form {
    padding: 1rem 0.5rem;
  }
}
</style>