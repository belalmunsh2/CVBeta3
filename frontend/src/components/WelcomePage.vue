<template>
  <div class="welcome-page">
    <div class="hero-section">
      <h1>Welcome to CV Builder!</h1>
      <p>Create your professional CV easily with our AI-powered CV Builder. Get started below!</p>
      <router-link to="/service" class="get-started-button">Get Started</router-link>
    </div>
  </div>  </template>

<script setup lang="ts">
// No script logic needed in WelcomePage.vue now - script block is intentionally empty
</script>

<style scoped>
.welcome-page {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f0f0;
}

.hero-section {
  text-align: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.hero-section h1 {
  color: #333;
}

.hero-section p {
  color: #666;
  margin-bottom: 20px;
}

.get-started-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.get-started-button:hover {
  background-color: #0056b3;
}
</style>