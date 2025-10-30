<template>
  <div class="min-h-screen bg-white">
    <!-- Header -->
    <section class="relative bg-gradient-to-r from-slate-900 via-red-900 to-slate-900 text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl font-bold mb-4">Match Fixtures</h1>
        <p class="text-xl text-gray-300">Stay updated with our match schedule and results</p>
      </div>
    </section>

    <!-- Filter Tabs -->
    <section class="bg-gray-900 border-b border-gray-800 sticky top-0 z-40 shadow-2xl">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex gap-3 overflow-x-auto py-6">
          <button 
            @click="filterStatus = 'all'"
            :class="filterStatus === 'all' ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'"
            class="px-8 py-3 rounded-xl font-semibold whitespace-nowrap transition-all duration-300"
          >
            All Matches
          </button>
          <button 
            @click="filterStatus = 'upcoming'"
            :class="filterStatus === 'upcoming' ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'"
            class="px-8 py-3 rounded-xl font-semibold whitespace-nowrap transition-all duration-300"
          >
            Upcoming
          </button>
          <button 
            @click="filterStatus = 'completed'"
            :class="filterStatus === 'completed' ? 'bg-gradient-to-r from-red-500 to-red-600 text-white shadow-lg' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'"
            class="px-8 py-3 rounded-xl font-semibold whitespace-nowrap transition-all duration-300"
          >
            Completed
          </button>
        </div>
      </div>
    </section>

    <!-- Fixtures List -->
    <section class="py-12">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="space-y-6">
          <div 
            v-for="fixture in filteredFixtures" 
            :key="fixture.id"
            @click="openMatchDetails(fixture)"
            class="bg-gray-900 rounded-lg shadow-2xl overflow-hidden hover:shadow-3xl transition-all duration-300 cursor-pointer transform hover:scale-102 border-2 border-gray-800"
          >
            <!-- Match Card -->
            <div class="px-6 py-4 border-b border-gray-800 bg-gray-950">
              <div class="flex flex-wrap items-center justify-between gap-3">
                <div class="flex items-center gap-2">
                  <span class="text-gray-300 text-sm font-medium">{{ fixture.matchType }}</span>
                  <span class="text-gray-600">·</span>
                  <span 
                    :class="fixture.status === 'upcoming' ? 'text-blue-400 bg-blue-950' : 'text-green-400 bg-green-950'"
                    class="text-sm font-semibold capitalize px-3 py-1 rounded-full border border-gray-700"
                  >
                    {{ fixture.status }}
                  </span>
                </div>
                <div class="text-gray-400 text-sm flex items-center gap-2">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"/>
                  </svg>
                  {{ formatDate(fixture.date) }} at {{ fixture.time }}
                </div>
              </div>
            </div>

            <!-- Teams -->
            <div class="p-6 bg-gray-900">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <!-- Home Team -->
                <div class="flex flex-col items-center text-center">
                  <div class="w-16 h-16 rounded-lg overflow-hidden mb-3 border-2 border-gray-700 flex-shrink-0">
                   <img 
                      v-if="fixture.homeFlag" 
                      :src="getTeamFlag(fixture.homeFlag)" 
                      :alt="`${fixture.homeTeam} flag`"
                      class="w-full h-full object-cover"
                    />
                    <div v-else class="w-full h-full bg-gray-800 flex items-center justify-center text-2xl">
                      🏏
                    </div>
                  </div>
                  <h3 
                    :class="fixture.homeTeam === 'Ace Cricket Club' ? 'text-red-500' : 'text-gray-300'"
                    class="text-lg font-bold mb-3"
                  >
                    {{ fixture.homeTeam }}
                  </h3>
                  <div v-if="fixture.scorecard" class="text-4xl font-bold text-blue-400">
                    {{ fixture.scorecard.home.innings.runs }}/{{ fixture.scorecard.home.innings.wickets }}
                  </div>
                  <div v-if="fixture.scorecard" class="text-sm text-gray-500 mt-1">
                    ({{ fixture.scorecard.home.innings.overs }} overs)
                  </div>
                </div>

                <!-- VS / Result -->
                <div class="text-center">
                  <div v-if="fixture.result" class="space-y-2">
                    <div class="text-sm font-semibold text-green-400 bg-green-950 px-4 py-2 rounded-lg border border-green-800">
                      {{ fixture.result }}
                    </div>
                  </div>
                  <div v-else class="w-16 h-16 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mx-auto text-gray-400 font-bold text-xl border-2 border-gray-700">
                    VS
                  </div>
                </div>

                <!-- Away Team -->
                <div class="flex flex-col items-center text-center">
                  <div class="w-16 h-16 rounded-lg overflow-hidden mb-3 border-2 border-gray-700 flex-shrink-0">
                    <img 
                      v-if="fixture.awayFlag" 
                      :src="getTeamFlag(fixture.awayFlag)" 
                      :alt="`${fixture.awayTeam} flag`"
                      class="w-full h-full object-cover"
                    />
                    <div v-else class="w-full h-full bg-gray-800 flex items-center justify-center text-2xl">
                      🏏
                    </div>
                  </div>
                  <h3 
                    :class="fixture.awayTeam === 'Ace Cricket Club' ? 'text-red-500' : 'text-gray-300'"
                    class="text-lg font-bold mb-3"
                  >
                    {{ fixture.awayTeam }}
                  </h3>
                  <div v-if="fixture.scorecard" class="text-4xl font-bold text-blue-400">
                    {{ fixture.scorecard.away.innings.runs }}/{{ fixture.scorecard.away.innings.wickets }}
                  </div>
                  <div v-if="fixture.scorecard" class="text-sm text-gray-500 mt-1">
                    ({{ fixture.scorecard.away.innings.overs }} overs)
                  </div>
                </div>
              </div>

              <!-- Venue -->
              <div class="mt-6 pt-4 border-t border-gray-800">
                <div class="flex items-center justify-center text-gray-400 text-sm">
                  <svg class="w-4 h-4 mr-2 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                  <span>{{ fixture.venue }}</span>
                </div>
              </div>

              <!-- Click to view details -->
              <div class="mt-4 text-center">
                <span class="text-sm text-blue-400 font-medium flex items-center justify-center gap-1">
                  Click to view {{ fixture.status === 'completed' ? 'full scorecard' : 'playing elevens' }}
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div v-if="filteredFixtures.length === 0" class="text-center py-24">
          <div class="w-32 h-32 bg-gray-800 rounded-full flex items-center justify-center mx-auto mb-6 border-2 border-gray-700">
            <svg class="w-16 h-16 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2" stroke-width="2"/>
              <line x1="16" y1="2" x2="16" y2="6" stroke-width="2"/>
              <line x1="8" y1="2" x2="8" y2="6" stroke-width="2"/>
              <line x1="3" y1="10" x2="21" y2="10" stroke-width="2"/>
            </svg>
          </div>
          <h3 class="text-3xl font-bold text-gray-400 mb-3">No matches found</h3>
          <p class="text-gray-500 text-lg">Check back later for upcoming fixtures</p>
        </div>
      </div>
    </section>

    <!-- Modal for Match Details -->
    <div v-if="selectedMatch" class="fixed inset-0 bg-black bg-opacity-75 z-50 flex items-center justify-center p-4" @click="closeModal">
      <div class="bg-gray-900 rounded-lg max-w-6xl w-full max-h-[90vh] overflow-y-auto border-2 border-gray-800" @click.stop>
        <!-- Modal Header -->
        <div class="sticky top-0 bg-gradient-to-r from-slate-900 via-red-900 to-slate-900 text-white px-6 py-4 flex justify-between items-center z-10">
          <div>
            <h2 class="text-2xl font-bold">{{ selectedMatch.homeTeam }} vs {{ selectedMatch.awayTeam }}</h2>
            <p class="text-sm text-gray-300 mt-1">{{ selectedMatch.matchType }} • {{ formatDate(selectedMatch.date) }}</p>
          </div>
          <button @click="closeModal" class="text-white hover:text-gray-300 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <!-- Modal Content -->
        <div class="p-6">
          <!-- Match Result -->
          <div v-if="selectedMatch.result" class="mb-6 text-center">
            <div class="inline-block bg-green-950 border-2 border-green-600 rounded-lg px-6 py-3">
              <p class="text-lg font-bold text-green-400">{{ selectedMatch.result }}</p>
            </div>
            <div v-if="selectedMatch.scorecard?.playerOfTheMatch" class="mt-3">
              <p class="text-sm text-gray-400">
                <span class="font-semibold">Player of the Match:</span> {{ selectedMatch.scorecard.playerOfTheMatch }}
              </p>
            </div>
          </div>

          <!-- Completed Match - Scorecard -->
          <div v-if="selectedMatch.status === 'completed' && selectedMatch.scorecard">
            <!-- Home Team Innings -->
            <div class="mb-8">
              <div class="bg-red-600 text-white px-4 py-3 rounded-t-lg">
                <h3 class="text-xl font-bold">{{ selectedMatch.scorecard.home.name }}</h3>
                <p class="text-2xl font-bold mt-1">
                  {{ selectedMatch.scorecard.home.innings.runs }}/{{ selectedMatch.scorecard.home.innings.wickets }}
                  <span class="text-sm font-normal">({{ selectedMatch.scorecard.home.innings.overs }} overs)</span>
                </p>
              </div>

              <!-- Batting Table -->
              <div class="overflow-x-auto bg-gray-950 rounded-b-lg">
                <table class="w-full text-sm">
                  <thead class="bg-gray-900 border-b-2 border-gray-700">
                    <tr>
                      <th class="text-left px-4 py-3 font-semibold text-gray-300">Batsman</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">R</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">B</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">4s</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">6s</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">SR</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(batsman, idx) in selectedMatch.scorecard.home.batting" :key="idx" class="border-b border-gray-800 hover:bg-gray-900">
                      <td class="px-4 py-3">
                        <div class="font-medium text-gray-200">{{ batsman.name }}</div>
                        <div class="text-xs text-gray-500">{{ batsman.dismissal }}</div>
                      </td>
                      <td class="text-center px-2 py-3 font-semibold text-gray-300">{{ batsman.runs }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.balls }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.fours }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.sixes }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.sr }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Bowling Table -->
              <div class="mt-6">
                <h4 class="font-bold text-gray-300 mb-2 px-4">Bowling</h4>
                <div class="overflow-x-auto bg-gray-950 rounded-lg">
                  <table class="w-full text-sm">
                    <thead class="bg-gray-900 border-b-2 border-gray-700">
                      <tr>
                        <th class="text-left px-4 py-3 font-semibold text-gray-300">Bowler</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">O</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">M</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">R</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">W</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">Econ</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(bowler, idx) in selectedMatch.scorecard.away.bowling" :key="idx" class="border-b border-gray-800 hover:bg-gray-900">
                        <td class="px-4 py-3 font-medium text-gray-200">{{ bowler.name }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.overs }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.maidens }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.runs }}</td>
                        <td class="text-center px-2 py-3 font-semibold text-gray-300">{{ bowler.wickets }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.economy }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            <!-- Away Team Innings -->
            <div class="mb-8">
              <div class="bg-blue-600 text-white px-4 py-3 rounded-t-lg">
                <h3 class="text-xl font-bold">{{ selectedMatch.scorecard.away.name }}</h3>
                <p class="text-2xl font-bold mt-1">
                  {{ selectedMatch.scorecard.away.innings.runs }}/{{ selectedMatch.scorecard.away.innings.wickets }}
                  <span class="text-sm font-normal">({{ selectedMatch.scorecard.away.innings.overs }} overs)</span>
                </p>
              </div>

              <!-- Batting Table -->
              <div class="overflow-x-auto bg-gray-950 rounded-b-lg">
                <table class="w-full text-sm">
                  <thead class="bg-gray-900 border-b-2 border-gray-700">
                    <tr>
                      <th class="text-left px-4 py-3 font-semibold text-gray-300">Batsman</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">R</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">B</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">4s</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">6s</th>
                      <th class="text-center px-2 py-3 font-semibold text-gray-300">SR</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(batsman, idx) in selectedMatch.scorecard.away.batting" :key="idx" class="border-b border-gray-800 hover:bg-gray-900">
                      <td class="px-4 py-3">
                        <div class="font-medium text-gray-200">{{ batsman.name }}</div>
                        <div class="text-xs text-gray-500">{{ batsman.dismissal }}</div>
                      </td>
                      <td class="text-center px-2 py-3 font-semibold text-gray-300">{{ batsman.runs }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.balls }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.fours }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.sixes }}</td>
                      <td class="text-center px-2 py-3 text-gray-400">{{ batsman.sr }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Bowling Table -->
              <div class="mt-6">
                <h4 class="font-bold text-gray-300 mb-2 px-4">Bowling</h4>
                <div class="overflow-x-auto bg-gray-950 rounded-lg">
                  <table class="w-full text-sm">
                    <thead class="bg-gray-900 border-b-2 border-gray-700">
                      <tr>
                        <th class="text-left px-4 py-3 font-semibold text-gray-300">Bowler</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">O</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">M</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">R</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">W</th>
                        <th class="text-center px-2 py-3 font-semibold text-gray-300">Econ</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(bowler, idx) in selectedMatch.scorecard.home.bowling" :key="idx" class="border-b border-gray-800 hover:bg-gray-900">
                        <td class="px-4 py-3 font-medium text-gray-200">{{ bowler.name }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.overs }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.maidens }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.runs }}</td>
                        <td class="text-center px-2 py-3 font-semibold text-gray-300">{{ bowler.wickets }}</td>
                        <td class="text-center px-2 py-3 text-gray-400">{{ bowler.economy }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- Upcoming Match - Playing Elevens -->
          <div v-if="selectedMatch.status === 'upcoming' && selectedMatch.playingElevens">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- Home Team -->
              <div>
                <div class="bg-red-600 text-white px-4 py-3 rounded-t-lg">
                  <h3 class="text-xl font-bold">{{ selectedMatch.homeTeam }}</h3>
                  <p class="text-sm">Playing XI</p>
                </div>
                <div class="border-2 border-gray-800 rounded-b-lg bg-gray-950">
                  <ul class="divide-y divide-gray-800">
                    <li v-for="(player, idx) in selectedMatch.playingElevens.home" :key="idx" class="px-4 py-3 hover:bg-gray-900 flex items-center gap-3">
                      <span class="w-8 h-8 bg-red-950 text-red-400 rounded-full flex items-center justify-center font-bold text-sm border border-red-800">
                        {{ idx + 1 }}
                      </span>
                      <span class="font-medium text-gray-300">{{ player }}</span>
                    </li>
                  </ul>
                </div>
              </div>

              <!-- Away Team -->
              <div>
                <div class="bg-blue-600 text-white px-4 py-3 rounded-t-lg">
                  <h3 class="text-xl font-bold">{{ selectedMatch.awayTeam }}</h3>
                  <p class="text-sm">Playing XI</p>
                </div>
                <div class="border-2 border-gray-800 rounded-b-lg bg-gray-950">
                  <ul class="divide-y divide-gray-800">
                    <li v-for="(player, idx) in selectedMatch.playingElevens.away" :key="idx" class="px-4 py-3 hover:bg-gray-900 flex items-center gap-3">
                      <span class="w-8 h-8 bg-blue-950 text-blue-400 rounded-full flex items-center justify-center font-bold text-sm border border-blue-800">
                        {{ idx + 1 }}
                      </span>
                      <span class="font-medium text-gray-300">{{ player }}</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import fixturesData from '../data/fixtures.json'

// Import all team flag images
import aceFlag from '@/assets/ace.webp'
import faisalabadFlag from '@/assets/faislabad.webp'
import punjabFlag from '@/assets/punjab.webp'
import multanFlag from '@/assets/multan.webp'
import karachiFlag from '@/assets/karachi.webp'
import islamabadFlag from '@/assets/islambad.webp'
import peshawarFlag from '@/assets/peshawar.webp'
import royalFlag from '@/assets/royal.webp'

export default {
  name: 'Fixtures',
  setup() {
    const fixtures = ref(fixturesData)
    const filterStatus = ref('all')
    const selectedMatch = ref(null)

    // Map of flag identifiers to imported images
    const flagMap = {
      'ace': aceFlag,
      'faislabad': faisalabadFlag,
      'punjab': punjabFlag,
      'multan': multanFlag,
      'karachi': karachiFlag,
      'islambad': islamabadFlag,
      'peshawar': peshawarFlag,
      'royal': royalFlag
    }

    const filteredFixtures = computed(() => {
      if (filterStatus.value === 'all') {
        return fixtures.value
      }
      return fixtures.value.filter(fixture => fixture.status === filterStatus.value)
    })

    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', { 
        weekday: 'short',
        month: 'short', 
        day: 'numeric', 
        year: 'numeric' 
      })
    }

    const getTeamFlag = (flagIdentifier) => {
      // Extract the flag name from the identifier (e.g., "ace" from any format)
      if (!flagIdentifier) return null
      
      // Get the filename from the path
      const fileName = flagIdentifier.split('/').pop().replace('.webp', '')
      return flagMap[fileName] || null
    }

    const openMatchDetails = (fixture) => {
      selectedMatch.value = fixture
    }

    const closeModal = () => {
      selectedMatch.value = null
    }

    return {
      fixtures,
      filterStatus,
      selectedMatch,
      filteredFixtures,
      formatDate,
      getTeamFlag,
      openMatchDetails,
      closeModal
    }
  }
}
</script>

<style scoped>
.hover\:scale-102:hover {
  transform: scale(1.02);
}
</style>