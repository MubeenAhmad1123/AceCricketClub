<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4 max-w-4xl">
      <h1 class="text-4xl font-bold text-center mb-8 text-gray-800">
        Live Match Score
      </h1>
      
      <Scorecard :data="matchData" />
      
      <div class="mt-8 text-center">
        <button 
          @click="refreshScore" 
          class="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg font-semibold transition-colors shadow-lg"
        >
          Refresh Score
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Scorecard from '@/components/Scorecard.vue'

const matchData = ref({
  match: {
    competition: 'ICC CWC League 2',
    date: 'Today',
    meta: 'ODI 86 of 73',
    result: 'USA won by 106 runs'
  },
  teams: [
    {
      id: 'usa',
      name: 'United States',
      flag: 'https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg',
      score: { runs: 262, wickets: 6, overs: '50' }
    },
    {
      id: 'nepal',
      name: 'Nepal',
      flag: 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Flag_of_Nepal.svg',
      score: { runs: 156, wickets: 10, overs: '39.1' }
    }
  ]
})

const refreshScore = () => {
  console.log('Refreshing score...')
  // TODO: Add your API call here
}
</script>