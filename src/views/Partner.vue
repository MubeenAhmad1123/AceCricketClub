<template>
  <!-- Sponsors & Partners -->
  <section class="bg-white py-20" id="Sponsors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
          Our Partners
        </h2>
        <p class="text-gray-600 text-base md:text-lg">
          Proud to be supported by leading brands
        </p>
      </div>

      <!-- Partners Carousel -->
      <div class="relative w-full overflow-hidden py-10">
        <div class="flex gap-12 md:gap-16 w-fit animate-partners-scroll hover:pause-animation">
          <div 
            v-for="(partner, index) in duplicatedPartners" 
            :key="index"
            class="flex-shrink-0 w-40 h-24 sm:w-44 sm:h-28 md:w-56 md:h-36 bg-gray-50 rounded-2xl p-6 md:p-8 flex items-center justify-center transition-all duration-300 hover:bg-white hover:shadow-xl hover:-translate-y-1"
          >
            <img
              :src="partner.logo"
              :alt="partner.name"
              class="max-w-full max-h-12 sm:max-h-14 md:max-h-20 w-auto h-auto object-contain grayscale opacity-70 transition-all duration-300 hover:grayscale-0 hover:opacity-100"
              loading="lazy"
            />
          </div>
        </div>
        
        <!-- Fade edges -->
        <div class="absolute inset-y-0 left-0 w-20 md:w-32 bg-gradient-to-r from-white to-transparent pointer-events-none z-10"></div>
        <div class="absolute inset-y-0 right-0 w-20 md:w-32 bg-gradient-to-l from-white to-transparent pointer-events-none z-10"></div>
      </div>
    </div>
  </section>
</template>

<script>
import { computed } from 'vue'

// Import all partner/brand images
import brand1 from '@/assets/brand1.webp'
import brand2 from '@/assets/brand2.webp'
import brand3 from '@/assets/brand3.webp'
import brand4 from '@/assets/brand4.webp'
import brand5 from '@/assets/brand5.webp'
import brand6 from '@/assets/brand6.webp'
import brand7 from '@/assets/brand7.webp'

export default {
  name: 'PartnersSection',
  setup() {
    const partners = [
      {
        id: 1,
        name: "Partner 1",
        logo: brand1
      },
      {
        id: 2,
        name: "Partner 2",
        logo: brand2
      },
      {
        id: 3,
        name: "Partner 3",
        logo: brand3
      },
      {
        id: 4,
        name: "Partner 4",
        logo: brand4
      },
      {
        id: 5,
        name: "Partner 5",
        logo: brand5
      },
      {
        id: 6,
        name: "Partner 6",
        logo: brand6
      },
      {
        id: 7,
        name: "Partner 7",
        logo: brand7
      }
    ]

    const duplicatedPartners = computed(() => {
      // Duplicate partners 3 times for seamless infinite scroll
      return [...partners, ...partners, ...partners]
    })

    return {
      duplicatedPartners
    }
  }
}
</script>

<style scoped>
/* Partners Carousel Animation */
@keyframes partners-scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-33.333%);
  }
}

.animate-partners-scroll {
  animation: partners-scroll 15s linear infinite;
}

.hover\:pause-animation:hover {
  animation-play-state: paused;
}

.grayscale {
  filter: grayscale(100%);
  opacity: 0.7;
}

.grayscale:hover {
  filter: grayscale(0%);
  opacity: 1;
}
</style>