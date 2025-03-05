<template>
  <div class="min-h-screen flex flex-col">
    <!-- Header Section -->
    <header class="bg-white border-b border-gray-200 py-2 sm:py-4 sticky top-0 z-50 shadow-soft">
      <div class="container mx-auto px-3 sm:px-4 flex justify-between items-center">
        <h1 class="text-xl sm:text-2xl font-bold text-primary-600">CV Builder</h1>
        <nav class="overflow-x-auto -mx-3 px-3">
          <ul class="flex space-x-3 sm:space-x-6 whitespace-nowrap">
            <li><a href="#templates" class="text-sm sm:text-base text-gray-600 hover:text-primary-500 transition-colors font-medium">Templates</a></li>
            <li><a href="#why-choose-us" class="text-sm sm:text-base text-gray-600 hover:text-primary-500 transition-colors font-medium">Why Us</a></li>
            <li><a href="#faq" class="text-sm sm:text-base text-gray-600 hover:text-primary-500 transition-colors font-medium">FAQ</a></li>
            <li><a href="#reviews" class="text-sm sm:text-base text-gray-600 hover:text-primary-500 transition-colors font-medium">Reviews</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="flex-grow">
      <!-- Hero Section -->
      <section id="hero" class="bg-gradient-to-b from-primary-50 to-white py-24 md:py-36">
        <div class="container-narrow mx-auto text-center">
          <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 mb-6 leading-tight animate-slide-in">Create a Professional CV <span class="text-primary-600">in Minutes</span></h2>
          <p class="text-xl text-gray-600 mb-10 max-w-3xl mx-auto leading-relaxed font-light">Land your dream job with our AI-powered CV generator. Create a professional CV that stands out from the crowd.</p>
          <router-link to="/service" class="btn btn-primary text-lg shadow-md hover:shadow-lg transform hover:-translate-y-1 transition duration-300">
            Generate My CV
          </router-link>
        </div>
      </section>

      <!-- Template View Section -->
      <section id="templates" class="section bg-white">
        <div class="container mx-auto px-4">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center">Choose from Professional Templates</h2>
          <p class="text-gray-600 text-center max-w-3xl mx-auto mb-12">Select from our professionally designed and ATS-optimized templates</p>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Template Card 1 -->
            <div class="card group">
              <div class="bg-gray-100 h-56 mb-5 rounded-xl flex items-center justify-center overflow-hidden group-hover:bg-primary-50 transition-colors">
                <Icon name="document" size="64" stroke="#3498DB" customClass="group-hover:scale-110 transition-transform duration-300" />
              </div>
              <h3 class="text-xl font-semibold mb-2 text-gray-800 group-hover:text-primary-600 transition-colors">Modern Template</h3>
              <p class="text-gray-600 leading-relaxed">Clean and professional design perfect for corporate roles.</p>
            </div>
            
            <!-- Template Card 2 -->
            <div class="card group">
              <div class="bg-gray-100 h-56 mb-5 rounded-xl flex items-center justify-center overflow-hidden group-hover:bg-primary-50 transition-colors">
                <Icon name="document" size="64" stroke="#3498DB" customClass="group-hover:scale-110 transition-transform duration-300" />
              </div>
              <h3 class="text-xl font-semibold mb-2 text-gray-800 group-hover:text-primary-600 transition-colors">Classic Template</h3>
              <p class="text-gray-600 leading-relaxed">Traditional and formal style ideal for academic or established industries.</p>
            </div>
            
            <!-- Template Card 3 -->
            <div class="card group">
              <div class="bg-gray-100 h-56 mb-5 rounded-xl flex items-center justify-center overflow-hidden group-hover:bg-primary-50 transition-colors">
                <Icon name="document" size="64" stroke="#3498DB" customClass="group-hover:scale-110 transition-transform duration-300" />
              </div>
              <h3 class="text-xl font-semibold mb-2 text-gray-800 group-hover:text-primary-600 transition-colors">Creative Template</h3>
              <p class="text-gray-600 leading-relaxed">Visually engaging design perfect for creative professionals.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Why Choose Us Section -->
      <section id="why-choose-us" class="section bg-gray-50">
        <div class="container mx-auto px-4">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center">Why Choose Our CV Builder</h2>
          <p class="text-gray-600 text-center max-w-3xl mx-auto mb-12">We combine cutting-edge technology with professional design to create the perfect CV</p>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Benefit Card 1 -->
            <div class="card hover:border hover:border-primary-300">
              <div class="flex items-center mb-5">
                <div class="bg-primary-100 p-3 rounded-squircle mr-4">
                  <Icon name="magic" size="28" stroke="#3498DB" fill="#3498DB" customClass="text-primary-500" />
                </div>
                <h3 class="text-xl font-semibold text-gray-800">AI-Powered Writing</h3>
              </div>
              <p class="text-gray-600 leading-relaxed">Our advanced AI helps you craft professional content tailored to your industry and experience.</p>
            </div>
            
            <!-- Benefit Card 2 -->
            <div class="card hover:border hover:border-primary-300">
              <div class="flex items-center mb-5">
                <div class="bg-primary-100 p-3 rounded-squircle mr-4">
                  <Icon name="document" size="28" stroke="#3498DB" customClass="text-primary-500" />
                </div>
                <h3 class="text-xl font-semibold text-gray-800">Professional Templates</h3>
              </div>
              <p class="text-gray-600 leading-relaxed">Choose from a variety of professionally designed templates that are ATS-friendly.</p>
            </div>
            
            <!-- Benefit Card 3 -->
            <div class="card hover:border hover:border-primary-300">
              <div class="flex items-center mb-5">
                <div class="bg-primary-100 p-3 rounded-squircle mr-4">
                  <Icon name="check" size="28" stroke="#3498DB" customClass="text-primary-500" />
                </div>
                <h3 class="text-xl font-semibold text-gray-800">Easy to Use</h3>
              </div>
              <p class="text-gray-600 leading-relaxed">Simple, intuitive interface that makes creating a professional CV quick and effortless.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- FAQ Section -->
      <section id="faq" class="section bg-white">
        <div class="container-narrow mx-auto">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center">Frequently Asked Questions</h2>
          <p class="text-gray-600 text-center max-w-3xl mx-auto mb-12">Everything you need to know about our CV builder</p>
          
          <div class="space-y-4">
            <!-- FAQ Item 1 -->
            <Disclosure as="div" class="border border-gray-200 rounded-lg overflow-hidden" v-for="(faq, index) in faqs" :key="index">
              <template #default="{ open }">
                <div>
                  <DisclosureButton class="w-full flex justify-between items-center px-6 py-4 text-left focus:outline-none focus-visible:ring focus-visible:ring-primary-500 focus-visible:ring-opacity-50 hover:bg-gray-50 transition-colors duration-150">
                    <div class="flex items-center">
                      <div class="bg-primary-100 p-2 rounded-full mr-4">
                        <Icon name="question" size="20" stroke="#3498DB" customClass="text-primary-500" />
                      </div>
                      <span class="text-lg font-semibold text-gray-800">{{ faq.question }}</span>
                    </div>
                    <ChevronDownIcon :class="[
                      open ? 'transform rotate-180' : '',
                      'w-5',
                      'h-5',
                      'text-primary-500',
                      'transition-transform',
                      'duration-200'
                    ]" />
                  </DisclosureButton>
                  <DisclosurePanel class="px-6 pt-2 pb-6 text-gray-600 bg-gray-50 border-t border-gray-200 animate-fadeIn">
                    <div class="pl-12">
                      <p class="leading-relaxed mb-3">{{ faq.answer }}</p>
                      <ul v-if="faq.list" class="list-disc pl-5 space-y-2 text-gray-600">
                        <li v-for="(item, itemIndex) in faq.list" :key="itemIndex" class="leading-relaxed">
                          {{ item }}
                        </li>
                      </ul>
                    </div>
                  </DisclosurePanel>
                </div>
              </template>
            </Disclosure>
          </div>
        </div>
      </section>

      <!-- Reviews Section -->
      <section id="reviews" class="section bg-gray-50">
        <div class="container mx-auto px-4">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4 text-center">What Our Users Say</h2>
          <p class="text-gray-600 text-center max-w-3xl mx-auto mb-12">Hear from people who have successfully used our platform</p>
          
          <div class="relative">
            <div class="flex justify-center mb-6">
              <button @click="prevSlide" class="bg-primary-100 text-primary-600 p-2 rounded-full hover:bg-primary-200 transition-colors mr-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                </svg>
              </button>
              <button @click="nextSlide" class="bg-primary-100 text-primary-600 p-2 rounded-full hover:bg-primary-200 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
            
            <div class="overflow-hidden">
              <div ref="reviewsContainer" class="flex transition-transform duration-500 ease-in-out" :style="{ transform: `translateX(${-currentSlide * 100}%)` }">
                <div v-for="(review, index) in displayedReviews" :key="index" class="w-full sm:w-1/2 md:w-1/3 flex-shrink-0 px-4">
                  <div class="card h-full">
                    <div class="flex justify-between items-center mb-6">
                      <div class="flex items-center">
                        <div class="bg-primary-100 rounded-full w-12 h-12 flex items-center justify-center text-primary-600 font-bold mr-4">{{ review.initials }}</div>
                        <div>
                          <p class="font-semibold text-gray-800">{{ review.name }}</p>
                          <p class="text-sm text-gray-500">{{ review.position }}</p>
                        </div>
                      </div>
                      <div class="flex">
                        <Icon name="star" size="20" fill="#3498DB" stroke="none" customClass="text-primary-500" v-for="star in 5" :key="star" />
                      </div>
                    </div>
                    <p class="text-gray-600 leading-relaxed italic">{{ review.comment }}</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="flex justify-center mt-6">
              <div v-for="(_, index) in reviews" :key="index" 
                   @click="setSlide(index)"
                   class="w-2 h-2 mx-1 rounded-full cursor-pointer transition-all duration-300"
                   :class="index === currentSlide % reviews.length ? 'bg-primary-600 w-6' : 'bg-primary-200'">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Call To Action Section -->
      <section class="section bg-primary-500 text-white">
        <div class="container-narrow mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Create Your Professional CV?</h2>
          <p class="text-xl mb-10 opacity-90 font-light">Join thousands of job seekers who have already transformed their careers</p>
          <router-link to="/service" class="btn bg-white text-primary-600 hover:bg-gray-100 text-lg shadow-md hover:shadow-lg transform hover:-translate-y-1 transition duration-300">
            Get Started Now
          </router-link>
        </div>
      </section>
    </main>

    <!-- Footer Section -->
    <footer class="bg-gray-100 text-gray-600 py-6 text-sm border-t border-gray-200">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
          <div>
            <h3 class="text-gray-800 font-medium mb-2 text-sm">CV Builder</h3>
            <p class="text-gray-500 text-xs leading-relaxed">Creating professional CVs with AI technology.</p>
          </div>
          <div>
            <h4 class="text-gray-800 font-medium mb-2 text-xs">Quick Links</h4>
            <ul class="space-y-1">
              <li><a href="#templates" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
                Templates
              </a></li>
              <li><a href="#faq" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
                FAQ
              </a></li>
              <li><a href="#pricing" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
                Pricing
              </a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-gray-800 font-medium mb-2 text-xs">Support</h4>
            <ul class="space-y-1">
              <li><a href="#" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Contact Us
              </a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Help Center
              </a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-gray-800 font-medium mb-2 text-xs">Legal</h4>
            <ul class="space-y-1">
              <li><a href="#" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
                Privacy
              </a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary-600 transition-colors text-xs flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Terms
              </a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-200 pt-4 flex flex-col sm:flex-row justify-between items-center">
          <p class="mb-2 sm:mb-0 text-gray-500 text-xs"> 2025 CV Builder. All rights reserved.</p>
          <div class="flex space-x-4">
            <a href="#" class="text-gray-400 hover:text-primary-600 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">
                <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
              </svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-primary-600 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-twitter-x" viewBox="0 0 16 16">
                <path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865z"/>
              </svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-primary-600 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z"/>
              </svg>
            </a>
            <a href="#" class="text-gray-400 hover:text-primary-600 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
                <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92s.546-.453.92-.598c.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
