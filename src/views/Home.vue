<template>
  <div>
    <!-- Toast Notification - Must be at root level -->
    <Transition name="slide-fade">
      <div v-if="toast.show" 
           :class="['fixed top-4 right-4 z-50 max-w-md w-full bg-white rounded-lg shadow-2xl border-l-4 p-4', 
                    toast.type === 'success' ? 'border-green-500' : 'border-blue-500']">
        <div class="flex items-start">
          <div :class="['flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center',
                        toast.type === 'success' ? 'bg-green-100' : 'bg-blue-100']">
            <svg v-if="toast.type === 'success'" class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <svg v-else class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </div>
          <div class="ml-3 flex-1">
            <p class="text-sm font-semibold text-gray-900">{{ toast.message }}</p>
          </div>
          <button @click="toast.show = false" class="ml-4 flex-shrink-0 text-gray-400 hover:text-gray-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </Transition>

    <!-- Professional Hero Section -->
    <section
      class="relative min-h-screen flex items-center bg-gradient-to-br from-slate-900 via-slate-800 to-red-900 text-white overflow-hidden">
      <!-- Animated Background Pattern -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute inset-0"
          style="background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAxMCAwIEwgMCAwIDAgMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg=='); background-size: 40px 40px;">
        </div>
      </div>

      <!-- Decorative Gradient Orbs -->
      <div
        class="absolute top-0 right-0 w-96 h-96 bg-red-500 rounded-full opacity-20 blur-3xl transform translate-x-1/2 -translate-y-1/2">
      </div>
      <div
        class="absolute bottom-0 left-0 w-96 h-96 bg-blue-500 rounded-full opacity-20 blur-3xl transform -translate-x-1/2 translate-y-1/2">
      </div>
      <div class="absolute top-1/2 left-1/2 w-64 h-64 bg-purple-500 rounded-full opacity-10 blur-3xl"></div>

      <!-- Main Content -->
      <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-32">
        <div class="text-center space-y-8">

          <!-- Badge with Tailwind Animation -->
          <div class="animate-fade-in-down">
            <span
              class="inline-flex items-center gap-2 px-4 py-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full text-sm font-semibold text-white shadow-lg">
              <span class="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
              Welcome to Excellence
            </span>
          </div>

          <!-- Main Heading with Tailwind Animation -->
          <div class="animate-fade-in-up delay-400">
            <h1
              class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-black mb-6 leading-tight tracking-tight">
              <span class="block text-white">Welcome to</span>
              <span class="block bg-gradient-to-r from-red-400 via-red-500 to-red-600 bg-clip-text text-transparent">
                Ace Cricket Club
              </span>
            </h1>
          </div>

          <!-- Subheading with Tailwind Animation -->
          <div class="animate-fade-in-up delay-600">
            <p
              class="text-lg sm:text-xl md:text-2xl lg:text-3xl text-gray-300 max-w-4xl mx-auto leading-relaxed font-light text-center">
              Where champions are made, records are broken, and legends are born
            </p>
          </div>

          <!-- CTA Buttons with Tailwind Animation -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center pt-4 animate-fade-in-up delay-800">
            <router-link to="/team"
              class="group relative inline-flex items-center justify-center gap-2 px-8 py-4 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white text-lg font-bold rounded-xl transition-all duration-300 transform hover:scale-105 hover:shadow-2xl hover:shadow-red-500/50 min-w-[200px] no-underline">
              <span>Meet Our Team</span>
              <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none"
                stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </router-link>

            <router-link to="/fixtures"
              class="group relative inline-flex items-center justify-center gap-2 px-8 py-4 bg-white/10 backdrop-blur-sm hover:bg-white/20 border-2 border-white/30 hover:border-white text-white text-lg font-bold rounded-xl transition-all duration-300 transform hover:scale-105 hover:shadow-2xl min-w-[200px] no-underline">
              <span>View Fixtures</span>
              <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none"
                stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </router-link>
          </div>

          <!-- Stats with Tailwind Staggered Animation -->
          <div class="pt-12 animate-fade-in delay-1000">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
              <div
                class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-1">
                <div class="text-3xl md:text-4xl font-black text-red-500 mb-2">150+</div>
                <div class="text-sm md:text-base text-gray-400 font-medium">Matches Played</div>
              </div>

              <div
                class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-1">
                <div class="text-3xl md:text-4xl font-black text-red-500 mb-2">85%</div>
                <div class="text-sm md:text-base text-gray-400 font-medium">Win Rate</div>
              </div>

              <div
                class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-1">
                <div class="text-3xl md:text-4xl font-black text-red-500 mb-2">20+</div>
                <div class="text-sm md:text-base text-gray-400 font-medium">Team Players</div>
              </div>

              <div
                class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-1">
                <div class="text-3xl md:text-4xl font-black text-red-500 mb-2">5</div>
                <div class="text-sm md:text-base text-gray-400 font-medium">Championships</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-10">
        <div class="flex flex-col items-center gap-2 text-white/60 hover:text-white transition-colors cursor-pointer">
          <span class="text-xs font-medium uppercase tracking-wider">Scroll Down</span>
          <svg class="w-6 h-6 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </div>
    </section>

    <!-- About Section with Tailwind Animations -->
    <section class="bg-white py-20 md:py-28">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-2 gap-8 md:gap-12 items-center">
          <div>
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">About Our Club</h2>
            <p class="text-gray-600 text-base md:text-lg mb-4 leading-relaxed">
              Founded in 2010, Ace Cricket Club has become one of the most prestigious cricket clubs in Punjab.
              We are committed to developing talent, fostering sportsmanship, and achieving excellence on the field.
            </p>
            <p class="text-gray-600 text-base md:text-lg mb-6 leading-relaxed">
              Our state-of-the-art facilities, experienced coaching staff, and passionate team members make us
              a force to be reckoned with in local and regional tournaments.
            </p>
            <div class="flex flex-wrap gap-4">
              <div class="flex items-center bg-gray-50 px-4 py-3 rounded-lg shadow-md">
                <svg class="w-5 h-5 md:w-6 md:h-6 text-red-500 mr-2 flex-shrink-0" fill="currentColor"
                  viewBox="0 0 20 20">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd" />
                </svg>
                <span class="text-gray-700 font-medium text-sm md:text-base">Professional Coaching</span>
              </div>
              <div class="flex items-center bg-gray-50 px-4 py-3 rounded-lg shadow-md">
                <svg class="w-5 h-5 md:w-6 md:h-6 text-red-500 mr-2 flex-shrink-0" fill="currentColor"
                  viewBox="0 0 20 20">
                  <path fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd" />
                </svg>
                <span class="text-gray-700 font-medium text-sm md:text-base">Modern Facilities</span>
              </div>
            </div>
          </div>
          <div class="relative">
            <!-- Main Image -->
            <div class="rounded-2xl h-80 md:h-96 overflow-hidden shadow-2xl transform hover:rotate-2 transition-transform duration-500">
              <img 
                src="/src/assets/main.webp" 
                alt="Ace Cricket Club" 
                class="w-full h-full object-cover"
              />
            </div>
            <!-- Bottom Right Image Badge -->
            <div class="absolute -bottom-4 -right-4 md:-bottom-6 md:-right-6 bg-slate-900 rounded-2xl w-40 h-40 md:w-48 md:h-48 overflow-hidden shadow-xl transform hover:-rotate-3 transition-transform duration-500">
              <img 
                src="/src/assets/badge.webp" 
                alt="15+ Years of Excellence" 
                class="w-full h-full object-cover opacity-30"
              />
              <div class="absolute inset-0 flex items-center justify-center text-white text-center p-4">
                <div>
                  <div class="text-3xl md:text-4xl font-bold">15+</div>
                  <div class="text-xs md:text-sm">Years of Excellence</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Players -->
    <section class="bg-gray-50 py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12 md:mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">Our Star Players</h2>
        </div>
        <p class="text-gray-600 text-base md:text-lg text-center mb-1.5 pb-2.5">Meet the champions who lead our team to victory</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
          <div v-for="player in featuredPlayers" :key="player.id">
            <PlayerCard :player="player" />
          </div>
        </div>
        <div class="text-center mt-16 mb-8">
          <router-link to="/team"
            class="inline-block bg-red-500 hover:bg-red-600 text-white px-8 py-4 rounded-lg font-semibold transition-all transform hover:scale-105 shadow-lg no-underline">
            View Full Team
          </router-link>
        </div>
      </div>
    </section>

    <!-- Upcoming Matches Section -->
    <section class="bg-gradient-to-br from-gray-50 to-gray-100 relative overflow-hidden py-20">
      <!-- Decorative Background Pattern -->
      <div class="absolute inset-0 opacity-5">
        <div class="absolute inset-0"
          style="background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAxMCAwIEwgMCAwIDAgMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg=='); background-size: 30px 30px;">
        </div>
      </div>

      <!-- Floating Decorative Elements -->
      <div class="absolute top-10 right-10 w-32 h-32 bg-red-500/10 rounded-full blur-3xl"></div>
      <div class="absolute bottom-10 left-10 w-40 h-40 bg-red-400/10 rounded-full blur-3xl"></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <!-- Section Header -->
        <div class="text-center mb-12 md:mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
            Upcoming Matches
          </h2>
          <p class="text-gray-600 text-base md:text-lg max-w-2xl mx-auto">
            Mark your calendars for these exciting matchups
          </p>
        </div>

        <!-- Matches Grid -->
        <div class="grid md:grid-cols-2 gap-6 md:gap-8">
          <div v-for="fixture in upcomingFixtures" :key="fixture.id"
            class="bg-white rounded-2xl shadow-xl overflow-hidden hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border border-gray-200">

            <!-- Match Header -->
            <div class="bg-gradient-to-r from-red-500 to-red-600 px-6 py-4">
              <div class="flex flex-wrap justify-around items-center gap-2">
                <span class="bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-white uppercase tracking-wide">
                  {{ fixture.matchType }}
                </span>
                <div class="flex items-center text-white/90 text-sm font-medium">
                  <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  {{ formatDate(fixture.date) }}
                </div>
              </div>
            </div>

            <!-- Match Content -->
            <div class="p-6">
              <!-- Teams Display -->
              <div class="flex items-center justify-between mb-6">
                <div class="text-center flex-1">
                  <div class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-gray-100 to-gray-200 rounded-full flex items-center justify-center shadow-md">
                    <span class="text-2xl">🏏</span>
                  </div>
                  <div class="font-bold text-slate-900 text-base md:text-lg">{{ fixture.homeTeam }}</div>
                  <div class="text-xs text-gray-500 mt-1">Home</div>
                </div>

                <div class="px-4">
                  <div class="w-14 h-14 bg-gradient-to-br from-red-500 to-red-600 rounded-full flex items-center justify-center shadow-lg">
                    <span class="text-white font-bold text-sm">VS</span>
                  </div>
                </div>

                <div class="text-center flex-1">
                  <div class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-gray-100 to-gray-200 rounded-full flex items-center justify-center shadow-md">
                    <span class="text-2xl">🏏</span>
                  </div>
                  <div class="font-bold text-slate-900 text-base md:text-lg">{{ fixture.awayTeam }}</div>
                  <div class="text-xs text-gray-500 mt-1">Away</div>
                </div>
              </div>

              <!-- Match Details -->
              <div class="bg-gray-50 rounded-xl p-4 space-y-3">
                <div class="flex items-center text-gray-700">
                  <div class="w-8 h-8 bg-red-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
                    <svg class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-xs text-gray-500 font-medium">Venue</div>
                    <div class="text-sm font-semibold">{{ fixture.venue }}</div>
                  </div>
                </div>

                <div class="flex items-center text-gray-700">
                  <div class="w-8 h-8 bg-red-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
                    <svg class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-xs text-gray-500 font-medium">Match Time</div>
                    <div class="text-sm font-semibold">{{ fixture.time }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Match Footer -->
            <div class="px-6 pb-6">
              <button @click="setReminder(fixture)"
                :class="['w-full py-3 rounded-xl font-semibold transition-all transform hover:scale-105 shadow-md hover:shadow-lg flex items-center justify-center gap-2',
                         reminders[fixture.id] ? 'bg-green-500 hover:bg-green-600 text-white' : 'bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white']">
                <svg v-if="reminders[fixture.id]" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                </svg>
                {{ reminders[fixture.id] ? 'Reminder Set ✓' : 'Get Reminders' }}
              </button>
            </div>
          </div>
        </div>

        <!-- View All Button -->
        <div class="text-center mt-16 mb-8">
          <router-link to="/fixtures"
            class="inline-flex items-center gap-2 bg-slate-900 hover:bg-slate-800 text-white px-10 py-4 rounded-xl font-bold transition-all transform hover:scale-105 shadow-xl hover:shadow-2xl no-underline">
            <span>View All Fixtures</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Achievements & Trophies Section -->
    <section class="bg-white py-20 md:py-28">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">Our Achievements</h2>
          <p class="text-gray-600 text-base md:text-lg">A legacy of excellence and victory</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div
            class="bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-2xl p-8 text-center border-2 border-yellow-300 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
            <div class="text-6xl mb-4">🏆</div>
            <div class="text-3xl font-bold text-slate-900 mb-2">5</div>
            <div class="text-gray-700 font-semibold">Championships</div>
          </div>

          <div
            class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-8 text-center border-2 border-blue-300 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
            <div class="text-6xl mb-4">🥇</div>
            <div class="text-3xl font-bold text-slate-900 mb-2">12</div>
            <div class="text-gray-700 font-semibold">Tournament Wins</div>
          </div>

          <div
            class="bg-gradient-to-br from-green-50 to-green-100 rounded-2xl p-8 text-center border-2 border-green-300 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
            <div class="text-6xl mb-4">⭐</div>
            <div class="text-3xl font-bold text-slate-900 mb-2">8</div>
            <div class="text-gray-700 font-semibold">Player Awards</div>
          </div>

          <div
            class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl p-8 text-center border-2 border-purple-300 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
            <div class="text-6xl mb-4">🎖️</div>
            <div class="text-3xl font-bold text-slate-900 mb-2">3</div>
            <div class="text-gray-700 font-semibold">Regional Titles</div>
          </div>
        </div>

        <!-- Recent Trophy Showcase -->
        <div class="mt-16 bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-8 md:p-12 text-white">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div class="flex-shrink-0">
              <div
                class="w-32 h-32 bg-gradient-to-br from-yellow-400 to-yellow-600 rounded-full flex items-center justify-center text-6xl shadow-2xl">
                🏆
              </div>
            </div>
            <div class="flex-1 text-center md:text-left">
              <h3 class="text-2xl md:text-3xl font-bold mb-2">Punjab Premier League Champions 2024</h3>
              <p class="text-gray-300 text-lg mb-4">Defeating Punjab Warriors in the grand finale</p>
              <div class="flex flex-wrap gap-4 justify-center md:justify-start">
                <span class="bg-white/10 px-4 py-2 rounded-lg text-sm">Match Score: 245/6</span>
                <span class="bg-white/10 px-4 py-2 rounded-lg text-sm">Man of the Match: Ali Hassan</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Latest News & Updates -->
    <section class="bg-gradient-to-br from-gray-50 to-gray-100 py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-slate-900 mb-4">Latest News</h2>
          <p class="text-gray-600 text-base md:text-lg">Stay updated with our latest achievements and announcements</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <!-- Article 1: Regional Championship -->
          <article
            class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
            <router-link to="/news/ace-cricket-club-wins-regional-championship">
              <div class="h-48 overflow-hidden">
                <img 
                  :src="regionalChampionship" 
                  alt="Regional Championship Victory"
                  class="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
                />
              </div>
            </router-link>
            <div class="p-6">
              <div class="text-xs text-red-500 font-semibold mb-2">OCT 20, 2025</div>
              <router-link to="/news/ace-cricket-club-wins-regional-championship">
                <h3 class="text-xl font-bold text-slate-900 mb-3 hover:text-red-500 transition-colors">
                  Ace Cricket Club Wins Regional Championship
                </h3>
              </router-link>
              <p class="text-gray-600 mb-4">
                In a thrilling final match, captain Ahmed Khan scored an unbeaten century to secure victory.
              </p>
              <router-link 
                to="/news/ace-cricket-club-wins-regional-championship" 
                class="text-red-500 font-semibold hover:text-red-600 inline-flex items-center gap-2"
              >
                Read More
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </article>

          <!-- Article 2: Training Facility -->
          <article
            class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
            <router-link to="/news/new-training-facility-iqbal-stadium">
              <div class="h-48 overflow-hidden">
                <img 
                  :src="newFacility" 
                  alt="New Training Facility"
                  class="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
                />
              </div>
            </router-link>
            <div class="p-6">
              <div class="text-xs text-blue-500 font-semibold mb-2">OCT 22, 2025</div>
              <router-link to="/news/new-training-facility-iqbal-stadium">
                <h3 class="text-xl font-bold text-slate-900 mb-3 hover:text-blue-500 transition-colors">
                  New Training Facility Opens at Iqbal Stadium
                </h3>
              </router-link>
              <p class="text-gray-600 mb-4">
                State-of-the-art training facility with modern equipment and coaching staff inaugurated.
              </p>
              <router-link 
                to="/news/new-training-facility-iqbal-stadium" 
                class="text-blue-500 font-semibold hover:text-blue-600 inline-flex items-center gap-2"
              >
                Read More
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </article>

          <!-- Article 3: Captain of the Year -->
          <article
            class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
            <router-link to="/news/ahmed-khan-captain-of-the-year">
              <div class="h-48 overflow-hidden">
                <img 
                  :src="captainOfYear" 
                  alt="Captain of the Year"
                  class="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
                />
              </div>
            </router-link>
            <div class="p-6">
              <div class="text-xs text-green-500 font-semibold mb-2">OCT 18, 2025</div>
              <router-link to="/news/ahmed-khan-captain-of-the-year">
                <h3 class="text-xl font-bold text-slate-900 mb-3 hover:text-green-500 transition-colors">
                  Ahmed Khan Named Captain of the Year
                </h3>
              </router-link>
              <p class="text-gray-600 mb-4">
                Our captain receives prestigious award for outstanding leadership and performance throughout the season.
              </p>
              <router-link 
                to="/news/ahmed-khan-captain-of-the-year" 
                class="text-green-500 font-semibold hover:text-green-600 inline-flex items-center gap-2"
              >
                Read More
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </article>
        </div>

        <!-- See More Button -->
        <div class="text-center mt-12">
          <router-link 
            to="/news" 
            class="inline-flex items-center gap-3 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white px-8 py-4 rounded-xl font-bold text-lg shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
          >
            <span>See More News</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Statistics & Performance -->
    <section class="bg-slate-900 py-20 md:py-28 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-4">Season Performance</h2>
          <p class="text-gray-400 text-base md:text-lg">Our outstanding statistics for the current season</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div
            class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8 text-center hover:bg-white/10 transition-all">
            <div class="text-5xl font-black text-red-500 mb-4">2,450</div>
            <div class="text-gray-400 text-sm uppercase tracking-wider mb-2">Total Runs</div>
            <div class="w-full bg-gray-700 rounded-full h-2 mb-2">
              <div class="bg-red-500 h-2 rounded-full" style="width: 88%"></div>
            </div>
            <div class="text-xs text-gray-500">88% of target</div>
          </div>

          <div
            class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8 text-center hover:bg-white/10 transition-all">
            <div class="text-5xl font-black text-blue-500 mb-4">156</div>
            <div class="text-gray-400 text-sm uppercase tracking-wider mb-2">Wickets Taken</div>
            <div class="w-full bg-gray-700 rounded-full h-2 mb-2">
              <div class="bg-blue-500 h-2 rounded-full" style="width: 92%"></div>
            </div>
            <div class="text-xs text-gray-500">92% of target</div>
          </div>

          <div
            class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8 text-center hover:bg-white/10 transition-all">
            <div class="text-5xl font-black text-green-500 mb-4">45</div>
            <div class="text-gray-400 text-sm uppercase tracking-wider mb-2">Sixes Hit</div>
            <div class="w-full bg-gray-700 rounded-full h-2 mb-2">
              <div class="bg-green-500 h-2 rounded-full" style="width: 75%"></div>
            </div>
            <div class="text-xs text-gray-500">75% of target</div>
          </div>

          <div
            class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8 text-center hover:bg-white/10 transition-all">
            <div class="text-5xl font-black text-yellow-500 mb-4">8.5</div>
            <div class="text-gray-400 text-sm uppercase tracking-wider mb-2">Run Rate</div>
            <div class="w-full bg-gray-700 rounded-full h-2 mb-2">
              <div class="bg-yellow-500 h-2 rounded-full" style="width: 85%"></div>
            </div>
            <div class="text-xs text-gray-500">Excellent performance</div>
          </div>
        </div>

        <!-- Performance Chart Placeholder -->
        <div class="mt-16 bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
          <h3 class="text-2xl font-bold mb-6">Match Results This Season</h3>
          <div class="grid grid-cols-3 gap-4 mb-8">
            <div class="text-center">
              <div class="text-4xl font-bold text-green-500 mb-2">17</div>
              <div class="text-gray-400 text-sm">Wins</div>
            </div>
            <div class="text-center">
              <div class="text-4xl font-bold text-red-500 mb-2">3</div>
              <div class="text-gray-400 text-sm">Losses</div>
            </div>
            <div class="text-center">
              <div class="text-4xl font-bold text-yellow-500 mb-2">0</div>
              <div class="text-gray-400 text-sm">Draws</div>
            </div>
          </div>
          <div class="h-2 bg-gray-700 rounded-full overflow-hidden flex">
            <div class="bg-green-500" style="width: 85%"></div>
            <div class="bg-red-500" style="width: 15%"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Training & Facilities -->
    <Facilities />
    
    <Programs />
    <Coaches />
    
    <!-- Testimonials -->
    <Testimonials />
    <Partner />
    


    <!-- Call to Action -->
    <section class="bg-gradient-to-r from-red-500 to-red-600 py-20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-6">Ready to Join Ace Cricket Club?</h2>
        <p class="text-lg md:text-xl mb-8 text-red-100">Be part of a winning legacy. Train with the best, compete at the highest level.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
           <router-link
            to="/programs"
            class="bg-white text-red-600 px-10 py-4 rounded-xl font-bold hover:bg-gray-100 transition-all transform hover:scale-105 shadow-xl">
            Join Training Program
          </router-link>
        <router-link
            to="/contact"
            class="bg-transparent border-2 border-white text-white px-10 py-4 rounded-xl font-bold hover:bg-white hover:text-red-600 transition-all transform hover:scale-105">
            Contact Us
          </router-link>
        </div>
      </div>
    </section>
    <Contact />

  </div>
