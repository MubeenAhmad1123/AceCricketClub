<template>
  <section class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">Start Your Cricket Journey</h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Ready to take your cricket to the next level? Get in touch with us today.
        </p>
      </div>

      <div v-if="!showSuccess" class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Form Section -->
        <div class="lg:col-span-2">
          <form @submit.prevent="handleSubmit" class="bg-white rounded-2xl shadow-xl p-8" novalidate>
            <div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg text-sm text-blue-800">
              <strong>Note:</strong> Fill out the form below and we'll receive your enrollment request via email.
            </div>

            <div v-if="draftRestored" class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg text-sm text-blue-800 flex justify-between items-center">
              <span>Draft restored from previous session</span>
              <button type="button" @click="clearDraft" class="text-blue-600 hover:text-blue-800 underline">Clear draft</button>
            </div>

            <div aria-live="polite" class="sr-only">{{ validationSummary }}</div>

            <!-- Full Name -->
            <div class="mb-6">
              <label for="fullName" class="block text-sm font-semibold text-gray-700 mb-2">
                Full Name <span class="text-red-600">*</span>
              </label>
              <input
                id="fullName"
                v-model="form.fullName"
                type="text"
                required
              
                :aria-invalid="errors.fullName ? 'true' : 'false'"
                :aria-describedby="errors.fullName ? 'fullName-error' : undefined"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
                @blur="validateField('fullName')"
              />
              <p v-if="errors.fullName" id="fullName-error" class="mt-2 text-sm text-red-600">{{ errors.fullName }}</p>
            </div>

            <!-- Age -->
            <div class="mb-6">
              <label for="age" class="block text-sm font-semibold text-gray-700 mb-2">
                Age <span class="text-red-600">*</span>
              </label>
              <input
                id="age"
                v-model.number="form.age"
                type="number"
                min="6"
                max="99"
                required
                :aria-invalid="errors.age ? 'true' : 'false'"
                :aria-describedby="errors.age ? 'age-error' : undefined"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
                @blur="validateField('age')"
              />
              <p v-if="errors.age" id="age-error" class="mt-2 text-sm text-red-600">{{ errors.age }}</p>
            </div>

            <!-- Email -->
            <div class="mb-6">
              <label for="email" class="block text-sm font-semibold text-gray-700 mb-2">
                Email Address <span class="text-red-600">*</span>
              </label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                :aria-invalid="errors.email ? 'true' : 'false'"
                :aria-describedby="errors.email ? 'email-error email-help' : 'email-help'"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
                @blur="validateField('email')"
              />
              <p id="email-help" class="mt-1 text-xs text-gray-500">We'll use this to send you important updates</p>
              <p v-if="errors.email" id="email-error" class="mt-2 text-sm text-red-600">{{ errors.email }}</p>
            </div>

            <!-- Phone -->
            <div class="mb-6">
              <label for="phone" class="block text-sm font-semibold text-gray-700 mb-2">
                Phone Number <span class="text-red-600">*</span>
              </label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                placeholder="+92 XXXXX XXXXX"
                required
                :aria-invalid="errors.phone ? 'true' : 'false'"
                :aria-describedby="errors.phone ? 'phone-error phone-help' : 'phone-help'"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
                @blur="validateField('phone')"
              />
              <p id="phone-help" class="mt-1 text-xs text-gray-500">Include country code (e.g., +92)</p>
              <p v-if="errors.phone" id="phone-error" class="mt-2 text-sm text-red-600">{{ errors.phone }}</p>
            </div>

            <!-- Skill Level -->
            <div class="mb-6">
              <label for="skillLevel" class="block text-sm font-semibold text-gray-700 mb-2">
                Current Skill Level <span class="text-red-600">*</span>
              </label>
              <select
                id="skillLevel"
                v-model="form.skillLevel"
                required
                :aria-invalid="errors.skillLevel ? 'true' : 'false'"
                :aria-describedby="errors.skillLevel ? 'skillLevel-error' : undefined"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors bg-white"
                @blur="validateField('skillLevel')"
              >
                <option value="">Select your level</option>
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
              </select>
              <p v-if="errors.skillLevel" id="skillLevel-error" class="mt-2 text-sm text-red-600">{{ errors.skillLevel }}</p>
            </div>

            <!-- Preferred Program -->
            <div class="mb-6">
              <label for="program" class="block text-sm font-semibold text-gray-700 mb-2">
                Preferred Program <span class="text-red-600">*</span>
              </label>
              <select
                id="program"
                v-model="form.program"
                required
                :aria-invalid="errors.program ? 'true' : 'false'"
                :aria-describedby="errors.program ? 'program-error' : undefined"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors bg-white"
                @blur="validateField('program')"
              >
                <option value="">Select a program</option>
                <option value="Junior Development — Age 6-12 — $99/month">Junior Development — Age 6-12 — $99/month</option>
                <option value="Intermediate Training — Age 13-17 — $149/month">Intermediate Training — Age 13-17 — $149/month</option>
                <option value="Elite Performance — Age 16+ — $249/month">Elite Performance — Age 16+ — $249/month</option>
                <option value="Weekend Warrior — All Ages — $79/month">Weekend Warrior — All Ages — $79/month</option>
              </select>
              <p v-if="errors.program" id="program-error" class="mt-2 text-sm text-red-600">{{ errors.program }}</p>
            </div>

            <!-- Start Date -->
            <div class="mb-6">
              <label for="startDate" class="block text-sm font-semibold text-gray-700 mb-2">
                Preferred Start Date <span class="text-gray-500 text-xs">(Optional)</span>
              </label>
              <input
                id="startDate"
                v-model="form.startDate"
                type="date"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
              />
            </div>

            <!-- Message -->
            <div class="mb-6">
              <label for="message" class="block text-sm font-semibold text-gray-700 mb-2">
                Message <span class="text-gray-500 text-xs">(Optional)</span>
              </label>
              <textarea
                id="message"
                v-model="form.message"
                rows="4"
                minlength="20"
                maxlength="800"
                :aria-invalid="errors.message ? 'true' : 'false'"
                :aria-describedby="errors.message ? 'message-error message-counter' : 'message-counter'"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors resize-none"
                @blur="validateField('message')"
              ></textarea>
              <div class="flex justify-between items-center mt-1">
                <p v-if="errors.message" id="message-error" class="text-sm text-red-600">{{ errors.message }}</p>
                <p id="message-counter" class="text-xs text-gray-500 ml-auto">{{ messageLength }}/800 characters</p>
              </div>
            </div>

            <!-- Newsletter -->
            <div class="mb-6">
              <label class="flex items-start">
                <input
                  v-model="form.newsletter"
                  type="checkbox"
                  class="mt-1 w-4 h-4 text-red-600 border-gray-300 rounded focus:ring-2 focus:ring-red-500"
                />
                <span class="ml-3 text-sm text-gray-700">
                  Subscribe to our newsletter for cricket tips, events, and exclusive offers
                </span>
              </label>
            </div>

            <!-- Math Captcha -->
            <div class="mb-6">
              <label for="mathCaptcha" class="block text-sm font-semibold text-gray-700 mb-2">
                Security Check: What is {{ mathQuestion.a }} + {{ mathQuestion.b }}? <span class="text-red-600">*</span>
              </label>
              <input
                id="mathCaptcha"
                v-model.number="form.mathAnswer"
                type="number"
                required
                :aria-invalid="errors.mathAnswer ? 'true' : 'false'"
                :aria-describedby="errors.mathAnswer ? 'mathAnswer-error' : undefined"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors"
                @blur="validateField('mathAnswer')"
              />
              <p v-if="errors.mathAnswer" id="mathAnswer-error" class="mt-2 text-sm text-red-600">{{ errors.mathAnswer }}</p>
            </div>

            <!-- Consent -->
            <div class="mb-6">
              <label class="flex items-start">
                <input
                  v-model="form.consent"
                  type="checkbox"
                  required
                  :aria-invalid="errors.consent ? 'true' : 'false'"
                  :aria-describedby="errors.consent ? 'consent-error' : undefined"
                  class="mt-1 w-4 h-4 text-red-600 border-gray-300 rounded focus:ring-2 focus:ring-red-500"
                />
                <span class="ml-3 text-sm text-gray-700">
                  I agree to the club's <a href="#" class="text-red-600 hover:text-red-700 underline">privacy policy</a> and to be contacted regarding my inquiry. <span class="text-red-600">*</span>
                </span>
              </label>
              <p v-if="errors.consent" id="consent-error" class="mt-2 text-sm text-red-600">{{ errors.consent }}</p>
            </div>

            <!-- Honeypot -->
            <div class="hidden" aria-hidden="true">
              <label for="website">Website</label>
              <input id="website" v-model="form.website" type="text" tabindex="-1" autocomplete="off" />
            </div>

            <!-- Global Error -->
            <div v-if="globalError" class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-sm text-red-800" role="alert">
              <strong>Error:</strong> {{ globalError }}
              <button v-if="showRetry" @click="handleSubmit" type="button" class="ml-4 underline hover:no-underline">
                Retry
              </button>
            </div>

            <!-- Submit Buttons -->
            <div class="flex flex-col sm:flex-row gap-4">
              <button
                type="submit"
                :disabled="isSubmitting"
                class="flex-1 bg-red-600 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-red-700 focus:ring-4 focus:ring-red-300 transition-all duration-300 shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="!isSubmitting">Submit Enrollment Request</span>
                <span v-else class="flex items-center justify-center">
                  <svg class="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Submitting...
                </span>
              </button>
              <a
                href="https://calendly.com/mubeenahma1123/30min"
                target="_blank"
                rel="noopener noreferrer"
                class="flex-1 bg-white text-red-600 border-2 border-red-600 px-8 py-4 rounded-lg font-bold text-lg hover:bg-red-50 focus:ring-4 focus:ring-red-300 transition-all duration-300 text-center inline-block"
              >
                Schedule Free Call
              </a>
            </div>
          </form>
        </div>

        <!-- Contact Details Sidebar -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-2xl shadow-xl p-8 sticky top-8">
            <h3 class="text-2xl font-bold text-gray-900 mb-6">Get In Touch</h3>
            
            <div class="space-y-6">
              <!-- Phone -->
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                  </svg>
                </div>
                <div class="ml-4">
                  <p class="text-sm font-semibold text-gray-900">Phone</p>
                  <a href="tel:+923218492868" class="text-sm text-gray-600 hover:text-red-600">+92 3218492868</a><br>
                  <a href="tel:+913029821121" class="text-sm text-gray-600 hover:text-red-600">+92 3029821121</a>
                </div>
              </div>

              <!-- Email -->
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <div class="ml-4">
                  <p class="text-sm font-semibold text-gray-900">Email</p>
                  <a href="mailto:info@AceCriketclub.com" class="text-sm text-gray-600 hover:text-red-600">info@AceCriketclub.com</a><br>
                  <a href="mailto:MubeenAhma1123@gmail.com" class="text-sm text-gray-600 hover:text-red-600">MubeenAhma1123@gmail.com</a>
                </div>
              </div>

              <!-- Location -->
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                  </svg>
                </div>
                <div class="ml-4">
                  <p class="text-sm font-semibold text-gray-900">Location</p>
                  <p class="text-sm text-gray-600">123 Cricket Ground Road<br>Sports Complex<br>Faisalabad, Punjab,