import Icon from '../components/Icon.vue'
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';

const IconName = ref('question');

const ChevronDownIcon = {
  template: `<svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 20 20"
      fill="currentColor"
      class="w-5 h-5"
    >
      <path
        fillRule="evenodd"
        d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
        clipRule="evenodd"
      />
    </svg>
  `
 };

const faqs = ref([
  {
    question: 'How does the AI CV Generator work?',
    answer: 'Our AI analyzes your input and generates professional content tailored to your experience and industry standards. The process includes:',
    list: [
      'Analyzing your provided information and work history',
      'Creating ATS-optimized content for your field',
      'Formatting your CV using professional templates',
      'Providing suggestions to improve your career narrative'
    ]
  },
  {
    question: 'Is my data secure?',
    answer: 'Yes, we use encryption to protect your personal information and do not share your data with third parties. Our security measures include:',
    list: [
      'End-to-end encryption for all user data',
      'Regular security audits and penetration testing',
      'Compliance with GDPR and other privacy regulations',
      'Automatic data purging after service completion'
    ]
  },
  {
    question: 'How much does it cost?',
    answer: 'We offer both free and premium plans. The premium plan includes additional templates and advanced AI features.',
    list: [
      'Free: Basic CV generation with limited templates',
      'Premium: $9.99 for full access to all templates and AI features',
      'Enterprise: Custom pricing for team and corporate solutions',
      'All plans include PDF download capability'
    ]
  },
  {
    question: 'Can I download my CV as a PDF?',
    answer: 'Yes, you can download your completed CV in PDF format, ready to send to employers. Our PDF exports feature:',
    list: [
      'High-quality, print-ready documents',
      'ATS-friendly formatting to pass application systems',
      'Multiple download options including email delivery',
      'Mobile-compatible downloads for on-the-go job applications'
    ]
  }
]);

