<template>
  <div class="w-full bg-gray-900 rounded-lg shadow-2xl p-6 md:p-8">
    <!-- Match Header -->
    <div class="text-gray-400 text-sm mb-6">
      <span class="font-medium">{{ data.match.competition }}</span>
      <span class="mx-2">·</span>
      <span>{{ data.match.date }}</span>
    </div>

    <!-- Main Scorecard Layout -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
      <!-- Left Team -->
      <div class="flex flex-col items-center md:items-end text-center md:text-right">
        <div class="w-16 h-16 rounded-lg overflow-hidden mb-3 border-2 border-gray-700 flex-shrink-0">
          <img 
            v-if="data.teams[0].flag" 
            :src="data.teams[0].flag" 
            :alt="`${data.teams[0].name} flag`"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full bg-gray-800 flex items-center justify-center text-2xl">
            🏏
          </div>
        </div>
        
        <h3 class="text-gray-300 text-lg font-medium mb-4">{{ data.teams[0].name }}</h3>
        
        <div class="score-animate">
          <div class="text-score-blue text-4xl font-bold mb-1">
            {{ formatScore(data.teams[0].score) }}
          </div>
          <div v-if="data.teams[0].score.overs" class="text-gray-500 text-sm">
            ({{ data.teams[0].score.overs }})
          </div>
        </div>
      </div>

      <!-- Center Result -->
      <div class="text-center order-last md:order-none mt-6 md:mt-0">
        <p class="text-gray-300 text-lg font-medium mb-2">
          {{ data.match.result }}
        </p>
        <p class="text-gray-500 text-sm">
          {{ data.match.meta }}
        </p>
      </div>

      <!-- Right Team -->
      <div class="flex flex-col items-center md:items-start text-center md:text-left">
        <div class="w-16 h-16 rounded-lg overflow-hidden mb-3 border-2 border-gray-700 flex-shrink-0">
          <img 
            v-if="data.teams[1].flag" 
            :src="data.teams[1].flag" 
            :alt="`${data.teams[1].name} flag`"
            class="w-full h-full object-cover"
          />
          <div v-else class="w-full h-full bg-gray-800 flex items-center justify-center text-2xl">
            🏏
          </div>
        </div>
        
        <h3 class="text-gray-300 text-lg font-medium mb-4">{{ data.teams[1].name }}</h3>
        
        <div class="score-animate">
          <div class="text-score-blue text-4xl font-bold mb-1">
            {{ formatScore(data.teams[1].score) }}
          </div>
          <div v-if="data.teams[1].score.overs" class="text-gray-500 text-sm">
            ({{ data.teams[1].score.overs }})
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

const formatScore = (score) => {
  if (score.wickets !== undefined) {
    return `${score.runs}/${score.wickets}`
  }
  return score.runs.toString()
}
</script>

<style scoped>
.text-score-blue {
  color: #9ad0ff;
}

.score-animate {
  animation: fadeInScore 0.8s ease-out;
}

@keyframes fadeInScore {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>