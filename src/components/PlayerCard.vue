<template>
  <div
    class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 w-full max-w-md mx-auto">
         
    <!-- Player Image - Dynamic aspect ratio based on ID -->
    <div 
      :class="[
        'relative bg-gradient-to-br from-slate-700 to-slate-900 overflow-hidden',
        player.id <= 9 ? 'aspect-landscape' : 'aspect-square'
      ]"
    >
      <img
        v-if="player.image"
        :src="getImageUrl(player.image)"
        :alt="player.name"
        class="w-full h-full object-cover object-center transition-transform duration-500 hover:scale-105"
      />
      <div
        v-else
        class="w-full h-full flex items-center justify-center text-white text-6xl font-bold">
        {{ player.name.charAt(0) }}
      </div>
       
      <!-- Role Badge -->
      <div class="absolute bottom-4 left-4 bg-red-500 text-white px-4 py-1.5 rounded-full text-sm font-semibold shadow-md">
        {{ player.role }}
      </div>
    </div>
     
    <!-- Player Info -->
    <div class="p-6">
      <h3 class="text-2xl font-bold text-slate-900 mb-1 text-center">{{ player.name }}</h3>
      <p class="text-red-500 font-medium mb-4 text-center">{{ player.specialization }}</p>
       
      <!-- Stats Grid -->
      <div class="grid grid-cols-3 gap-4 mb-4">
        <div class="text-center">
          <p class="text-2xl font-bold text-slate-900">{{ player.matches }}</p>
          <p class="text-xs text-gray-500 uppercase tracking-wider">Matches</p>
        </div>
        <div class="text-center border-x border-gray-200">
          <p class="text-2xl font-bold text-slate-900">
            {{ player.runs ? player.runs : player.wickets }}
          </p>
          <p class="text-xs text-gray-500 uppercase tracking-wider">
            {{ player.runs ? 'Runs' : 'Wickets' }}
          </p>
        </div>
        <div class="text-center">
          <p class="text-2xl font-bold text-slate-900">{{ player.average }}</p>
          <p class="text-xs text-gray-500 uppercase tracking-wider">Average</p>
        </div>
      </div>
       
      <!-- Additional Info -->
      <div class="flex items-center justify-between text-sm text-gray-600 border-t pt-4">
        <div class="flex items-center gap-1">
          <svg class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <span class="truncate max-w-[120px]">
            {{ player.battingStyle || player.bowlingStyle }}
          </span>
        </div>
         
        <div class="flex items-center gap-1">
          <svg class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
          <span>Age: {{ player.age }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  player: {
    type: Object,
    required: true
  }
})

// Function to dynamically import images
const getImageUrl = (imageName) => {
  return new URL(`../assets/${imageName}`, import.meta.url).href
}
</script>

<style scoped>
/* Landscape aspect ratio for IDs 1-8 (1280x800 images) */
.aspect-landscape {
  aspect-ratio: 2 / 1.5;
}

/* Square aspect ratio for IDs 9-16 (1024x1024 images) */
.aspect-square {
  aspect-ratio: 1 / 1;
}
</style>