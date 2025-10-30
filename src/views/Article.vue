<template>
  <div class="article-page">
    <!-- Skeleton Loader -->
    <div v-if="loading" class="skeleton-loader">
      <div class="container">
        <div class="skeleton-hero"></div>
        <div class="skeleton-content">
          <div class="skeleton-line"></div>
          <div class="skeleton-line"></div>
          <div class="skeleton-line short"></div>
        </div>
      </div>
    </div>

    <!-- Article Not Found -->
    <div v-else-if="!article" class="not-found">
      <div class="container">
        <h1>Article Not Found</h1>
        <p>Sorry, we couldn't find the article you're looking for.</p>
        <router-link to="/news" class="back-link">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M12.5 5L7.5 10L12.5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          Back to News
        </router-link>
      </div>
    </div>

    <!-- Article Content -->
    <article v-else class="article">
      <!-- Hero Section -->
      <header class="hero">
        <div class="hero-container">
          <figure class="hero-image">
            <img 
              :src="getImagePath(article.image)" 
              :alt="article.image_alt"
              loading="eager"
              @error="handleImageError"
            />
          </figure>
          <div class="hero-content">
            <nav class="breadcrumb">
              <router-link to="/news" class="back-link">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                  <path d="M12.5 5L7.5 10L12.5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Back to News
              </router-link>
            </nav>
            <span class="category-badge">{{ article.category }}</span>
            <h1 class="title">{{ article.title }}</h1>
            <div class="meta">
              <time :datetime="article.date_published" class="date">
                {{ formatDate(article.date_published) }}
              </time>
              <span class="separator">•</span>
              <span class="author">{{ article.author.name }}</span>
              <span class="separator">•</span>
              <span class="reading-time">{{ article.reading_time_minutes }} min read</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Main Content -->
      <div class="article-body">
        <!-- Sticky Share Bar (Desktop) -->
        <aside class="share-sidebar" aria-label="Share options">
          <button 
            @click="shareArticle" 
            class="share-btn"
            aria-label="Share article"
            title="Share"
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M15 6.667C16.3807 6.667 17.5 5.54769 17.5 4.167C17.5 2.78631 16.3807 1.667 15 1.667C13.6193 1.667 12.5 2.78631 12.5 4.167C12.5 5.54769 13.6193 6.667 15 6.667Z" stroke="currentColor" stroke-width="1.5"/>
              <path d="M5 12.5C6.38071 12.5 7.5 11.3807 7.5 10C7.5 8.61929 6.38071 7.5 5 7.5C3.61929 7.5 2.5 8.61929 2.5 10C2.5 11.3807 3.61929 12.5 5 12.5Z" stroke="currentColor" stroke-width="1.5"/>
              <path d="M15 18.333C16.3807 18.333 17.5 17.2137 17.5 15.833C17.5 14.4523 16.3807 13.333 15 13.333C13.6193 13.333 12.5 14.4523 12.5 15.833C12.5 17.2137 13.6193 18.333 15 18.333Z" stroke="currentColor" stroke-width="1.5"/>
              <path d="M7.15833 11.2583L12.85 14.575" stroke="currentColor" stroke-width="1.5"/>
              <path d="M12.8417 5.42505L7.15833 8.74172" stroke="currentColor" stroke-width="1.5"/>
            </svg>
          </button>
          <button 
            @click="copyLink" 
            class="share-btn"
            aria-label="Copy link"
            title="Copy link"
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M8.33333 10.8333C8.69101 11.3118 9.14771 11.7077 9.67187 11.9948C10.196 12.2819 10.7764 12.4537 11.3721 12.4988C11.9679 12.5439 12.5667 12.4612 13.1279 12.2561C13.6891 12.051 14.2005 11.7282 14.6283 11.31L17.1283 8.80999C17.9323 7.97739 18.3776 6.86544 18.3681 5.71061C18.3586 4.55578 17.8951 3.45161 17.0773 2.63176C16.2594 1.81192 15.1559 1.34581 14.0011 1.33363C12.8463 1.32145 11.7337 1.76419 10.9 2.56666L9.36667 4.09166" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M11.6667 9.16667C11.309 8.68824 10.8523 8.29235 10.3281 8.00524C9.80398 7.71814 9.22361 7.54631 8.62786 7.50121C8.0321 7.45611 7.43334 7.53876 6.87213 7.74387C6.31091 7.94898 5.79952 8.27184 5.37167 8.69L2.87167 11.19C2.06769 12.0226 1.62238 13.1346 1.63187 14.2894C1.64135 15.4442 2.10483 16.5484 2.92268 17.3682C3.74052 18.1881 4.84406 18.6542 5.99888 18.6664C7.1537 18.6786 8.26627 18.2358 9.1 17.4333L10.625 15.9083" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span v-if="linkCopied" class="copied-tooltip">Copied!</span>
          </button>
          <button 
            @click="saveArticle" 
            class="share-btn"
            :aria-label="isSaved ? 'Article saved' : 'Save article'"
            :title="isSaved ? 'Saved' : 'Save'"
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M15.8333 17.5L10 13.3333L4.16667 17.5V4.16667C4.16667 3.72464 4.34226 3.30072 4.65482 2.98816C4.96738 2.67559 5.39131 2.5 5.83333 2.5H14.1667C14.6087 2.5 15.0326 2.67559 15.3452 2.98816C15.6577 3.30072 15.8333 3.72464 15.8333 4.16667V17.5Z" :fill="isSaved ? 'currentColor' : 'none'" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
          <button 
            @click="printArticle" 
            class="share-btn"
            aria-label="Print article"
            title="Print"
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M5 7.5V2.5H15V7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M5 15H3.33333C2.89131 15 2.46738 14.8244 2.15482 14.5118C1.84226 14.1993 1.66667 13.7754 1.66667 13.3333V9.16667C1.66667 8.72464 1.84226 8.30072 2.15482 7.98816C2.46738 7.67559 2.89131 7.5 3.33333 7.5H16.6667C17.1087 7.5 17.5326 7.67559 17.8452 7.98816C18.1577 8.30072 18.3333 8.72464 18.3333 9.16667V13.3333C18.3333 13.7754 18.1577 14.1993 17.8452 14.5118C17.5326 14.8244 17.1087 15 16.6667 15H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M5 12.5H15V17.5H5V12.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </aside>

        <!-- Content Column -->
        <main class="content">
          <div class="excerpt">{{ article.excerpt }}</div>

          <!-- Mobile Share Buttons -->
          <div class="mobile-share">
            <button @click="shareArticle" class="mobile-share-btn">
              <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
                <path d="M15 6.667C16.3807 6.667 17.5 5.54769 17.5 4.167C17.5 2.78631 16.3807 1.667 15 1.667C13.6193 1.667 12.5 2.78631 12.5 4.167C12.5 5.54769 13.6193 6.667 15 6.667Z" stroke="currentColor" stroke-width="1.5"/>
                <path d="M5 12.5C6.38071 12.5 7.5 11.3807 7.5 10C7.5 8.61929 6.38071 7.5 5 7.5C3.61929 7.5 2.5 8.61929 2.5 10C2.5 11.3807 3.61929 12.5 5 12.5Z" stroke="currentColor" stroke-width="1.5"/>
                <path d="M15 18.333C16.3807 18.333 17.5 17.2137 17.5 15.833C17.5 14.4523 16.3807 13.333 15 13.333C13.6193 13.333 12.5 14.4523 12.5 15.833C12.5 17.2137 13.6193 18.333 15 18.333Z" stroke="currentColor" stroke-width="1.5"/>
                <path d="M7.15833 11.2583L12.85 14.575" stroke="currentColor" stroke-width="1.5"/>
                <path d="M12.8417 5.42505L7.15833 8.74172" stroke="currentColor" stroke-width="1.5"/>
              </svg>
              Share
            </button>
            <button @click="copyLink" class="mobile-share-btn">
              <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
                <path d="M8.33333 10.8333C8.69101 11.3118 9.14771 11.7077 9.67187 11.9948C10.196 12.2819 10.7764 12.4537 11.3721 12.4988C11.9679 12.5439 12.5667 12.4612 13.1279 12.2561C13.6891 12.051 14.2005 11.7282 14.6283 11.31L17.1283 8.80999C17.9323 7.97739 18.3776 6.86544 18.3681 5.71061C18.3586 4.55578 17.8951 3.45161 17.0773 2.63176C16.2594 1.81192 15.1559 1.34581 14.0011 1.33363C12.8463 1.32145 11.7337 1.76419 10.9 2.56666L9.36667 4.09166" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M11.6667 9.16667C11.309 8.68824 10.8523 8.29235 10.3281 8.00524C9.80398 7.71814 9.22361 7.54631 8.62786 7.50121C8.0321 7.45611 7.43334 7.53876 6.87213 7.74387C6.31091 7.94898 5.79952 8.27184 5.37167 8.69L2.87167 11.19C2.06769 12.0226 1.62238 13.1346 1.63187 14.2894C1.64135 15.4442 2.10483 16.5484 2.92268 17.3682C3.74052 18.1881 4.84406 18.6542 5.99888 18.6664C7.1537 18.6786 8.26627 18.2358 9.1 17.4333L10.625 15.9083" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ linkCopied ? 'Copied!' : 'Copy' }}
            </button>
            <button @click="saveArticle" class="mobile-share-btn">
              <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
                <path d="M15.8333 17.5L10 13.3333L4.16667 17.5V4.16667C4.16667 3.72464 4.34226 3.30072 4.65482 2.98816C4.96738 2.67559 5.39131 2.5 5.83333 2.5H14.1667C14.6087 2.5 15.0326 2.67559 15.3452 2.98816C15.6577 3.30072 15.8333 3.72464 15.8333 4.16667V17.5Z" :fill="isSaved ? 'currentColor' : 'none'" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              {{ isSaved ? 'Saved' : 'Save' }}
            </button>
          </div>

          <!-- Content Blocks -->
          <div class="content-blocks" v-if="article.content_blocks && article.content_blocks.length">
            <component 
              v-for="(block, index) in article.content_blocks" 
              :key="index"
              :is="getBlockComponent(block.type)"
              v-bind="getBlockProps(block)"
            />
          </div>

          <!-- Fallback to HTML content -->
          <div v-else-if="article.content_html" class="content-html" v-html="sanitizeHtml(article.content_html)"></div>

          <!-- CTA -->
          <div v-if="article.cta" class="cta">
            <a :href="article.cta.url" class="cta-button">{{ article.cta.text }}</a>
          </div>

          <!-- Tags -->
          <div v-if="article.tags && article.tags.length" class="tags">
            <span class="tags-label">Tags:</span>
            <span v-for="tag in article.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>

          <!-- Navigation -->
          <nav class="article-nav">
            <router-link 
              v-if="previousArticle" 
              :to="`/news/${previousArticle.slug}`" 
              class="nav-link prev"
            >
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M12.5 5L7.5 10L12.5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <div>
                <span class="nav-label">Previous</span>
                <span class="nav-title">{{ previousArticle.title }}</span>
              </div>
            </router-link>
            <router-link 
              v-if="nextArticle" 
              :to="`/news/${nextArticle.slug}`" 
              class="nav-link next"
            >
              <div>
                <span class="nav-label">Next</span>
                <span class="nav-title">{{ nextArticle.title }}</span>
              </div>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M7.5 15L12.5 10L7.5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </router-link>
          </nav>

          <!-- Related Articles -->
          <section v-if="relatedArticles.length" class="related-articles">
            <h2>Related Articles</h2>
            <div class="related-grid">
              <router-link 
                v-for="related in relatedArticles" 
                :key="related.slug"
                :to="`/news/${related.slug}`"
                class="related-card"
              >
                <img 
                  :src="getImagePath(related.image)" 
                  :alt="related.image_alt"
                  loading="lazy"
                  @error="handleImageError"
                />
                <div class="related-content">
                  <span class="related-category">{{ related.category }}</span>
                  <h3>{{ related.title }}</h3>
                  <p>{{ related.excerpt }}</p>
                </div>
              </router-link>
            </div>
          </section>
        </main>
      </div>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import newsData from '@/data/news.json'

