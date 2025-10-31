<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <section class="bg-gradient-to-r from-slate-900 to-red-900 text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl font-bold mb-4">Latest News</h1>
        <p class="text-xl text-gray-300">Stay updated with the latest from Ace Cricket Club</p>
      </div>
    </section>

    <!-- Loading State -->
    <section v-if="loading" class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-gray-600">Loading news...</p>
        </div>
      </div>
    </section>

    <!-- No Articles -->
    <section v-else-if="!featuredNews && newsArticles.length === 0" class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-gray-600">No news articles available at the moment.</p>
        </div>
      </div>
    </section>

    <!-- News Content -->
    <section v-else class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Featured News -->
        <div v-if="featuredNews" class="bg-white rounded-2xl shadow-2xl overflow-hidden mb-12">
          <div class="md:flex">
            <div class="md:w-1/2 overflow-hidden">
              <img 
                :src="getImagePath(featuredNews.image)" 
                :alt="featuredNews.image_alt"
                class="w-full h-full object-cover"
              />
            </div>
            <div class="md:w-1/2 p-8 md:p-12">
              <div class="text-sm text-red-500 font-semibold mb-2">{{ featuredNews.category.toUpperCase() }}</div>
             <router-link :to="`/news/${featuredNews.slug}`" class="text-3xl font-bold text-slate-900 mb-4">
                {{ featuredNews.title }}
            </router-link>
              <p class="text-gray-600 mb-4">
                {{ featuredNews.excerpt }}
              </p>
              <div class="flex items-center text-sm text-gray-500 mb-6">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                <span>{{ formatDate(featuredNews.date_published) }}</span>
              </div>
              <router-link :to="`/news/${featuredNews.slug}`" class="bg-red-500 hover:bg-red-600 text-white px-6 py-2 rounded-lg font-semibold transition-colors inline-block">
                Read Full Story
              </router-link>
            </div>
          </div>
        </div>

        <!-- News Grid -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <article 
            v-for="article in regularArticles" 
            :key="article.id"
            class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition-all transform hover:-translate-y-2"
          >
            <!-- Article Image -->
            <div class="h-48 overflow-hidden">
              <img 
                :src="getImagePath(article.image)" 
                :alt="article.image_alt"
                class="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
              />
            </div>

            <!-- Article Content -->
            <div class="p-6">
              <div class="flex items-center gap-2 mb-3">
                <span class="text-xs font-semibold text-red-500 uppercase">{{ article.category }}</span>
                <span class="text-gray-400">•</span>
                <span class="text-xs text-gray-500">{{ formatDate(article.date_published) }}</span>
              </div>
              
              <h3 class="text-xl font-bold text-slate-900 mb-3 hover:text-red-500 transition-colors cursor-pointer">
                {{ article.title }}
              </h3>
              
              <p class="text-gray-600 mb-4 line-clamp-3">
                {{ article.excerpt }}
              </p>

              <div class="flex items-center justify-between">
                <div class="flex items-center text-sm text-gray-500">
                  <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"/>
                  </svg>
                  <span>{{ article.author.name }}</span>
                </div>
                <router-link 
                  :to="`/news/${article.slug}`"
                  class="text-red-500 hover:text-red-600 font-semibold text-sm transition-colors"
                >
                  Read More →
                </router-link>
              </div>
            </div>
          </article>
        </div>

        <!-- Load More Button (Optional - for future pagination) -->
        <div v-if="canLoadMore" class="text-center mt-12">
          <button 
            @click="loadMore"
            class="bg-slate-900 hover:bg-slate-800 text-white px-8 py-3 rounded-lg font-semibold transition-colors"
          >
            Load More Articles
          </button>
        </div>
      </div>
    </section>

    <!-- Newsletter Section -->
    <section class="py-16 bg-gradient-to-r from-red-500 to-red-600">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="text-3xl font-bold mb-4">Stay in the Loop</h2>
        <p class="text-xl mb-8 text-red-100">
          Subscribe to our newsletter for the latest updates, match results, and exclusive content
        </p>
        <div class="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
          <input 
            v-model="email"
            type="email" 
            placeholder="Enter your email"
            class="flex-1 px-4 py-3 rounded-lg text-gray-900 focus:outline-none focus:ring-2 focus:ring-white"
          />
          <button 
            @click="subscribe"
            class="bg-slate-900 hover:bg-slate-800 text-white px-8 py-3 rounded-lg font-semibold transition-colors whitespace-nowrap"
          >
            Subscribe
          </button>
        </div>
        <p class="text-sm text-red-100 mt-4">
          We respect your privacy. Unsubscribe at any time.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import newsData from '@/data/news.json'

// State
const loading = ref(true)
const allArticles = ref([])
const displayLimit = ref(6)
const email = ref('')

// Computed properties
const featuredNews = computed(() => {
  return allArticles.value.find(article => article.featured === true)
})

const regularArticles = computed(() => {
  return allArticles.value
    .filter(article => !article.featured)
    .slice(0, displayLimit.value)
})

const newsArticles = computed(() => {
  return allArticles.value.filter(article => !article.featured)
})

const canLoadMore = computed(() => {
  return newsArticles.value.length > displayLimit.value
})

// Methods
const getImagePath = (imagePath) => {
  if (!imagePath) return ''
  
  // If it's already a full URL, return it
  if (imagePath.startsWith('http')) return imagePath
  
  // Handle /assets/news/ paths
  if (imagePath.startsWith('/assets/news/')) {
    const filename = imagePath.replace('/assets/news/', '')
    try {
      return new URL(`../assets/${filename}`, import.meta.url).href
    } catch (e) {
      console.warn('Image not found:', filename)
      return ''
    }
  }
  
  return imagePath
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return date.toLocaleDateString('en-US', options)
}

const loadMore = () => {
  displayLimit.value += 6
}

const subscribe = () => {
  if (email.value && email.value.includes('@')) {
    alert('Thank you for subscribing!')
    email.value = ''
  } else {
    alert('Please enter a valid email address')
  }
}

const loadNewsData = () => {
  try {
    // Load news from JSON file
    if (Array.isArray(newsData)) {
      // Sort by date (newest first)
      allArticles.value = [...newsData].sort((a, b) => {
        return new Date(b.date_published) - new Date(a.date_published)
      })
    } else {
      console.error('News data is not an array')
      allArticles.value = []
    }
  } catch (error) {
    console.error('Error loading news data:', error)
    allArticles.value = []
  } finally {
    loading.value = false
  }
}

// Lifecycle
onMounted(() => {
  loadNewsData()
})
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>