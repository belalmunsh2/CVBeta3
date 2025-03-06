import './utils/globals.js' // Import globals first to prevent reference errors
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'

createApp(App)
  .use(router)
  .mount('#app')