const props = defineProps({
  slug: String
})

const route = useRoute()
const loading = ref(true)
const linkCopied = ref(false)
const isSaved = ref(false)

const activeSlug = computed(() => props.slug || route.params.slug)

const article = computed(() => {
  if (!activeSlug.value) return null
  return newsData.find(a => a.slug === activeSlug.value)
})

const articleIndex = computed(() => {
  if (!article.value) return -1
  return newsData.findIndex(a => a.slug === article.value.slug)
})

const previousArticle = computed(() => {
  if (articleIndex.value > 0) {
    return newsData[articleIndex.value - 1]
  }
  return null
})

const nextArticle = computed(() => {
  if (articleIndex.value >= 0 && articleIndex.value < newsData.length - 1) {
    return newsData[articleIndex.value + 1]
  }
  return null
})

const relatedArticles = computed(() => {
  if (!article.value) return []
  
  let related = []
  
  if (article.value.related_slugs && article.value.related_slugs.length) {
    related = article.value.related_slugs
      .map(slug => newsData.find(a => a.slug === slug))
      .filter(Boolean)
      .slice(0, 3)
  }
  
  if (related.length < 3) {
    const additional = newsData
      .filter(a => a.slug !== article.value.slug && a.category === article.value.category)
      .filter(a => !related.some(r => r.slug === a.slug))
      .slice(0, 3 - related.length)
    related = [...related, ...additional]
  }
  
  return related.slice(0, 3)
})