Pakistan</p>
                </div>
              </div>

              <!-- Hours -->
              <div class="flex items-start">
                <div class="flex-shrink-0">
                  <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                </div>
                <div class="ml-4">
                  <p class="text-sm font-semibold text-gray-900">Hours</p>
                  <p class="text-sm text-gray-600">Mon-Fri: 6:00 AM - 8:00 PM<br>Sat-Sun: 7:00 AM - 6:00 PM</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Success Panel -->
      <div v-else class="max-w-3xl mx-auto">
        <div class="bg-white rounded-2xl shadow-xl p-12 text-center">
          <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
          </div>
          
          <h3 class="text-3xl font-bold text-gray-900 mb-4">Thank You, {{ successData.name }}!</h3>
          <p class="text-xl text-gray-600 mb-6">
            Your enrollment request for <strong>{{ successData.program }}</strong> has been received.
          </p>
          <p class="text-gray-600 mb-8">
            Your enrollment details have been saved. Check your email client or click the button below to send the email manually.
          </p>

          <div class="mb-8 p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <p class="text-sm text-blue-800 mb-4"><strong>Email not sent?</strong> Copy the details below and email them to MubeenAhma1123@gmail.com</p>
            <div class="bg-white p-4 rounded border border-blue-300 text-left text-sm font-mono mb-4 max-h-64 overflow-y-auto">
              <strong>Name:</strong> {{ form.fullName }}<br>
              <strong>Age:</strong> {{ form.age }}<br>
              <strong>Email:</strong> {{ form.email }}<br>
              <strong>Phone:</strong> {{ form.phone }}<br>
              <strong>Skill Level:</strong> {{ form.skillLevel }}<br>
              <strong>Program:</strong> {{ form.program }}<br>
              <strong>Start Date:</strong> {{ form.startDate || 'Not specified' }}<br>
              <strong>Message:</strong> {{ form.message || 'None' }}<br>
              <strong>Newsletter:</strong> {{ form.newsletter ? 'Yes' : 'No' }}
            </div>
            <div class="flex gap-2">
              <a
                :href="mailtoLink"
                target="_blank"
                class="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
              >
                Try Email Again
              </a>
              <button
                @click="copyToClipboard"
                class="inline-block bg-gray-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-gray-700 transition-colors"
              >
                {{ copied ? 'Copied!' : 'Copy Details' }}
              </button>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              @click="backToForm"
              class="bg-gray-200 text-gray-800 px-8 py-3 rounded-lg font-semibold hover:bg-gray-300 transition-colors"
            >
              Submit Another
            </button>
            <a
              href="tel:+923218492868"
              class="bg-green-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors inline-block"
            >
              📞 Call Us Now
            </a>
          </div>

          <div class="mt-8 p-4 bg-yellow-50 border border-yellow-200 rounded-lg text-sm">
            <p class="text-yellow-800">
              <strong>Alternative:</strong> You can also WhatsApp us at <a href="https://wa.me/923218492868" class="underline font-semibold">+92 3218492868</a> or call directly.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted } from 'vue';