</template>

<script setup>
import PlayerCard from '@/components/PlayerCard.vue'
import Programs from '@/views/program.vue'
import Coaches from '@/views/Coaches.vue'
import Contact from '@/views/Contact.vue'
import Testimonials from '@/views/Testimonials.vue'
import Facilities from '@/views/Facilities.vue'
import playersData from '@/data/players.json'
import fixturesData from '@/data/fixtures.json'
import regionalChampionship from '@/assets/regional-championship.webp'
import newFacility from '@/assets/new-facility.webp'
import captainOfYear from '@/assets/captain-of-year.webp'

import { ref, onMounted, onUnmounted, computed } from 'vue';
import Partner from './Partner.vue'

const featuredPlayers = ref(playersData.slice(0, 3))
const upcomingFixtures = ref(fixturesData.filter(f => f.status === 'upcoming').slice(0, 2))





const toast = ref({ show: false, message: '', type: '' });
const reminders = ref({});
let checkInterval = null;

// Load reminders from localStorage on mount
onMounted(() => {
  const saved = localStorage.getItem('cricketReminders');
  if (saved) {
    reminders.value = JSON.parse(saved);
  }

  // Check reminders every minute
  checkInterval = setInterval(() => {
    checkReminders();
  }, 60000);

  // Also check immediately
  checkReminders();
});

