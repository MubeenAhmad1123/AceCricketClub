<template>
  <section class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <!-- Header Section -->
      <div class="text-center mb-16">
        <h2 class="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
          Our Coaching Staff
        </h2>
        <p class="text-xl sm:text-2xl text-red-600 font-semibold mb-4">
          Learn from the Best
        </p>
        <p class="text-gray-600 max-w-3xl mx-auto text-lg">
          Our team of professional coaches brings decades of combined experience from national and international cricket. Each coach is dedicated to helping you unlock your full potential.
        </p>
      </div>

      <!-- Coaches Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
        <div
          v-for="coach in coaches"
          :key="coach.id"
          class="group relative bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden hover:ring-2 hover:ring-red-600"
        >
          <div class="p-6">
            <!-- Coach Image -->
            <div class="flex justify-center mb-4">
              <div class="w-32 h-32 rounded-full overflow-hidden ring-4 ring-gray-100 group-hover:ring-red-200 transition-all duration-300 bg-gray-200">
                <img
                  :src="coach.image"
                  :alt="`${coach.name} – ${coach.title}`"
                  class="w-full h-full object-cover"
                  @error="handleImageError"
                />
              </div>
            </div>

            <!-- Coach Name & Title -->
            <h3 class="text-xl font-bold text-gray-900 text-center mb-1">
              {{ coach.name }}
            </h3>
            <p class="text-md font-semibold text-red-600 text-center mb-2">
              {{ coach.title }}
            </p>
            <p class="text-sm text-gray-500 text-center mb-4 italic">
              {{ coach.specialization }}
            </p>

            <!-- Credentials List -->
            <ul class="space-y-2 mb-4">
              <li
                v-for="(credential, index) in coach.credentials"
                :key="index"
                class="flex items-start gap-2 text-sm text-gray-700"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-4 h-4 text-red-600 flex-shrink-0 mt-0.5"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span>{{ credential }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Why Our Coaches Stand Out -->
      <div class="bg-white rounded-2xl shadow-xl p-8 sm:p-12 mb-12">
        <h3 class="text-3xl font-bold text-gray-900 text-center mb-8">
          Why Our Coaches Stand Out
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <div
            v-for="feature in features"
            :key="feature.id"
            class="text-center"
          >
            <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-8 h-8 text-red-600"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path :d="feature.iconPath" v-if="feature.iconPath" />
                <circle v-if="feature.iconCircle" :cx="feature.iconCircle.cx" :cy="feature.iconCircle.cy" :r="feature.iconCircle.r" />
                <polyline v-if="feature.iconPolyline" :points="feature.iconPolyline" />
              </svg>
            </div>
            <h4 class="text-xl font-bold text-gray-900 mb-2">
              {{ feature.title }}
            </h4>
            <p class="text-gray-600">
              {{ feature.description }}
            </p>
          </div>
        </div>

        <!-- CTA Button -->
        <div class="flex justify-center">
<router-link 
  to="/contact" 
  class="inline-block bg-red-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-red-700 transition-colors shadow-lg hover:shadow-xl"
>
 Meet Our Coaches
</router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const coaches = [
  {
    id: 1,
    name: "Aqib javed",
    title: "Head Coach & Director",
    specialization: "Batting & Match Strategy",
    image: "/src/assets/aqib.webp", // Using placeholder from your assets
    credentials: [
      "Former State Level Player",
      "Level 3 Certified Coach",
      "15+ years coaching experience",
      "Specialized in batting techniques",
      "Coached 20+ state-level players"
    ]
  },
  {
    id: 2,
    name: "Amir Khan",
    title: "Senior Bowling Coach",
    specialization: "Pace & Spin Bowling",
    image: "/src/assets/amir.webp",
    credentials: [
      "Former National Team Player",
      "ICC Certified Coach",
      "12+ years professional experience",
      "Fast bowling specialist",
      "International playing experience"
    ]
  },
  {
    id: 3,
    name: "Sarah Ahmed",
    title: "Youth Development Coach",
    specialization: "Junior Development",
    image: "/src/assets/sarah.webp",
    credentials: [
      "BCCI Level 2 Certified",
      "Child Psychology Degree",
      "8+ years with junior players",
      "Player development specialist",
      "Youth Coach of the Year 2023"
    ]
  },
  {
    id: 4,
    name: "David Martin",
    title: "Fitness & Conditioning Coach",
    specialization: "Strength & Conditioning",
    image: "/src/assets/david.webp",
    credentials: [
      "Sports Science Degree",
      "Certified Strength Coach",
      "10+ years in cricket fitness",
      "Injury prevention specialist",
      "Elite athlete trainer"
    ]
  }
];

const features = [
  {
    id: 1,
    title: "Personalized Attention",
    description: "Individual feedback and customized training plans for every student",
    iconPath: "M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2",
    iconCircle: { cx: "12", cy: "7", r: "4" }
  },
  {
    id: 2,
    title: "Real Experience",
    description: "Learn from coaches who've played at district, state, and national levels",
    iconCircle: { cx: "12", cy: "8", r: "7" },
    iconPolyline: "8.21 13.89 7 23 12 20 17 23 15.79 13.88"
  },
  {
    id: 3,
    title: "Proven Results",
    description: "Track record of developing players who compete at higher levels",
    iconPath: "M6 9H4.5a2.5 2.5 0 0 1 0-5H6 M18 9h1.5a2.5 2.5 0 0 0 0-5H18 M4 22h16 M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22 M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22 M18 2H6v7a6 6 0 0 0 12 0V2Z"
  }
];


const handleImageError = (e) => {
  console.error('Image failed to load:', e.target.src);
  e.target.src = './assets/user.webp'; // Fallback image
};
</script>

<style scoped>
/* Add background to show if image doesn't load */
img {
  background-color: #f3f4f6;
}
</style>