/**
 * SETUP INSTRUCTIONS FOR EMAIL DELIVERY:
 * 
 * Option 1 (RECOMMENDED): Use Formspree (Free & Easy)
 * 1. Go to https://formspree.io
 * 2. Sign up for free account
 * 3. Create a new form
 * 4. Copy your form ID (looks like: xyzabc123)
 * 5. Replace 'YOUR_FORM_ID' in line 52 with your actual form ID
 * 6. Set email to: MubeenAhma1123@gmail.com in Formspree dashboard
 * 
 * Option 2: Use Web3Forms (Alternative free service)
 * 1. Go to https://web3forms.com
 * 2. Enter your email: MubeenAhma1123@gmail.com
 * 3. Get your access key
 * 4. Replace the fetch URL with Web3Forms endpoint
 * 
 * Option 3: mailto fallback (Already configured)
 * - Works but depends on user having email client configured
 * - Users can copy details and email manually
 */

const emit = defineEmits(['submitted', 'save-draft', 'schedule-trial']);

// Form state
const form = reactive({
  fullName: '',
  age: null,
  email: '',
  phone: '',
  skillLevel: '',
  program: '',
  startDate: '',
  message: '',
  newsletter: false,
  consent: false,
  mathAnswer: null,
  website: '' // honeypot
});

