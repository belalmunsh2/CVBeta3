<template>
  <div class="cv-form">
    <h2>Enter Your CV Text</h2>
    <textarea id="cv-text-input" rows="10" placeholder="Paste or type your CV text here..."></textarea>
    <button class="submit-button">Submit</button>
  </div>
</template>

<script setup>
// No script logic needed for now
</script>

<style scoped>
.cv-form {
  text-align: center;
  padding: 20px;
}

textarea {
  width: 100%;
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: inherit;
  font-size: inherit;
}

.submit-button {
  background-color: #28a745; /* Example green submit button color */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #1e7e34; /* Darker green on hover */
}
</style>