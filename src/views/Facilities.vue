<template>
  <section class="bg-white py-20 md:py-28">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
          World-Class Facilities
        </h2>
        <p class="text-gray-600 text-base md:text-lg max-w-3xl mx-auto">
          Train Like a Professional - Access to top-tier facilities and equipment that provide the perfect environment for skill development and performance enhancement
        </p>
      </div>

      <!-- Main Facilities Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        <div 
          v-for="facility in facilities" 
          :key="facility.id"
          :class="[
            'rounded-2xl overflow-hidden border-2 hover:shadow-xl transition-shadow',
            facility.bgClass,
            facility.borderClass
          ]"
        >
          <img 
            :src="facility.image" 
            :alt="facility.title" 
            class="w-full h-48 object-cover"
          >
          <div class="p-6">
            <div class="flex items-start gap-4 mb-3">
              <div 
                :class="[
                  'w-12 h-12 rounded-xl flex items-center justify-center text-2xl flex-shrink-0',
                  facility.iconBgClass
                ]"
              >
                {{ facility.emoji }}
              </div>
              <h3 class="text-xl font-bold text-slate-900">{{ facility.title }}</h3>
            </div>
            <p class="text-gray-700">{{ facility.description }}</p>
          </div>
        </div>
      </div>

      <!-- See Our Academy in Action -->
      <div class="mb-16">
        <h3 class="text-2xl md:text-3xl font-bold text-slate-900 mb-8 text-center">
          See Our Academy in Action
        </h3>
        
        <div class="carousel-container">
          <div class="carousel-track">
            <div 
              v-for="(item, index) in duplicatedGalleryItems" 
              :key="index"
              class="carousel-item"
            >
              <img 
                :src="item.image" 
                :alt="item.title"
                class="carousel-image"
              />
              <div class="carousel-overlay">
                <div class="text-3xl mb-2">{{ item.emoji }}</div>
                <div class="text-white font-semibold text-base">{{ item.title }}</div>
                <div class="text-white/80 text-sm">{{ item.subtitle }}</div>
              </div>
            </div>
          </div>
          
          <!-- Fade edges -->
          <div class="fade-left"></div>
          <div class="fade-right"></div>
        </div>
      </div>

      <!-- Training Programs -->
      <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-8 md:p-12 text-white mb-16">
        <h3 class="text-2xl md:text-3xl font-bold mb-8 text-center">Our Training Programs</h3>
        <div class="grid md:grid-cols-3 gap-6">
          <div 
            v-for="program in trainingPrograms" 
            :key="program.id"
            class="bg-white/10 rounded-xl p-6 backdrop-blur-sm"
          >
            <div class="text-3xl mb-3">{{ program.emoji }}</div>
            <h4 class="text-xl font-bold mb-2">{{ program.title }}</h4>
            <p class="text-gray-300 text-sm mb-4">{{ program.description }}</p>
            <div class="text-red-400 font-semibold">{{ program.schedule }}</div>
          </div>
        </div>
      </div>

      <!-- Visit Our Facilities -->
      <div class="bg-gradient-to-br from-red-500 to-red-600 rounded-2xl overflow-hidden shadow-2xl">
        <div class="grid md:grid-cols-2 gap-0">
          <div class="p-8 md:p-12 text-white">
            <h3 class="text-3xl md:text-4xl font-bold mb-4">Visit Our Facilities</h3>
            <p class="text-red-100 mb-6 text-lg">
              Experience our world-class training environment firsthand. Schedule a free tour and see why <strong class="text-xl">Ace Cricket Club</strong> is the premier choice for serious cricket training.
            </p>
            
            <div class="space-y-4 mb-8">
              <div class="flex items-start gap-3">
                <div class="text-2xl">📍</div>
                <div>
                  <div class="font-semibold">123 Cricket Lane, Sports Complex</div>
                  <div class="text-red-100 text-sm">Mughalabad, Punjab</div>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <div class="text-2xl">🕒</div>
                <div>
                  <div class="font-semibold">Open 7 days a week</div>
                  <div class="text-red-100 text-sm">6 AM - 9 PM</div>
                </div>
              </div>
            </div>

            <div class="bg-white/10 backdrop-blur-sm rounded-xl p-6 mb-6">
              <h4 class="font-bold text-lg mb-4">What You'll See on Tour:</h4>
              <div class="space-y-2">
                <div 
                  v-for="(item, index) in tourFeatures" 
                  :key="index"
                  class="flex items-center gap-2"
                >
                  <span class="text-green-300">✓</span>
                  <span class="text-sm">{{ item }}</span>
                </div>
              </div>
            </div>

            <a 
              href="/contact" 
              class="inline-block bg-white text-red-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-red-50 transition-colors shadow-lg"
            >
              Schedule Your Tour
            </a>
          </div>

          <div class="relative min-h-[400px] md:min-h-0">
            <img 
              :src="facilityTourImage" 
              alt="Facility Tour" 
              class="absolute inset-0 w-full h-full object-cover"
            >
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Import all images at the top
import indoorNets from '../assets/indoor-nets.jpg'
import outdoorGround from '../assets/outdoor-ground.webp'
import bowlingMachine from '../assets/bowling macine.webp'
import videoAnalysis from '../assets/video-analysis.webp'
import fitnessCenter from '../assets/fitness-center.webp'
import playerLounge from '../assets/player-loung.webp'
import trainingSession from '../assets/training-session.webp'
import bowlingPractice from '../assets/bowling-practice.webp'
import matchDay from '../assets/match-day.webp'
import fitnessTraining from '../assets/fitness-training.webp'
import teamBuilding from '../assets/team-building.webp'
import coachFeedback from '../assets/coach-feedback.webp'
import facilityTour from '../assets/facility-tour.webp'