// Validation state
const errors = reactive({
  fullName: '',
  age: '',
  email: '',
  phone: '',
  skillLevel: '',
  program: '',
  message: '',
  mathAnswer: '',
  consent: ''
});

// UI state
const isSubmitting = ref(false);
const showSuccess = ref(false);
const globalError = ref('');
const showRetry = ref(false);
const draftRestored = ref(false);
const copied = ref(false);

// Math captcha
const mathQuestion = reactive({
  a: Math.floor(Math.random() * 10) + 1,
  b: Math.floor(Math.random() * 10) + 1
});

// Success data
const successData = reactive({
  name: '',
  program: ''
});

// Computed
const messageLength = computed(() => form.message.length);

const validationSummary = computed(() => {
  const errorCount = Object.values(errors).filter(e => e).length;
  return errorCount > 0 ? `${errorCount} validation error${errorCount > 1 ? 's' : ''} found` : '';
});

const mailtoLink = computed(() => {
  const subject = encodeURIComponent('Cricket Club Enrollment Request');
  const body = encodeURIComponent(`
Name: ${form.fullName}
Age: ${form.age}
Email: ${form.email}
Phone: ${form.phone}
Skill Level: ${form.skillLevel}
Program: ${form.program}
Start Date: ${form.startDate || 'Not specified'}
Message: ${form.message || 'None'}
Newsletter: ${form.newsletter ? 'Yes' : 'No'}
  `);
  return `mailto:MubeenAhma1123@gmail.com?subject=${subject}&body=${body}`;
});

