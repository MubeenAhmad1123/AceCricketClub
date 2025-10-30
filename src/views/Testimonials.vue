<template>
  <section
    class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 py-16 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-7xl mx-auto">
      <!-- Header Section -->
      <div class="text-center mb-16">
        <h2 class="text-4xl sm:text-5xl font-bold text-gray-900 mb-4">
          Success Stories
        </h2>
        <p class="text-xl sm:text-2xl text-red-600 font-semibold mb-4">
          What Our Students Say
        </p>
        <p class="text-gray-600 max-w-3xl mx-auto text-lg">
          Don't just take our word for it. Hear from students and parents who
          have experienced the transformation firsthand.
        </p>
      </div>

      <!-- Testimonials Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        <figure
          v-for="testimonial in testimonials"
          :key="testimonial.name"
          class="group bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden p-8"
        >
          <!-- Photo -->
          <div class="flex justify-center mb-6">
            <div
              class="w-24 h-24 rounded-full overflow-hidden ring-4 ring-red-100 group-hover:ring-red-200 transition-all duration-300"
            >
              <img
                :src="testimonial.photo"
                :alt="testimonial.alt"
                class="w-full h-full object-cover"
                loading="lazy"
              />
            </div>
          </div>

          <!-- Name & Role -->
          <div class="text-center mb-4">
            <h3 class="text-xl font-bold text-gray-900 mb-1">
              {{ testimonial.name }}
            </h3>
            <div class="flex items-center justify-center gap-2">
              <span
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-4 h-4 mr-1"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                {{ testimonial.role }}
              </span>
            </div>
          </div>

          <!-- Quote -->
          <blockquote class="text-gray-600 text-center italic leading-relaxed">
            <svg
              class="w-8 h-8 text-red-600 mx-auto mb-2 opacity-50"
              fill="currentColor"
              viewBox="0 0 32 32"
            >
              <path
                d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.8 3.456-8.256 9.12-8.256 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z"
              />
            </svg>
            "{{ testimonial.quote }}"
          </blockquote>
        </figure>
      </div>

      <!-- Community Banner -->
      <div class="bg-white rounded-2xl shadow-xl p-8 sm:p-12">
        <h3 class="text-3xl font-bold text-gray-900 text-center mb-8">
          Join Our Growing Community
        </h3>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div
            v-for="stat in stats"
            :key="stat.title"
            class="text-center p-6 bg-gradient-to-br from-red-50 to-red-100 rounded-xl"
          >
            <div
              class="w-12 h-12 bg-red-600 rounded-full flex items-center justify-center mx-auto mb-4"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-6 h-6 text-white"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <p class="text-2xl font-bold text-gray-900 mb-1">
              {{ stat.value }}
            </p>
            <p class="text-gray-600 font-medium">{{ stat.title }}</p>
          </div>
        </div>

        <!-- CTA Button -->
        <div class="flex justify-center">
          <router-link
            to="/contact"
            class="inline-block bg-red-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-red-700 transition-colors shadow-lg hover:shadow-xl"
          >
            Start Your Journey
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Import all testimonial images
import farhanImage from '@/assets/farhan.webp'
import saimImage from '@/assets/saim.webp'
import amantImage from '@/assets/amant.webp'
import fatimaImage from '@/assets/fatima.webp'
import azamImage from '@/assets/azam.webp'
import sidraImage from '@/assets/sidra.webp'

export default {
  name: 'Testimonials',
  data() {
    return {
      testimonials: [
        {
          name: "Sahibzada Farhan",
          role: "Student Parent",
          quote:
            "My son joined as a complete beginner and within 6 months, he was selected for his school team. The coaches here really know how to bring out the best in young players.",
          photo: farhanImage,
          alt: "Sahibzada Farhan – Parent testimonial, Ace Cricket Club",
        },
        {
          name: "Saim Ayub",
          role: "Advanced Student",
          quote:
            "The quality of coaching here is exceptional. The personalized attention and professional guidance have helped me refine my technique significantly. I recently scored my first century in a district match!",
          photo: saimImage,
          alt: "Saim Ayub – Advanced Student testimonial, Ace Cricket Club",
        },
        {
          name: "Amanat Chan",
          role: "Student Parent",
          quote:
            "Both my kids train here and the transformation has been incredible. Not just in their cricket skills, but also in their confidence and discipline. Best decision we made for their development.",
          photo: amantImage,
          alt: "Amanat Chan – Parent testimonial, Ace Cricket Club",
        },
        {
          name: "Fatima Sana",
          role: "Intermediate Student",
          quote:
            "As a female cricketer, I was looking for a supportive environment where I could develop my skills. I found exactly that here. The coaches are encouraging and professional. I'm now playing at state level.",
          photo: fatimaImage,
          alt: "Fatima Sana – Intermediate Student testimonial, Ace Cricket Club",
        },
        {
          name: "Azam Siddique",
          role: "Student Parent",
          quote:
            "The structured programs and professional approach make all the difference. My son's bowling has improved dramatically, and he's now one of the key players in his team. Highly recommended!",
          photo: azamImage,
          alt: "Azam Siddique – Parent testimonial, Ace Cricket Club",
        },
        {
          name: "Sidra Ameen",
          role: "Junior Student",
          quote:
            "I started at age 7 and now I'm 12 and playing for my district. The coaches are so nice and they make practice fun while teaching us important skills. I love coming to practice every week!",
          photo: sidraImage,
          alt: "Sidra Ameen – Junior Student testimonial, Ace Cricket Club",
        },
      ],
      stats: [
        {
          title: "Students Trained",
          value: "500+",
        },
        {
          title: "Satisfaction Rate",
          value: "98%",
        },
        {
          title: "Team Selections",
          value: "50+",
        },
      ]
    }
  }
}
</script>

<style scoped>
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .transform:hover {
    transform: none !important;
  }
}

figure:focus {
  outline: 2px solid #ef4444;
  outline-offset: 2px;
}

button:focus {
  outline: 2px solid #ef4444;
  outline-offset: 2px;
}
</style>