const placeholderImage = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"%3E%3Crect fill="%23e5e7eb" width="1200" height="630"/%3E%3Ctext x="50%25" y="50%25" font-family="Arial" font-size="24" fill="%239ca3af" text-anchor="middle" dominant-baseline="middle"%3EImage%3C/text%3E%3C/svg%3E'

// FIXED: Image path handler
const getImagePath = (imagePath) => {
  if (!imagePath) {
    console.warn('No image path provided')
    return placeholderImage
  }
  
  // If it's already a full URL, return it
  if (imagePath.startsWith('http')) {
    return imagePath
  }
  
  // Handle /assets/news/ paths
  if (imagePath.startsWith('/assets/news/')) {
    const filename = imagePath.replace('/assets/news/', '')
    try {
      // Import the image from assets folder
      return new URL(`../assets/${filename}`, import.meta.url).href
    } catch (e) {
      console.error('Image import failed:', filename, e)
      return placeholderImage
    }
  }
  
  // If it's just /assets/something.webp
  if (imagePath.startsWith('/assets/')) {
    const filename = imagePath.replace('/assets/', '')
    try {
      return new URL(`../assets/${filename}`, import.meta.url).href
    } catch (e) {
      console.error('Image import failed:', filename, e)
      return placeholderImage
    }
  }
  
  // Last resort: treat as filename
  try {
    return new URL(`../assets/${imagePath}`, import.meta.url).href
  } catch (e) {
    console.error('Image loading failed:', imagePath, e)
    return placeholderImage
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

const handleImageError = (e) => {
  console.error('Image failed to load:', e.target.src)
  e.target.src = placeholderImage
}

const shareArticle = async () => {
  const shareData = {
    title: article.value.title,
    text: article.value.excerpt,
    url: window.location.href
  }
  
  if (navigator.share) {
    try {
      await navigator.share(shareData)
    } catch (err) {
      if (err.name !== 'AbortError') {
        console.warn('Share failed:', err)
      }
    }
  } else {
    const twitter = `https://twitter.com/intent/tweet?text=${encodeURIComponent(article.value.title)}&url=${encodeURIComponent(window.location.href)}`
    window.open(twitter, '_blank', 'width=600,height=400')
  }
}

const copyLink = async () => {
  const url = window.location.href
  
  try {
    await navigator.clipboard.writeText(url)
    linkCopied.value = true
    setTimeout(() => {
      linkCopied.value = false
    }, 2000)
  } catch (err) {
    console.warn('Copy failed:', err)
  }
}

const saveArticle = () => {
  const savedArticles = JSON.parse(localStorage.getItem('savedArticles') || '[]')
  const index = savedArticles.indexOf(article.value.slug)
  
  if (index > -1) {
    savedArticles.splice(index, 1)
    isSaved.value = false
  } else {
    savedArticles.push(article.value.slug)
    isSaved.value = true
  }
  
  localStorage.setItem('savedArticles', JSON.stringify(savedArticles))
}

const printArticle = () => {
  window.print()
}

const checkSavedStatus = () => {
  if (!article.value) return
  const savedArticles = JSON.parse(localStorage.getItem('savedArticles') || '[]')
  isSaved.value = savedArticles.includes(article.value.slug)
}

const sanitizeHtml = (html) => {
  if (!html) return ''
  return html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
}

const getBlockComponent = (type) => {
  const components = {
    'p': 'p',
    'h2': 'h2',
    'blockquote': 'blockquote',
    'ul': 'ul',
    'ol': 'ol',
    'img': 'figure'
  }
  return components[type] || 'div'
}

const getBlockProps = (block) => {
  if (block.type === 'img') {
    return {
      innerHTML: `<img src="${block.src}" alt="${block.alt}" loading="lazy" />`
    }
  }
  
  if (block.type === 'ul' || block.type === 'ol') {
    return {
      innerHTML: block.items.map(item => `<li>${item}</li>`).join('')
    }
  }
  
  if (block.text) {
    return {
      textContent: block.text
    }
  }
  
  return {}
}

const updateMetaTags = () => {
  if (!article.value) return
  
  document.title = article.value.seo_title || article.value.title
  
  const updateMeta = (name, content) => {
    let meta = document.querySelector(`meta[name="${name}"]`)
    if (!meta) {
      meta = document.createElement('meta')
      meta.name = name
      document.head.appendChild(meta)
    }
    meta.content = content
  }
  
  const updateOgMeta = (property, content) => {
    let meta = document.querySelector(`meta[property="${property}"]`)
    if (!meta) {
      meta = document.createElement('meta')
      meta.setAttribute('property', property)
      document.head.appendChild(meta)
    }
    meta.content = content
  }
  
  updateMeta('description', article.value.meta_description)
  
  if (article.value.og) {
    updateOgMeta('og:title', article.value.og.title)
    updateOgMeta('og:description', article.value.og.description)
    updateOgMeta('og:image', article.value.og.image)
    updateOgMeta('og:url', window.location.href)
    updateOgMeta('og:type', 'article')
  }
  
  if (article.value.twitter_card) {
    updateMeta('twitter:card', article.value.twitter_card.card)
    updateMeta('twitter:title', article.value.twitter_card.title)
    updateMeta('twitter:description', article.value.twitter_card.description)
    updateMeta('twitter:image', article.value.twitter_card.image)
  }
}

onMounted(() => {
  setTimeout(() => {
    loading.value = false
    checkSavedStatus()
    updateMetaTags()
  }, 300)
})

watch(() => activeSlug.value, () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    checkSavedStatus()
    updateMetaTags()
    window.scrollTo(0, 0)
  }, 300)
})
</script>

