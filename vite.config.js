import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath } from 'node:url'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  build: {
    rollupOptions: {
      output: {
        // Disable hashing for asset files (images, fonts, etc.)
        assetFileNames: (assetInfo) => {
          const info = assetInfo.name.split('.')
          const ext = info[info.length - 1]
          
          // Keep assets in assets folder without hash
          if (/png|jpe?g|svg|gif|tiff|bmp|ico|webp/i.test(ext)) {
            return `assets/[name].[ext]`
          }
          return `assets/[name].[ext]`
        },
        // Disable hashing for JavaScript chunks (you can keep this for cache busting if needed)
        chunkFileNames: 'assets/[name]-[hash].js',
        // Disable hashing for entry files
        entryFileNames: 'assets/[name]-[hash].js',
      }
    }
  }
})