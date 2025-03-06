<template>
  <div class="personal-info-page">
    <h2 class="section-title">Personal Information</h2>
    <p class="section-description">Please provide your basic contact information for your CV.</p>

    <div class="form-group">
      <label for="fullName" class="essential-field">Full Name</label>
      <input 
        id="fullName"
        type="text"
        v-model="localFormData.fullName"
        placeholder="Your full name"
        class="form-input essential-input"
        @input="updateFormData"
        required
      />
    </div>

    <div class="form-group">
      <label for="email" class="essential-field">Email Address</label>
      <input 
        id="email"
        type="email"
        v-model="localFormData.email"
        placeholder="your-email@example.com"
        class="form-input essential-input"
        @input="updateFormData"
        required
      />
    </div>

    <div class="form-group">
      <label for="phone" class="essential-field">Phone Number</label>
      <input 
        id="phone"
        type="tel"
        v-model="localFormData.phone"
        placeholder="Your phone number"
        class="form-input essential-input"
        @input="updateFormData"
        required
      />
    </div>

    <div class="form-group">
      <label for="location">Location (City, Region - optional)</label>
      <input 
        id="location"
        type="text"
        v-model="localFormData.location"
        placeholder="e.g., New York, NY"
        class="form-input"
        @input="updateFormData"
      />
    </div>

    <div class="form-group">
      <label for="headline" class="essential-field">Professional Headline/Title</label>
      <input 
        id="headline"
        type="text"
        v-model="localFormData.headline"
        placeholder="e.g., Senior Software Engineer"
        class="form-input essential-input"
        @input="updateFormData"
        required
      />
    </div>

    <div class="form-actions">
      <button 
        @click="goToNextPage" 
        class="btn-primary"
      >
        Next: Work Experience
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

const emit = defineEmits(['update-form-data', 'next-page']);

// Create a local copy of the form data to avoid directly modifying the prop
const localFormData = ref({
  fullName: '',
  email: '',
  phone: '',
  location: '',
  headline: ''
});

// Initialize local form data from props
onMounted(() => {
  // Initialize with data from props, or use empty strings if not available
  localFormData.value = {
    fullName: props.formData.fullName || '',
    email: props.formData.email || '',
    phone: props.formData.phone || '',
    location: props.formData.location || '',
    headline: props.formData.headline || ''
  };
});

// Watch for changes to the formData prop
watch(() => props.formData, (newValue) => {
  localFormData.value = {
    fullName: newValue.fullName || localFormData.value.fullName,
    email: newValue.email || localFormData.value.email,
    phone: newValue.phone || localFormData.value.phone,
    location: newValue.location || localFormData.value.location,
    headline: newValue.headline || localFormData.value.headline
  };
}, { deep: true });

// Emit form data updates to parent
const updateFormData = () => {
  emit('update-form-data', {
    ...props.formData,
    ...localFormData.value
  });
};

// Go to the next page
const goToNextPage = () => {
  // First, ensure form data is updated
  updateFormData();
  
  // Then emit next-page event
  emit('next-page');
};
</script>

<style scoped>
.personal-info-page {
  max-width: 640px;
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

.form-input {
  width: 100%;
  padding: 0.625rem 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-size: 0.95rem;
  transition: all 0.2s ease-in-out;
}

.form-input:focus {
  outline: none;
  border-color: #3498DB;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.15);
}

.essential-input {
  background-color: rgba(253, 230, 138, 0.1); /* Very subtle yellow highlight */
  border-left: 3px solid #3498DB; /* Blue left border for emphasis */
}

.form-actions {
  display: flex;
  justify-content: flex-end;
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

.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.4);
}

@media (max-width: 640px) {
  .personal-info-page {
    padding: 1rem;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .btn-primary {
    width: 100%;
  }
}
</style>