<style scoped>
/* Critical styles */
.article-page {
  min-height: 100vh;
  background: #ffffff;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.skeleton-loader {
  padding: 4rem 0;
}

.skeleton-hero {
  height: 400px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
}

.skeleton-content {
  max-width: 800px;
  margin: 0 auto;
}

.skeleton-line {
  height: 1rem;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  border-radius: 0.25rem;
  margin-bottom: 0.75rem;
}

.skeleton-line.short {
  width: 60%;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.not-found {
  padding: 6rem 0;
  text-align: center;
}

.not-found h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #111827;
}

.not-found p {
  font-size: 1.125rem;
  color: #6b7280;
  margin-bottom: 2rem;
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #ef4444;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.2s;
}

.back-link:hover {
  opacity: 0.8;
}

.hero {
  background: #f9fafb;
  padding: 2rem 0;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 1024px) {
  .hero-container {
    grid-template-columns: 1fr 1fr;
    align-items: center;
  }
}

.hero-image {
  margin: 0;
  order: 2;
}

.hero-image img {
  width: 100%;
  height: auto;
  max-height: 500px;
  object-fit: cover;
  border-radius: 0.5rem;
}

.hero-content {
  order: 1;
}

@media (min-width: 1024px) {
  .hero-image {
    order: 1;
  }
  
  .hero-content {
    order: 2;
  }
}

