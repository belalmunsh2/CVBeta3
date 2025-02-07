<template>
  <div class="welcome-page">
    <div class="hero-section">
      <h1>Welcome to CV Builder!</h1>
      <p>Create your professional CV easily with our AI-powered CV Builder. Get started below!</p>
      <router-link to="/service" class="get-started-button">Get Started</router-link>
    </div>
    <textarea v-model="userText" placeholder="Enter your experience and skills here..." rows="10" cols="80"></textarea><br>
    <button @click="generateCvClicked">Generate CV</button>

    <div v-if="generatedCvContent">
      <h2>Generated CV Content:</h2>
      <pre style="white-space: pre-wrap;">{{ generatedCvContent }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { generateCV } from '../services/api'; 

const userText = ref('');
const generatedCvContent = ref('');

const generateCvClicked = async () => {
  generatedCvContent.value = ''; 
  const response = await generateCV(userText.value);
  generatedCvContent.value = response;
};
</script>

<style scoped>
.welcome-page {
  text-align: center; 
  padding: 20px; 
}

.hero-section { 
  background-color: #f0f0f0; 
  padding: 40px 20px;
  border-radius: 8px;
  margin-bottom: 20px; 
  text-align: center; 
}

h1 {
  margin-bottom: 15px;
  color: #333;
}

p {
  color: #555;
  margin-bottom: 20px; 
  font-size: 1.1rem;
}

.get-started-button { 
  background-color: #007bff; 
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease; 
}

.get-started-button:hover {
  background-color: #0056b3; 
}
</style>
