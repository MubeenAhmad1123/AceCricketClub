<template>
  <section class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <!-- Header Section -->
      <div class="text-center mb-16">
        <h2 class="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
          Our Programs
        </h2>
        <p class="text-xl sm:text-2xl text-red-600 font-semibold mb-4">
          Choose Your Training Path
        </p>
        <p class="text-gray-600 max-w-2xl mx-auto text-lg">
          Whether you're just starting out or aiming for professional cricket, 
          we have the perfect program to help you achieve your goals and develop your skills.
        </p>
      </div>

      <!-- Programs Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
        <div
          v-for="program in programs"
          :key="program.id"
          @click="selectProgram(program.id)"
          :class="[
            'relative bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden cursor-pointer',
            activeProgram === program.id ? 'ring-4 ring-red-600' : ''
          ]"
        >
          <!-- Popular/Active Badge -->
          <div
            v-if="activeProgram === program.id"
            class="absolute top-0 right-0 bg-red-600 text-white px-4 py-2 rounded-bl-2xl font-semibold text-sm"
          >
            {{ program.popular ? 'Most Popular' : 'Selected' }}
          </div>

          <!-- Card Content -->
          <div class="p-6">
            <!-- Icon/Image -->
            <div
              :class="[
                'w-20 h-20 aspect-square rounded-full flex items-center justify-center mb-4 overflow-hidden transition-colors duration-300',
                activeProgram === program.id ? 'bg-red-100' : 'bg-gray-100'
              ]"
            >
              <img
                :src="program.image"
                :alt="program.title"
                class="w-20 h-20 object-contain aspect-square"
              />
            </div>

            <!-- Title -->
            <h3 class="text-2xl font-bold text-gray-900 mb-2">
              {{ program.title }}
            </h3>

            <!-- Age & Level -->
            <div class="flex gap-2 mb-4">
              <span class="text-sm bg-gray-100 text-gray-700 px-3 py-1 rounded-full">
                {{ program.age }}
              </span>
              <span
                :class="[
                  'text-sm px-3 py-1 rounded-full transition-colors duration-300',
                  activeProgram === program.id
                    ? 'bg-red-100 text-red-700' 
                    : 'bg-gray-100 text-gray-700'
                ]"
              >
                {{ program.level }}
              </span>
            </div>

            <!-- Price -->
            <div class="mb-6">
              <span class="text-4xl font-bold text-gray-900">
                {{ program.price }}
              </span>
              <span class="text-gray-600 text-lg">/month</span>
            </div>

            <!-- Features -->
            <ul class="space-y-3 mb-6">
              <li
                v-for="(feature, index) in program.features"
                :key="index"
                class="flex items-start gap-2"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  :class="[
                    'w-5 h-5 flex-shrink-0 mt-0.5 transition-colors duration-300',
                    activeProgram === program.id ? 'text-red-600' : 'text-gray-400'
                  ]"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                <span class="text-gray-700 text-sm">
                  {{ feature }}
                </span>
              </li>
            </ul>

            <!-- CTA Button -->
            <router-link
              to="/contact"
              :class="[
                'block text-center w-full py-3 px-6 rounded-lg font-semibold transition-all duration-300',
                activeProgram === program.id
                  ? 'bg-red-600 text-white hover:bg-red-700 shadow-md hover:shadow-lg'
                  : 'bg-gray-900 text-white hover:bg-black shadow-md hover:shadow-lg'
              ]"
            >
              Enroll Now
            </router-link>
          </div>
        </div>
      </div>

      <!-- Consultation Banner -->
      <div class="bg-gradient-to-r from-red-600 to-black rounded-2xl shadow-xl p-8 sm:p-12">
        <div class="max-w-4xl mx-auto text-center">
          <h3 class="text-2xl sm:text-3xl font-bold text-white mb-4">
            Not sure which program is right for you?
          </h3>
          <p class="text-red-100 text-lg mb-8">
            Book a free consultation with our coaching staff.
          </p>
          
         <router-link
            to="/contact"
             href="https://calendly.com/mubeenahma1123/30min"
                target="_blank"
           class="bg-white text-red-600 px-8 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105">
            Schedule Free Consultation
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Import images
import userImage from '../assets/user.webp'
import targetImage from '../assets/target.webp'
import trophyImage from '../assets/trophy.webp'

export default {
  name: 'Programs',
  data() {
    return {
      activeProgram: 2, // Initially set to Intermediate Training (Most Popular)
      programs: [
        {
          id: 1,
          title: "Junior Development",
          age: "Age 6-12",
          level: "Beginner",
          price: "$99",
          popular: false,
          image: userImage,
          features: [
            "Basic cricket fundamentals",
            "Fun learning environment",
            "Motor skills development",
            "Team building activities",
            "2 sessions per week"
          ]
        },
        {
          id: 2,
          title: "Intermediate Training",
          age: "Age 13-17",
          level: "Intermediate",
          price: "$149",
          popular: true,
          image: targetImage,
          features: [
            "Advanced technique training",
            "Match strategies & tactics",
            "Fitness & conditioning",
            "Mental toughness coaching",
            "3 sessions per week"
          ]
        },
        {
          id: 3,
          title: "Elite Performance",
          age: "Age 16+",
          level: "Advanced",
          price: "$249",
          popular: false,
          image: trophyImage,
          features: [
            "Professional-level training",
            "Video analysis & feedback",
            "Personalized training plans",
            "Match preparation",
            "5 sessions per week"
          ]
        },
        {
          id: 4,
          title: "Weekend Warrior",
          age: "All Ages",
          level: "All Levels",
          price: "$79",
          popular: false,
          image: userImage,
          features: [
            "Flexible weekend sessions",
            "Skill maintenance",
            "Friendly match practice",
            "Weekend sessions only"
          ]
        }
      ]
    };
  },
  methods: {
    selectProgram(programId) {
      this.activeProgram = programId;
    }
  }
};
</script>

<style scoped>
/* Additional styles if needed */
</style>