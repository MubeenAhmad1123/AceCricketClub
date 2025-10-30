<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <section class="bg-gradient-to-r from-slate-900 to-red-900 text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl font-bold mb-4">Our Team</h1>
        <p class="text-xl text-gray-300">Meet the warriors of Ace Cricket Club</p>
      </div>
    </section>

    <!-- Filter Buttons -->
    <section class="bg-white border-b sticky top-16 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex flex-wrap gap-3 justify-center">
          <button 
            @click="filterRole = 'all'"
            :class="filterRole === 'all' ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            class="px-6 py-2 rounded-lg font-semibold transition-colors"
          >
            All Players
          </button>
          <button 
            @click="filterRole = 'Batsman'"
            :class="filterRole === 'Batsman' ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            class="px-6 py-2 rounded-lg font-semibold transition-colors"
          >
            Batsmen
          </button>
          <button 
            @click="filterRole = 'Bowler'"
            :class="filterRole === 'Bowler' ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            class="px-6 py-2 rounded-lg font-semibold transition-colors"
          >
            Bowlers
          </button>
          <button 
            @click="filterRole = 'All-Rounder'"
            :class="filterRole === 'All-Rounder' ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            class="px-6 py-2 rounded-lg font-semibold transition-colors"
          >
            All-Rounders
          </button>
          <button 
            @click="filterRole = 'Wicket Keeper'"
            :class="filterRole === 'Wicket Keeper' ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'"
            class="px-6 py-2 rounded-lg font-semibold transition-colors"
          >
            Wicket Keepers
          </button>
        </div>
      </div>
    </section>

    <!-- Players Grid -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="mb-8 text-center">
          <p class="text-gray-600">
            Showing <span class="font-bold text-red-500">{{ filteredPlayers.length }}</span> 
            {{ filterRole === 'all' ? 'players' : filterRole.toLowerCase() + 's' }}
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <PlayerCard 
            v-for="player in filteredPlayers" 
            :key="player.id" 
            :player="player" 
          />
        </div>

        <div v-if="filteredPlayers.length === 0" class="text-center py-20">
          <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
          </svg>
          <h3 class="text-2xl font-bold text-gray-400 mb-2">No players found</h3>
          <p class="text-gray-500">Try selecting a different filter</p>
        </div>
      </div>
    </section>

    <!-- Team Stats -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-slate-900 text-center mb-12">Team Statistics</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="bg-gradient-to-br from-red-500 to-red-600 rounded-xl p-6 text-white">
            <div class="text-4xl font-bold mb-2">{{ totalPlayers }}</div>
            <div class="text-red-100">Total Players</div>
          </div>
          <div class="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-6 text-white">
            <div class="text-4xl font-bold mb-2">{{ averageAge }}</div>
            <div class="text-blue-100">Average Age</div>
          </div>
          <div class="bg-gradient-to-br from-green-500 to-green-600 rounded-xl p-6 text-white">
            <div class="text-4xl font-bold mb-2">{{ totalMatches }}</div>
            <div class="text-green-100">Total Matches</div>
          </div>
          <div class="bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl p-6 text-white">
            <div class="text-4xl font-bold mb-2">{{ totalRuns }}</div>
            <div class="text-purple-100">Total Runs</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import PlayerCard from '@/components/PlayerCard.vue'
import playersData from '@/data/players.json'

const players = ref(playersData)
const filterRole = ref('all')

const filteredPlayers = computed(() => {
  if (filterRole.value === 'all') {
    return players.value
  }
  return players.value.filter(player => player.role === filterRole.value)
})

const totalPlayers = computed(() => players.value.length)
const averageAge = computed(() => {
  const total = players.value.reduce((sum, player) => sum + player.age, 0)
  return Math.round(total / players.value.length)
})
const totalMatches = computed(() => {
  return players.value.reduce((sum, player) => sum + player.matches, 0)
})
const totalRuns = computed(() => {
  return players.value.reduce((sum, player) => sum + (player.runs || 0), 0)
})
</script>