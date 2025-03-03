<template>
  <div class="min-h-screen flex flex-col">
    <!-- Header Section -->
    <header class="bg-white border-b border-gray-200 py-4 sticky top-0 z-50 shadow-soft">
      <div class="container mx-auto px-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-primary-600">CV Builder</h1>
        <nav>
          <ul class="flex space-x-6">
            <li><a href="#templates" class="text-gray-600 hover:text-primary-500 transition-colors font-medium">Templates</a></li>
            <li><a href="#why-choose-us" class="text-gray-600 hover:text-primary-500 transition-colors font-medium">Why Choose Us</a></li>
            <li><a href="#faq" class="text-gray-600 hover:text-primary-500 transition-colors font-medium">FAQ</a></li>
            <li><a href="#reviews" class="text-gray-600 hover:text-primary-500 transition-colors font-medium">Reviews</a></li>
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
                  <DisclosurePanel class="px-6 pt-0 pb-4 text-gray-600 bg-gray-50 border-t border-gray-200 animate-fadeIn">
                    <div class="pl-12">
                      <p class="leading-relaxed">{{ faq.answer }}</p>
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
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Review Card 1 -->
            <div class="card">
              <div class="flex justify-between items-center mb-6">
                <div class="flex items-center">
                  <div class="bg-primary-100 rounded-full w-12 h-12 flex items-center justify-center text-primary-600 font-bold mr-4">JD</div>
                  <div>
                    <p class="font-semibold text-gray-800">John Doe</p>
                    <p class="text-sm text-gray-500">Software Developer</p>
                  </div>
                </div>
                <Icon name="star" size="20" fill="#3498DB" stroke="none" customClass="text-primary-500" />
              </div>
              <p class="text-gray-600 leading-relaxed italic">"This CV builder helped me land interviews at top companies! The AI suggestions were spot-on for my industry."</p>
            </div>
            
            <!-- Review Card 2 -->
            <div class="card">
              <div class="flex justify-between items-center mb-6">
                <div class="flex items-center">
                  <div class="bg-primary-100 rounded-full w-12 h-12 flex items-center justify-center text-primary-600 font-bold mr-4">JS</div>
                  <div>
                    <p class="font-semibold text-gray-800">Jane Smith</p>
                    <p class="text-sm text-gray-500">Marketing Manager</p>
                  </div>
                </div>
                <Icon name="star" size="20" fill="#3498DB" stroke="none" customClass="text-primary-500" />
              </div>
              <p class="text-gray-600 leading-relaxed italic">"I was struggling with my CV for weeks. This tool helped me create a professional CV in just 30 minutes!"</p>
            </div>
            
            <!-- Review Card 3 -->
            <div class="card">
              <div class="flex justify-between items-center mb-6">
                <div class="flex items-center">
                  <div class="bg-primary-100 rounded-full w-12 h-12 flex items-center justify-center text-primary-600 font-bold mr-4">RJ</div>
                  <div>
                    <p class="font-semibold text-gray-800">Robert Johnson</p>
                    <p class="text-sm text-gray-500">Financial Analyst</p>
                  </div>
                </div>
                <Icon name="star" size="20" fill="#3498DB" stroke="none" customClass="text-primary-500" />
              </div>
              <p class="text-gray-600 leading-relaxed italic">"The templates are modern and professional. I received compliments on my CV design from multiple recruiters."</p>
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
    <footer class="bg-gray-800 text-white py-12">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div>
            <h3 class="text-xl font-bold mb-4">CV Builder</h3>
            <p class="text-gray-400 leading-relaxed">Creating professional CVs with AI technology to help you land your dream job.</p>
          </div>
          <div>
            <h4 class="text-lg font-medium mb-4">Quick Links</h4>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Templates</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Pricing</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Resources</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-lg font-medium mb-4">Support</h4>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Help Center</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Contact Us</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">FAQ</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-lg font-medium mb-4">Legal</h4>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Privacy Policy</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Terms of Service</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Cookie Policy</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-700 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p class="mb-4 md:mb-0 text-gray-400"> 2025 CV Builder. All rights reserved.</p>
          <div class="flex space-x-6">
            <a href="#" class="text-gray-400 hover:text-white transition-colors">Facebook</a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors">Twitter</a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors">LinkedIn</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
import Icon from '../components/Icon.vue'
import { ref } from 'vue';

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
    answer: 'Our AI analyzes your input and generates professional content tailored to your experience and industry standards.'
  },
  {
    question: 'Is my data secure?',
    answer: 'Yes, we use encryption to protect your personal information and do not share your data with third parties.'
  },
  {
    question: 'How much does it cost?',
    answer: 'We offer both free and premium plans. The premium plan includes additional templates and advanced AI features.'
  },
  {
    question: 'Can I download my CV as a PDF?',
    answer: 'Yes, you can download your completed CV in PDF format, ready to send to employers.'
  }
]);
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