const reviews = ref([
  {
    initials: 'JD',
    name: 'John Doe',
    position: 'Software Developer',
    comment: 'This CV builder helped me land interviews at top companies! The AI suggestions were spot-on for my industry.'
  },
  {
    initials: 'JS',
    name: 'Jane Smith',
    position: 'Marketing Manager',
    comment: 'I was struggling with my CV for weeks. This tool helped me create a professional CV in just 30 minutes!'
  },
  {
    initials: 'RJ',
    name: 'Robert Johnson',
    position: 'Financial Analyst',
    comment: 'The templates are modern and professional. I received compliments on my CV design from multiple recruiters.'
  }
]);

const currentSlide = ref(0);
const reviewsContainer = ref(null);
const autoplayInterval = ref(null);

// Create an extended reviews array for the infinite loop effect
const displayedReviews = computed(() => {
  // Clone the original reviews and add duplicates at the beginning and end
  // This creates the illusion of an infinite loop
  return [...reviews.value, ...reviews.value, ...reviews.value];
});

function prevSlide() {
  if (currentSlide.value <= 0) {
    // Jump to the end of the middle set (for seamless looping)
    currentSlide.value = reviews.value.length;
    // Force immediate repositioning without animation
    setTimeout(() => {
      if (reviewsContainer.value) {
        reviewsContainer.value.style.transition = 'none';
        currentSlide.value--;
        setTimeout(() => {
          if (reviewsContainer.value) {
            reviewsContainer.value.style.transition = 'transform 500ms ease-in-out';
          }
        }, 50);
      }
    }, 0);
  } else {
    currentSlide.value--;
  }
  resetAutoplayTimer();
}