onUnmounted(() => {
  if (checkInterval) {
    clearInterval(checkInterval);
  }
});

// Format date
const formatDate = (dateStr) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric' 
  });
};

// Show toast notification
const showToast = (message, type = 'success') => {
  toast.value = { show: true, message, type };
  setTimeout(() => {
    toast.value = { show: false, message: '', type: '' };
  }, 4000);
};

// Request browser notification permission
const requestNotificationPermission = async () => {
  if ('Notification' in window) {
    const permission = await Notification.requestPermission();
    return permission === 'granted';
  }
  return false;
};

// Set reminder for a match
const setReminder = async (fixture) => {
  // Request notification permission
  const hasPermission = await requestNotificationPermission();
  
  if (!hasPermission) {
    showToast('Please enable browser notifications to receive reminders!', 'info');
    return;
  }

  // Save reminder
  reminders.value[fixture.id] = {
    matchType: fixture.matchType,
    homeTeam: fixture.homeTeam,
    awayTeam: fixture.awayTeam,
    venue: fixture.venue,
    date: fixture.date,
    time: fixture.time,
    notified30Min: false,
    notified1Hour: false
  };

  // Save to localStorage
  localStorage.setItem('cricketReminders', JSON.stringify(reminders.value));
  
  showToast(`Reminder set for ${fixture.homeTeam} vs ${fixture.awayTeam}!`, 'success');
};