.breadcrumb {
  margin-bottom: 1rem;
}

.category-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: #ef4444;
  color: white;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.25rem;
  margin-bottom: 1rem;
}

.title {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.2;
  color: #111827;
  margin: 0 0 1rem 0;
}

@media (max-width: 768px) {
  .title {
    font-size: 1.875rem;
  }
}

.meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  color: #6b7280;
  font-size: 0.875rem;
  align-items: center;
}

.separator {
  color: #d1d5db;
}

.article-body {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 1rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  position: relative;
}

@media (min-width: 1024px) {
  .article-body {
    grid-template-columns: 60px 1fr;
    gap: 3rem;
  }
}

.share-sidebar {
  display: none;
  position: sticky;
  top: 2rem;
  height: fit-content;
  flex-direction: column;
  gap: 0.75rem;
}

@media (min-width: 1024px) {
  .share-sidebar {
    display: flex;
  }
}

.share-btn {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
}

.share-btn:hover {
  background: #f9fafb;
  color: #ef4444;
  border-color: #ef4444;
}

.copied-tooltip {
  position: absolute;
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 0.5rem;
  padding: 0.25rem 0.5rem;
  background: #111827;
  color: white;
  font-size: 0.75rem;
  border-radius: 0.25rem;
  white-space: nowrap;
}