function nextSlide() {
  if (currentSlide.value >= reviews.value.length * 2 - 1) {
    // Jump to the beginning of the middle set (for seamless looping)
    currentSlide.value = reviews.value.length - 1;
    // Force immediate repositioning without animation
    setTimeout(() => {
      if (reviewsContainer.value) {
        reviewsContainer.value.style.transition = 'none';
        currentSlide.value++;
        setTimeout(() => {
          if (reviewsContainer.value) {
            reviewsContainer.value.style.transition = 'transform 500ms ease-in-out';
          }
        }, 50);
      }
    }, 0);
  } else {
    currentSlide.value++;
  }
  resetAutoplayTimer();
}

function setSlide(index) {
  // Adjust index to the middle set (to maintain infinite loop capability)
  currentSlide.value = index + reviews.value.length;
  resetAutoplayTimer();
}

function startAutoplay() {
  autoplayInterval.value = setInterval(() => {
    nextSlide();
  }, 5000);
}

function resetAutoplayTimer() {
  if (autoplayInterval.value) {
    clearInterval(autoplayInterval.value);
    startAutoplay();
  }
}

onMounted(() => {
  // Start from the middle set of slides (for infinite looping)
  currentSlide.value = reviews.value.length;
  // Start autoplay
  startAutoplay();
});

onBeforeUnmount(() => {
  if (autoplayInterval.value) {
    clearInterval(autoplayInterval.value);
  }
});
</script>

<style>
/* Add animation for FAQ accordion */
.animate-fadeIn {
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>