// Validation functions
const validateField = (fieldName) => {
  errors[fieldName] = '';

  switch (fieldName) {
    case 'fullName':
      if (!form.fullName.trim()) {
        errors.fullName = 'Full name is required';
      }
      break;

    case 'age':
      if (!form.age) {
        errors.age = 'Age is required';
      } else if (form.age < 6 || form.age > 99) {
        errors.age = 'Age must be between 6 and 99';
      }
      break;

    case 'email':
      if (!form.email.trim()) {
        errors.email = 'Email is required';
      } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
        errors.email = 'Please enter a valid email address';
      }
      break;

    case 'phone':
      const digits = form.phone.replace(/\D/g, '');
      if (!form.phone.trim()) {
        errors.phone = 'Phone number is required';
      } else if (digits.length < 10) {
        errors.phone = 'Phone number must have at least 10 digits';
      }
      break;

    case 'skillLevel':
      if (!form.skillLevel) {
        errors.skillLevel = 'Please select your skill level';
      }
      break;

    case 'program':
      if (!form.program) {
        errors.program = 'Please select a program';
      }
      break;

    case 'message':
      if (form.message && (form.message.length < 20 || form.message.length > 800)) {
        errors.message = 'Message must be between 20 and 800 characters';
      }
      break;

    case 'mathAnswer':
      if (form.mathAnswer !== (mathQuestion.a + mathQuestion.b)) {
        errors.mathAnswer = 'Incorrect answer. Please try again.';
      }
      break;

    case 'consent':
      if (!form.consent) {
        errors.consent = 'You must agree to the privacy policy';
      }
      break;
  }
};

const validateForm = () => {
  // Check honeypot
  if (form.website) {
    return false;
  }

  // Validate all fields
  validateField('fullName');
  validateField('age');
  validateField('email');
  validateField('phone');
  validateField('skillLevel');
  validateField('program');
  if (form.message) validateField('message');
  validateField('mathAnswer');
  validateField('consent');

  // Check if any errors exist
  const hasErrors = Object.values(errors).some(error => error);
  
  if (hasErrors) {
    // Focus first invalid field
    const firstErrorField = Object.keys(errors).find(key => errors[key]);
    if (firstErrorField) {
      const element = document.getElementById(firstErrorField);
      if (element) element.focus();
    }
  }

  return !hasErrors;
};

// Submit handler
const handleSubmit = async () => {
  globalError.value = '';
  showRetry.value = false;

  if (!validateForm()) {
    return;
  }

  isSubmitting.value = true;

  try {
    const submissionData = {
      fullName: form.fullName,
      age: form.age,
      email: form.email,
      phone: form.phone,
      skillLevel: form.skillLevel,
      program: form.program,
      startDate: form.startDate,
      message: form.message,
      newsletter: form.newsletter,
      consent: form.consent,
      timestamp: new Date().toISOString()
    };

    // Save to localStorage for backup
    const submissions = JSON.parse(localStorage.getItem('ace_submissions') || '[]');
    submissions.push(submissionData);
    localStorage.setItem('ace_submissions', JSON.stringify(submissions));

    // Try to submit via Formspree (free service)
    // You need to create a free account at https://formspree.io and replace 'YOUR_FORM_ID'
    // Or use the mailto fallback below
    
    try {
      // Option 1: Try Formspree (recommended)
      const response = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: form.fullName,
          age: form.age,
          email: form.email,
          phone: form.phone,
          skillLevel: form.skillLevel,
          program: form.program,
          startDate: form.startDate,
          message: form.message,
          newsletter: form.newsletter,
          _replyto: form.email,
          _subject: 'Cricket Club Enrollment Request'
        })
      });

      if (!response.ok) {
        throw new Error('Formspree not configured');
      }
    } catch (fetchError) {
      // Option 2: Fallback to mailto with better handling
      console.log('Using mailto fallback');
      
      // Create a more reliable mailto link
      const emailBody = `
Cricket Club Enrollment Request
================================

Name: ${form.fullName}
Age: ${form.age}
Email: ${form.email}
Phone: ${form.phone}
Skill Level: ${form.skillLevel}
Program: ${form.program}
Start Date: ${form.startDate || 'Not specified'}
Message: ${form.message || 'None'}
Newsletter: ${form.newsletter ? 'Yes' : 'No'}

Submitted: ${new Date().toLocaleString()}
      `;

      // Try to open mailto
      const mailtoUrl = `mailto:MubeenAhma1123@gmail.com?subject=${encodeURIComponent('Cricket Club Enrollment Request')}&body=${encodeURIComponent(emailBody)}`;
      
      // Create temporary link and click it
      const link = document.createElement('a');
      link.href = mailtoUrl;
      link.target = '_blank';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
      // Small delay to allow mailto to trigger
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    // Success
    successData.name = form.fullName;
    successData.program = form.program;
    showSuccess.value = true;

    // Clear draft
    localStorage.removeItem('ace_form_draft');

    // Emit event
    emit('submitted', submissionData);

  } catch (error) {
    globalError.value = error.message || 'Failed to process form. Please try again.';
    showRetry.value = true;
    console.error('Form submission error:', error);
  } finally {
    isSubmitting.value = false;
  }
};

