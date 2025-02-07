<template>
  <div class="welcome-page">
    <div class="hero-section">
      <h1>Welcome to CV Builder!</h1>
      <p>Create your professional CV easily with our AI-powered CV Builder. Get started below!</p>
      <router-link to="/service" class="get-started-button">Get Started</router-link>
    </div>
  </div>
</template>

<script setup>
// No script logic needed yet
</script>

<style scoped>
.welcome-page {
  text-align: center; /* Center content in WelcomePage (though hero-section centers too) */
  padding: 20px; /* Keep some padding on the overall page */
}

.hero-section { /* Hero Section Styles */
  background-color: #f0f0f0; /* Light background color for hero section */
  padding: 40px 20px;
  border-radius: 8px;
  margin-bottom: 20px; /* Space below hero section */
  text-align: center; /* Center text within hero section */
}

h1 {
  margin-bottom: 15px;
  color: #333;
}

p {
  color: #555;
  margin-bottom: 20px; /* Space below paragraph */
  font-size: 1.1rem;
}

.get-started-button { /* "Get Started" Button Styles */
  background-color: #007bff; /* Example primary button color */
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

.get-started-button:hover {
  background-color: #0056b3; /* Darker color on hover */
}
</style>