// Check if it's time to send reminders
const checkReminders = () => {
  const now = new Date();

  Object.keys(reminders.value).forEach(fixtureId => {
    const reminder = reminders.value[fixtureId];
    const matchDateTime = new Date(`${reminder.date}T${reminder.time}:00`);
    const timeDiff = matchDateTime - now;

    // Send notification 1 hour before (between 59-61 minutes)
    if (!reminder.notified1Hour && timeDiff > 0 && timeDiff <= 3660000 && timeDiff >= 3540000) {
      sendNotification(
        '🏏 Match Starting in 1 Hour!',
        `${reminder.homeTeam} vs ${reminder.awayTeam} at ${reminder.venue}`
      );
      reminders.value[fixtureId].notified1Hour = true;
      localStorage.setItem('cricketReminders', JSON.stringify(reminders.value));
    }

    // Send notification 30 minutes before (between 29-31 minutes)
    if (!reminder.notified30Min && timeDiff > 0 && timeDiff <= 1860000 && timeDiff >= 1740000) {
      sendNotification(
        '🏏 Match Starting in 30 Minutes!',
        `${reminder.homeTeam} vs ${reminder.awayTeam} - Get Ready!`
      );
      reminders.value[fixtureId].notified30Min = true;
      localStorage.setItem('cricketReminders', JSON.stringify(reminders.value));
    }

    // Clean up old reminders (matches that have passed)
    if (timeDiff < -7200000) { // 2 hours after match time
      delete reminders.value[fixtureId];
      localStorage.setItem('cricketReminders', JSON.stringify(reminders.value));
    }
  });
};

// Send browser notification
const sendNotification = (title, body) => {
  if (Notification.permission === 'granted') {
    new Notification(title, {
      body: body,
      icon: '🏏',
      badge: '🏏',
      tag: 'cricket-match',
      requireInteraction: true
    });
    
    // Also show toast
    showToast(title, 'info');
  }
};
</script>

<style scoped>
/* Essential CSS for features not available in Tailwind */
.bg-clip-text {
  -webkit-background-clip: text;
  background-clip: text;
}

.no-underline {
  text-decoration: none !important;
}

.backdrop-blur-sm {
  backdrop-filter: blur(12px);
}

/* Custom delay classes */
.delay-400 {
  animation-delay: 0.4s;
  animation-fill-mode: both;
}

.delay-600 {
  animation-delay: 0.6s;
  animation-fill-mode: both;
}

.delay-800 {
  animation-delay: 0.8s;
  animation-fill-mode: both;
}

.delay-1000 {
  animation-delay: 1s;
  animation-fill-mode: both;
}


/* Toast Animation */
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s ease-in;
}

.slide-fade-enter-from {
  transform: translateX(20px);
  opacity: 0;
}

.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>