// Back to form
const backToForm = () => {
  showSuccess.value = false;
  resetForm();
};

// Reset form
const resetForm = () => {
  form.fullName = '';
  form.age = null;
  form.email = '';
  form.phone = '';
  form.skillLevel = '';
  form.program = '';
  form.startDate = '';
  form.message = '';
  form.newsletter = false;
  form.consent = false;
  form.mathAnswer = null;
  form.website = '';

  // Reset errors
  Object.keys(errors).forEach(key => {
    errors[key] = '';
  });

  // Generate new math question
  mathQuestion.a = Math.floor(Math.random() * 10) + 1;
  mathQuestion.b = Math.floor(Math.random() * 10) + 1;
};

// Schedule trial
const scheduleTrial = () => {
  emit('schedule-trial');
  // You can add custom scheduling logic here or open a calendar booking link
  // Example: window.open('https://calendly.com/your-link', '_blank');
};

// Draft management
const saveDraft = () => {
  const draft = {
    fullName: form.fullName,
    age: form.age,
    email: form.email,
    phone: form.phone,
    skillLevel: form.skillLevel,
    program: form.program,
    startDate: form.startDate,
    message: form.message,
    newsletter: form.newsletter
  };
  localStorage.setItem('ace_form_draft', JSON.stringify(draft));
  emit('save-draft', draft);
};

const restoreDraft = () => {
  const draft = localStorage.getItem('ace_form_draft');
  if (draft) {
    try {
      const parsed = JSON.parse(draft);
      form.fullName = parsed.fullName || '';
      form.age = parsed.age || null;
      form.email = parsed.email || '';
      form.phone = parsed.phone || '';
      form.skillLevel = parsed.skillLevel || '';
      form.program = parsed.program || '';
      form.startDate = parsed.startDate || '';
      form.message = parsed.message || '';
      form.newsletter = parsed.newsletter || false;
      draftRestored.value = true;
    } catch (e) {
      console.error('Failed to restore draft:', e);
    }
  }
};

const clearDraft = () => {
  localStorage.removeItem('ace_form_draft');
  draftRestored.value = false;
  resetForm();
};

// Copy to clipboard function
const copyToClipboard = async () => {
  const text = `
Cricket Club Enrollment Request

Name: ${form.fullName}
Age: ${form.age}
Email: ${form.email}
Phone: ${form.phone}
Skill Level: ${form.skillLevel}
Program: ${form.program}
Start Date: ${form.startDate || 'Not specified'}
Message: ${form.message || 'None'}
Newsletter: ${form.newsletter ? 'Yes' : 'No'}
  `;

  try {
    await navigator.clipboard.writeText(text);
    copied.value = true;
    setTimeout(() => {
      copied.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy:', err);
    // Fallback for older browsers
    const textArea = document.createElement('textarea');
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    copied.value = true;
    setTimeout(() => {
      copied.value = false;
    }, 2000);
  }
};

// Watch form changes and save draft
watch(
  () => ({ ...form }),
  () => {
    // Debounce save - only save if user has started filling the form
    if (form.fullName || form.email || form.phone) {
      saveDraft();
    }
  },
  { deep: true }
);

// Lifecycle
onMounted(() => {
  restoreDraft();
});
</script>

<style scoped>
/* Fallback styles for non-Tailwind environments */
@supports not (display: grid) {
  .grid {
    display: block;
  }
}

/* Smooth transitions */
* {
  transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

/* Reduce motion for accessibility */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Focus styles for accessibility */
input:focus,
select:focus,
textarea:focus,
button:focus {
  outline: 2px solid #ef4444;
  outline-offset: 2px;
}

/* Hidden honeypot */
.hidden {
  position: absolute;
  left: -9999px;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

/* Screen reader only */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Animations */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>