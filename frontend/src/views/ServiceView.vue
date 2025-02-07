<template>
  <div class="service-page">
    <h1>CV Creator Service Page</h1>
    <p>This is the CV Creator Service Page. Input your CV text below.</p>
    <CvForm />
  </div>
</template>

<script setup>
import CvForm from '../components/CvForm.vue';
</script>

<style scoped>
.service-page {
  text-align: center;
  padding: 20px;
}

h1 {
  margin-bottom: 15px;
  color: #333;
}

p {
  color: #555;
}
</style>
