<template>
  <svg 
    xmlns="http://www.w3.org/2000/svg" 
    :width="size" 
    :height="size" 
    :viewBox="`0 0 24 24`" 
    :fill="fill" 
    :stroke="stroke" 
    :class="customClass">
    <g v-if="name === 'document'">
      <path d="M14 2H6C4.89543 2 4 2.89543 4 4V20C4 21.1046 4.89543 22 6 22H18C19.1046 22 20 21.1046 20 20V8L14 2Z" />
      <path d="M14 2V8H20" />
      <path d="M16 13H8" />
      <path d="M16 17H8" />
      <path d="M10 9H8" />
    </g>
    <g v-else-if="name === 'star'">
      <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
    </g>
    <g v-else-if="name === 'shield'">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    </g>
    <g v-else-if="name === 'magic'">
      <path d="M12 2L14.85 8.35L22 9.82L16.72 14.54L18 22L12 18.35L6 22L7.27 14.54L2 9.82L9.15 8.35L12 2Z" />
    </g>
    <g v-else-if="name === 'check'">
      <path d="M20 6L9 17L4 12" />
    </g>
    <g v-else-if="name === 'question'">
      <circle cx="12" cy="12" r="10" />
      <path d="M12 16V16.01" />
      <path d="M12 13C12.5523 13 13 12.5523 13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12" />
      <path d="M9.09 9C9.3251 8.33167 9.7889 7.76811 10.4 7.40913C11.0111 7.05016 11.7333 6.91894 12.4384 7.03871C13.1435 7.15849 13.7881 7.52152 14.2665 8.06353C14.745 8.60553 15.0303 9.29152 15.0707 10.005C15.1112 10.7184 14.9044 11.4255 14.4847 12.0027C14.0649 12.5799 13.4612 12.9934 12.78 13.173C12.53 13.23 12.27 13.26 12 13.27" />
    </g>
    <g v-else>
      <!-- Default: user icon -->
      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
      <circle cx="12" cy="7" r="4" />
    </g>
  </svg>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    default: 'user'
  },
  size: {
    type: [Number, String],
    default: 24
  },
  stroke: {
    type: String,
    default: 'currentColor'
  },
  fill: {
    type: String,
    default: 'none'
  },
  customClass: {
    type: String,
    default: ''
  }
});
</script>