export default {
  name: 'FacilitiesSection',
  data() {
    return {
      facilityTourImage: facilityTour,
      facilities: [
        {
          id: 1,
          emoji: '🎯',
          title: 'Indoor Training Nets',
          description: 'Climate-controlled facility with 4 professional cricket nets, allowing year-round training regardless of weather conditions.',
          image: indoorNets,
          bgClass: 'bg-gradient-to-br from-red-50 to-red-100',
          borderClass: 'border-red-200',
          iconBgClass: 'bg-red-500'
        },
        {
          id: 2,
          emoji: '🏟️',
          title: 'Outdoor Practice Ground',
          description: 'Full-size cricket ground with professionally maintained pitch and outfield, perfect for match simulation and practice.',
          image: outdoorGround,
          bgClass: 'bg-gradient-to-br from-blue-50 to-blue-100',
          borderClass: 'border-blue-200',
          iconBgClass: 'bg-blue-500'
        },
        {
          id: 3,
          emoji: '🎰',
          title: 'Bowling Machines',
          description: 'State-of-the-art automated bowling machines with adjustable speed, spin, and trajectory for batting practice.',
          image: bowlingMachine,
          bgClass: 'bg-gradient-to-br from-green-50 to-green-100',
          borderClass: 'border-green-200',
          iconBgClass: 'bg-green-500'
        },
        {
          id: 4,
          emoji: '📹',
          title: 'Video Analysis Lab',
          description: 'High-speed cameras and analysis software to review and improve your technique with frame-by-frame feedback.',
          image: videoAnalysis,
          bgClass: 'bg-gradient-to-br from-purple-50 to-purple-100',
          borderClass: 'border-purple-200',
          iconBgClass: 'bg-purple-500'
        },
        {
          id: 5,
          emoji: '💪',
          title: 'Fitness Center',
          description: 'Dedicated gym with cricket-specific equipment for strength, conditioning, and injury prevention programs.',
          image: fitnessCenter,
          bgClass: 'bg-gradient-to-br from-orange-50 to-orange-100',
          borderClass: 'border-orange-200',
          iconBgClass: 'bg-orange-500'
        },
        {
          id: 6,
          emoji: '🛋️',
          title: 'Player Lounge',
          description: 'Comfortable space for students to relax, review match footage, and discuss strategy with coaches and teammates.',
          image: playerLounge,
          bgClass: 'bg-gradient-to-br from-teal-50 to-teal-100',
          borderClass: 'border-teal-200',
          iconBgClass: 'bg-teal-500'
        }
      ],
      galleryItems: [
        {
          emoji: '🏏',
          title: 'Training Session',
          subtitle: 'Batting techniques',
          image: trainingSession
        },
        {
          emoji: '🎯',
          title: 'Bowling Practice',
          subtitle: 'Accuracy & consistency',
          image: bowlingPractice
        },
        {
          emoji: '🏆',
          title: 'Match Day',
          subtitle: 'Practice matches',
          image: matchDay
        },
        {
          emoji: '💪',
          title: 'Fitness Training',
          subtitle: 'Conditioning sessions',
          image: fitnessTraining
        },
        {
          emoji: '👥',
          title: 'Team Building',
          subtitle: 'Group activities',
          image: teamBuilding
        },
        {
          emoji: '🎓',
          title: 'Coach Feedback',
          subtitle: 'Technical guidance',
          image: coachFeedback
        }
      ],
      trainingPrograms: [
        {
          id: 1,
          emoji: '🌱',
          title: 'Junior Academy',
          description: 'Ages 10-15, foundational skills and technique development',
          schedule: '3 days/week'
        },
        {
          id: 2,
          emoji: '⚡',
          title: 'Senior Training',
          description: 'Ages 16-25, advanced tactics and competitive preparation',
          schedule: '5 days/week'
        },
        {
          id: 3,
          emoji: '🏆',
          title: 'Professional Squad',
          description: 'Elite players, tournament preparation and match analysis',
          schedule: '6 days/week'
        }
      ],
      tourFeatures: [
        'Complete facility walkthrough',
        'Meet our coaching staff',
        'Watch live training sessions',
        'Free skill assessment',
        'Program recommendations'
      ]
    };
  },
  computed: {
    duplicatedGalleryItems() {
      return [...this.galleryItems, ...this.galleryItems, ...this.galleryItems];
    }
  }
};
</script>

<style scoped>
/* Carousel Container */
.carousel-container {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding: 20px 0;
}

/* Carousel Track - holds all images */
.carousel-track {
  display: flex;
  gap: 24px;
  width: fit-content;
  animation: scroll-left 20s linear infinite;
}

/* Pause animation on hover */
.carousel-track:hover {
  animation-play-state: paused;
}

/* Individual carousel item */
.carousel-item {
  position: relative;
  flex-shrink: 0;
  width: 320px;
  height: 240px;
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.carousel-item:hover {
  transform: translateY(-8px);
}

/* Carousel image */
.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.carousel-item:hover .carousel-image {
  transform: scale(1.1);
}

/* Overlay on image */
.carousel-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 16px;
}

/* Fade edges */
.fade-left {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 100px;
  background: linear-gradient(to right, white, transparent);
  pointer-events: none;
  z-index: 10;
}

.fade-right {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100px;
  background: linear-gradient(to left, white, transparent);
  pointer-events: none;
  z-index: 10;
}

/* Scroll Animation - Left to Right */
@keyframes scroll-left {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-33.333%);
  }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .carousel-item {
    width: 280px;
    height: 200px;
  }
  
  .fade-left,
  .fade-right {
    width: 50px;
  }
}
</style>