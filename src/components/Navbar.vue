<template>
  <nav
    class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 shadow-2xl sticky top-0 z-50 border-b border-slate-700/50 backdrop-blur-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Logo & Brand -->
        <router-link to="/" class="flex items-center space-x-3 group relative">
          <div class="relative">
            <div
              class="absolute inset-0 bg-red-500 rounded-full blur-md opacity-50 group-hover:opacity-75 transition-opacity">
            </div>
            <div
              class="relative w-14 h-14 rounded-full flex items-center justify-center transform group-hover:scale-110 group-hover:rotate-12 transition-all duration-300 shadow-lg overflow-hidden ring-2 ring-red-500/50 group-hover:ring-red-400">
              <img src="/src/assets/ace.webp" alt="Ace Cricket Club logo" class="w-full h-full object-cover" />
            </div>
          </div>
          <div class="hidden sm:block">
            <span class="text-white font-black text-2xl tracking-tight">Ace Cricket</span>
            <div class="text-red-400 text-xs font-semibold tracking-wider uppercase">Club</div>
          </div>
        </router-link>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-4">
          <router-link v-for="link in navLinks" :key="link.path" :to="link.path"
            class="relative px-4 py-2 rounded-xl font-bold transition-all duration-300 overflow-hidden whitespace-nowrap"
            :class="$route.path === link.path 
              ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg shadow-red-500/50' 
              : 'text-gray-300 hover:text-white hover:bg-gradient-to-r hover:from-red-500 hover:to-red-600 hover:shadow-lg hover:shadow-red-500/30 transform hover:scale-105'">
            <!-- Icon -->
            <span class="relative flex items-center gap-2">
              <svg v-if="link.icon" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="link.icon" />
              </svg>
              {{ link.name }}
            </span>
          </router-link>

          <!-- More Dropdown -->
          <div class="relative" @mouseenter="dropdownOpen = true" @mouseleave="dropdownOpen = false">
            <button
              class="relative px-4 py-2 rounded-xl text-gray-300 hover:text-white font-semibold text-sm transition-all duration-300 overflow-hidden whitespace-nowrap hover:bg-slate-700/50 flex items-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
              </svg>
            </button>

            <!-- Dropdown Menu -->
            <transition enter-active-class="transition-all duration-200 ease-out"
              leave-active-class="transition-all duration-150 ease-in"
              enter-from-class="opacity-0 scale-95 -translate-y-2" enter-to-class="opacity-100 scale-100 translate-y-0"
              leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 -translate-y-2">
              <div v-if="dropdownOpen"
                class="absolute right-0 mt-2 w-52 bg-gradient-to-b from-slate-800 to-slate-900 rounded-xl shadow-2xl border border-slate-700/50 overflow-hidden py-2">
                <router-link v-for="item in moreLinks" :key="item.path" :to="item.path"
                  class="flex items-center gap-3 px-4 py-2.5 text-sm font-medium transition-all duration-300 group"
                  :class="$route.path === item.path 
                    ? 'bg-gradient-to-r from-red-500 to-red-600 text-white' 
                    : 'text-gray-300 hover:text-white hover:bg-gradient-to-r hover:from-red-500/80 hover:to-red-600/80'">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                  </svg>
                  {{ item.name }}
                  <svg
                    class="w-3.5 h-3.5 ml-auto opacity-0 group-hover:opacity-100 transform group-hover:translate-x-1 transition-all duration-300"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                </router-link>
              </div>
            </transition>
          </div>

          <!-- CTA Button -->
          <router-link to="/contact"
            class="ml-2 px-5 py-2 text-white font-semibold text-sm rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700 transform hover:scale-105 transition-all duration-300 shadow-lg hover:shadow-emerald-500/50 whitespace-nowrap ring-2 ring-emerald-400/20">
            Join Us
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden relative w-10 h-10 text-gray-300 hover:text-white focus:outline-none rounded-lg hover:bg-slate-700/50 transition-all duration-300 flex items-center justify-center group">
          <div class="relative w-6 h-6">
            <!-- Hamburger to X animation -->
            <span class="absolute left-0 top-1 w-6 h-0.5 bg-current transform transition-all duration-300 rounded-full"
              :class="mobileMenuOpen ? 'rotate-45 top-2.5' : ''"></span>
            <span class="absolute left-0 top-2.5 w-6 h-0.5 bg-current transition-all duration-300 rounded-full"
              :class="mobileMenuOpen ? 'opacity-0' : ''"></span>
            <span class="absolute left-0 top-4 w-6 h-0.5 bg-current transform transition-all duration-300 rounded-full"
              :class="mobileMenuOpen ? '-rotate-45 top-2.5' : ''"></span>
          </div>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition enter-active-class="transition-all duration-300 ease-out"
      leave-active-class="transition-all duration-200 ease-in" enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0" leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2">
      <div v-if="mobileMenuOpen"
        class="md:hidden bg-gradient-to-b from-slate-800 to-slate-900 border-t border-slate-700/50 shadow-xl">
        <div class="px-4 pt-4 pb-6 space-y-3">
          <!-- Main Links -->
          <router-link v-for="link in navLinks" :key="link.path" :to="link.path" @click="mobileMenuOpen = false"
            class="flex items-center gap-3 px-5 py-4 rounded-xl font-semibold transition-all duration-300 transform hover:translate-x-1 group"
            :class="$route.path === link.path 
              ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg' 
              : 'text-gray-300 hover:text-white hover:bg-gradient-to-r hover:from-red-500 hover:to-red-600 hover:shadow-lg'">
            <svg v-if="link.icon" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="link.icon" />
            </svg>
            {{ link.name }}
            <svg
              class="w-4 h-4 ml-auto opacity-0 group-hover:opacity-100 transform group-hover:translate-x-1 transition-all duration-300"
              fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </router-link>

          <!-- Mobile More Section -->
          <div class="pt-3 border-t border-slate-700/50">
            <button @click="mobileMoreOpen = !mobileMoreOpen"
              class="flex items-center justify-between w-full px-5 py-3 rounded-xl text-gray-300 hover:text-white hover:bg-slate-700/50 font-medium text-sm transition-all duration-300">
              <span class="flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z" />
                </svg>
                More Options
              </span>
              <svg class="w-4 h-4 transition-transform duration-300" :class="{ 'rotate-180': mobileMoreOpen }"
                fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Mobile Dropdown Items -->
            <transition enter-active-class="transition-all duration-300 ease-out"
              leave-active-class="transition-all duration-200 ease-in" enter-from-class="opacity-0 max-h-0"
              enter-to-class="opacity-100 max-h-96" leave-from-class="opacity-100 max-h-96"
              leave-to-class="opacity-0 max-h-0">
              <div v-if="mobileMoreOpen" class="mt-2 space-y-2 pl-4 overflow-hidden">
                <router-link v-for="item in moreLinks" :key="item.path" :to="item.path"
                  @click="mobileMenuOpen = false"
                  class="flex items-center gap-2.5 px-4 py-2.5 rounded-lg text-sm font-medium transition-all duration-300 transform hover:translate-x-1 group"
                  :class="$route.path === item.path 
                    ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg' 
                    : 'text-gray-300 hover:text-white hover:bg-gradient-to-r hover:from-red-500/80 hover:to-red-600/80'">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                  </svg>
                  {{ item.name }}
                  <svg
                    class="w-3.5 h-3.5 ml-auto opacity-0 group-hover:opacity-100 transform group-hover:translate-x-1 transition-all duration-300"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                </router-link>
              </div>
            </transition>
          </div>

          <!-- Mobile CTA -->
          <router-link to="/contact" @click="mobileMenuOpen = false"
            class="flex items-center justify-center gap-2 px-5 py-3.5 mt-4 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-semibold text-sm shadow-lg hover:shadow-emerald-500/50 transform hover:scale-105 transition-all duration-300 ring-2 ring-emerald-400/20">
            Join Our Club
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </router-link>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)
const dropdownOpen = ref(false)
const mobileMoreOpen = ref(false)

const navLinks = [
  {
    name: 'Home',
    path: '/',
    icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6'
  },
  {
    name: 'Team',
    path: '/team',
    icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z'
  },
  {
    name: 'Fixtures',
    path: '/fixtures',
    icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z'
  },
  {
    name: 'News',
    path: '/news',
    icon: 'M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z'
  }
]

const moreLinks = [
  {
    name: 'Facilities',
    path: '/facilities',
    icon: 'M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4'
  },
  {
    name: 'Success Stories',
    path: '/success-stories',
    icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'
  },
  {
    name: 'Coaches',
    path: '/coaches',
    icon: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z'
  },
  {
  name: 'Programs',
  path: '/programs',
  icon: 'M12 14l9-5-9-5-9 5 9 5z M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222'
},
 {
  name: 'Partners',
  path: '/partners',
  icon: 'M9 11l3 3 8-8m-8 8l-4 4a4 4 0 01-5.657-5.657l5.657-5.657a4 4 0 015.657 0L19 9',
}

]
</script>

<style scoped>
/* Smooth transitions for dropdown */
.max-h-0 {
  max-height: 0;
}

.max-h-96 {
  max-height: 24rem;
}
</style>