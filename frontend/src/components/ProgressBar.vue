<template>
  <div class="progress-container">
    <div 
      class="progress-bar" 
      :style="{ width: `${progress}%` }"
      :aria-valuenow="progress"
      aria-valuemin="0"
      aria-valuemax="100"
      role="progressbar"
    ></div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  progress: {
    type: Number,
    required: true,
    validator: (value) => value >= 0 && value <= 100,
    default: 0
  }
});

// Ensure progress is always between 0 and 100
const clampedProgress = computed(() => {
  return Math.min(100, Math.max(0, props.progress));
});
</script>

<style scoped>
.progress-container {
  width: 100%;
  height: 4px;
  background-color: #e2e8f0; /* Light gray background for the track */
  border-radius: 2px;
  overflow: hidden;
  margin: 0.5rem 0;
}

.progress-bar {
  height: 100%;
  background-color: #3498DB; /* Primary blue color */
  border-radius: 2px;
  transition: width 0.3s ease; /* Smooth animation when progress changes */
}

@media (max-width: 640px) {
  .progress-container {
    height: 3px; /* Slightly smaller on mobile */
  }
}
</style>