.content {
  max-width: 800px;
  margin: 0 auto;
  width: 100%;
}

.excerpt {
  font-size: 1.25rem;
  line-height: 1.75;
  color: #4b5563;
  margin-bottom: 2rem;
  font-weight: 500;
}

.mobile-share {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

@media (min-width: 1024px) {
  .mobile-share {
    display: none;
  }
}

.mobile-share-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.875rem;
}

.mobile-share-btn:hover {
  background: #f9fafb;
  color: #ef4444;
  border-color: #ef4444;
}

.content-blocks > * {
  margin-bottom: 1.5rem;
}

.content-blocks p {
  font-size: 1.125rem;
  line-height: 1.75;
  color: #374151;
}

.content-blocks h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
}

.content-blocks blockquote {
  border-left: 4px solid #ef4444;
  padding-left: 1.5rem;
  margin: 2rem 0;
  font-size: 1.25rem;
  font-style: italic;
  color: #4b5563;
}

.content-blocks ul,
.content-blocks ol {
  padding-left: 1.5rem;
  font-size: 1.125rem;
  line-height: 1.75;
  color: #374151;
}

.content-blocks li {
  margin-bottom: 0.5rem;
}

.content-blocks figure {
  margin: 2rem 0;
}

.content-blocks figure img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
}

.content-html {
  font-size: 1.125rem;
  line-height: 1.75;
  color: #374151;
}

.content-html p {
  margin-bottom: 1.5rem;
}

.content-html h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
}

.content-html blockquote {
  border-left: 4px solid #ef4444;
  padding-left: 1.5rem;
  margin: 2rem 0;
  font-size: 1.25rem;
  font-style: italic;
  color: #4b5563;
}

.content-html ul,
.content-html ol {
  padding-left: 1.5rem;
  margin-bottom: 1.5rem;
}

.content-html li {
  margin-bottom: 0.5rem;
}

.content-html img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
  margin: 2rem 0;
}

.cta {
  margin: 3rem 0;
  padding: 2rem;
  background: #fef2f2;
  border-radius: 0.5rem;
  text-align: center;
}

.cta-button {
  display: inline-block;
  padding: 1rem 2rem;
  background: #ef4444;
  color: white;
  text-decoration: none;
  font-weight: 600;
  border-radius: 0.5rem;
  transition: background 0.2s;
}

.cta-button:hover {
  background: #dc2626;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 3rem 0;
  padding-top: 2rem;
  border-top: 1px solid #e5e7eb;
}

.tags-label {
  font-weight: 600;
  color: #6b7280;
}

.tag {
  padding: 0.25rem 0.75rem;
  background: #f3f4f6;
  color: #6b7280;
  font-size: 0.875rem;
  border-radius: 0.25rem;
}

.article-nav {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 3rem 0;
  padding: 2rem 0;
  border-top: 1px solid #e5e7eb;
  border-bottom: 1px solid #e5e7eb;
}

@media (min-width: 768px) {
  .article-nav {
    grid-template-columns: 1fr 1fr;
  }
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 0.5rem;
  text-decoration: none;
  transition: background 0.2s;
}

.nav-link:hover {
  background: #f3f4f6;
}

.nav-link.next {
  justify-content: flex-end;
  text-align: right;
}

.nav-label {
  display: block;
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
}

.nav-title {
  display: block;
  font-weight: 600;
  color: #111827;
}

.related-articles {
  margin: 4rem 0;
}

.related-articles h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 2rem;
}

.related-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .related-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.related-card {
  display: block;
  text-decoration: none;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.related-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.related-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.related-content {
  padding: 1.5rem;
}

.related-category {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  background: #fef2f2;
  color: #ef4444;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 0.25rem;
  margin-bottom: 0.75rem;
}

.related-card h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.related-card p {
  font-size: 0.875rem;
  color: #6b7280;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

@media print {
  .share-sidebar,
  .mobile-share,
  .article-nav,
  .related-articles,
  .back-link {
    display: none !important;
  }
  
  .hero-container {
    grid-template-columns: 1fr;
  }
  
  .article-body {
    grid-template-columns: 1fr;
  }
}
</style>