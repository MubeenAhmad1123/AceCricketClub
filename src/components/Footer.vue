<template>
  <footer
    class="relative bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-gray-300 overflow-hidden"
  >
    <!-- Decorative Top Border with Animation -->
    <div
      class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-red-500 to-transparent"
    ></div>

    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute inset-0"
        style="
          background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAxMCAwIEwgMCAwIDAgMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg==');
          background-size: 40px 40px;
        "
      ></div>
    </div>

    <!-- Decorative Elements -->
    <div
      class="absolute top-10 right-10 w-64 h-64 bg-red-500/10 rounded-full blur-3xl"
    ></div>
    <div
      class="absolute bottom-10 left-10 w-64 h-64 bg-red-500/10 rounded-full blur-3xl"
    ></div>

    <div class="relative z-10">
      <!-- Main Footer Content -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
        <div
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-12"
        >
          <!-- Brand Section - Takes more space -->
          <div class="lg:col-span-5">
            <!-- Logo and Title -->
            <div class="flex items-center space-x-3 mb-5">
              <div class="relative flex-shrink-0">
                <div
                  class="absolute inset-0 bg-red-500 rounded-xl blur-md opacity-50"
                ></div>
                <div
                  class="relative w-14 h-14 rounded-full flex items-center justify-center transform group-hover:scale-110 group-hover:rotate-12 transition-all duration-300 shadow-lg overflow-hidden ring-2 ring-red-500/50 group-hover:ring-red-400"
                >
                  <img
                    src="/src/assets/ace.webp"
                    alt="Ace Cricket Club logo"
                    class="w-full h-full object-cover"
                  />
                </div>
              </div>
              <div>
                <h3
                  class="text-white font-black text-2xl tracking-tight leading-tight"
                >
                  Ace Cricket Club
                </h3>
                <p
                  class="text-red-400 text-xs font-semibold uppercase tracking-wider mt-0.5"
                >
                  Est. 2010
                </p>
              </div>
            </div>

            <!-- Description -->
            <p class="text-gray-400 text-base leading-relaxed mb-8 max-w-md">
              Building champions on and off the field. Join us in our journey to
              excellence in cricket and witness the making of legends.
            </p>

            <!-- Newsletter Signup -->
            <div class="mb-8">
              <h4
                class="text-white font-semibold text-sm uppercase tracking-wider mb-4"
              >
                Stay Updated
              </h4>
              <div class="flex gap-2">
                <input
                  type="email"
                  placeholder="Enter your email"
                  class="flex-1 px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white text-sm placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                />
                <button
                  class="px-6 py-3 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white font-semibold rounded-lg transition-all transform hover:scale-105 shadow-lg flex-shrink-0"
                >
                  <svg
                    class="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M14 5l7 7m0 0l-7 7m7-7H3"
                    />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Social Media -->
            <div>
              <h4
                class="text-white font-semibold text-sm uppercase tracking-wider mb-4"
              >
                Connect With Us
              </h4>
              <div class="flex gap-3">
                <!-- Twitter/X -->
                <a
                  href="https://x.com/MubeenAhmad112"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group w-11 h-11 bg-slate-800 rounded-lg flex items-center justify-center hover:bg-red-500 transition-all duration-300 transform hover:scale-110 hover:-translate-y-1 flex-shrink-0"
                >
                  <svg
                    class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
                    />
                  </svg>
                </a>

                <!-- Instagram -->
                <a
                  href="https://www.instagram.com/mubeenahmad533/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group w-11 h-11 bg-slate-800 rounded-lg flex items-center justify-center hover:bg-red-500 transition-all duration-300 transform hover:scale-110 hover:-translate-y-1 flex-shrink-0"
                >
                  <svg
                    class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"
                    />
                  </svg>
                </a>

                <!-- Facebook -->
                <a
                  href="https://web.facebook.com/profile.php?id=61577200874318"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group w-11 h-11 bg-slate-800 rounded-lg flex items-center justify-center hover:bg-red-500 transition-all duration-300 transform hover:scale-110 hover:-translate-y-1 flex-shrink-0"
                >
                  <svg
                    class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"
                    />
                  </svg>
                </a>

                <!-- LinkedIn -->
                <a
                  href="https://www.linkedin.com/in/mubeen-ahmad-frontend/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group w-11 h-11 bg-slate-800 rounded-lg flex items-center justify-center hover:bg-red-500 transition-all duration-300 transform hover:scale-110 hover:-translate-y-1 flex-shrink-0"
                >
                  <svg
                    class="w-5 h-5 text-gray-400 group-hover:text-white transition-colors"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
                    />
                  </svg>
                </a>
              </div>
            </div>
          </div>

          <!-- Quick Links -->
          <div class="lg:col-span-2">
            <h4
              class="text-white font-bold text-base mb-6 uppercase tracking-wider"
            >
              Quick Links
            </h4>
            <ul class="space-y-3.5">
              <li>
                <router-link
                  to="/"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Home</span>
                </router-link>
              </li>
              <li>
                <router-link
                  to="/team"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Our Team</span>
                </router-link>
              </li>
              <li>
                <router-link
                  to="/fixtures"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Fixtures</span>
                </router-link>
              </li>
              <li>
                <router-link
                  to="/news"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">News</span>
                </router-link>
              </li>
              <li>
                <router-link
                  to="/contact"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Contact</span>
                </router-link>
              </li>
            </ul>
          </div>

          <!-- Resources -->
          <div class="lg:col-span-2">
            <h4
              class="text-white font-bold text-base mb-6 uppercase tracking-wider"
            >
              Resources
            </h4>
            <ul class="space-y-3.5">
              <li>
                <a
                  href="/#about"
                  @click="scrollToSection('about')"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">About Us</span>
                </a>
              </li>
              <li>
                <router-link
                  to="/contact"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Membership</span>
                </router-link>
              </li>
              <li>
                <router-link
                  to="/news"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Gallery</span>
                </router-link>
              </li>
              <li>
               <router-link
                    to="/partners"
                  @click="scrollToSection('Sponsors')"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Sponsors</span>
              </router-link>
              </li>
              <li>
                <router-link
                  to="/contact"
                  class="group inline-flex items-center text-gray-400 hover:text-red-500 transition-colors duration-200 no-underline"
                >
                  <span
                    class="w-1.5 h-1.5 bg-red-500 rounded-full mr-3 transform group-hover:scale-150 transition-transform"
                  ></span>
                  <span class="no-underline">Careers</span>
                </router-link>
              </li>
            </ul>
          </div>

          <!-- Contact Info -->
          <div class="lg:col-span-3">
            <h4
              class="text-white font-bold text-base mb-6 uppercase tracking-wider"
            >
              Get In Touch
            </h4>
            <ul class="space-y-4">
              <li class="flex items-start group">
                <div
                  class="w-10 h-10 bg-red-500/10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0 group-hover:bg-red-500/20 transition-colors"
                >
                  <svg
                    class="w-5 h-5 text-red-500"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                  </svg>
                </div>
                <div>
                  <p
                    class="text-xs text-gray-500 font-medium uppercase tracking-wide mb-1"
                  >
                    Address
                  </p>
                  <p class="text-gray-300 text-sm">
                    Faisalabad, Punjab,<br />Pakistan
                  </p>
                </div>
              </li>
              <li class="flex items-start group">
                <div
                  class="w-10 h-10 bg-red-500/10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0 group-hover:bg-red-500/20 transition-colors"
                >
                  <svg
                    class="w-5 h-5 text-red-500"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                    />
                  </svg>
                </div>
                <div>
                  <p
                    class="text-xs text-gray-500 font-medium uppercase tracking-wide mb-1"
                  >
                    Email
                  </p>
                  <a
                    href="mailto:info@acecricket.com"
                    class="text-gray-300 text-sm hover:text-red-500 transition-colors"
                    >info@acecricket.com</a
                  >
                </div>
              </li>
              <li class="flex items-start group">
                <div
                  class="w-10 h-10 bg-red-500/10 rounded-lg flex items-center justify-center mr-3 flex-shrink-0 group-hover:bg-red-500/20 transition-colors"
                >
                  <svg
                    class="w-5 h-5 text-red-500"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                    />
                  </svg>
                </div>
                <div>
                  <p
                    class="text-xs text-gray-500 font-medium uppercase tracking-wide mb-1"
                  >
                    Phone
                  </p>
                  <a
                    href="tel:+923218492868"
                    class="text-gray-300 text-sm hover:text-red-500 transition-colors"
                    >+92 3218492868</a
                  >
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t border-slate-800/50 backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div
            class="flex flex-col md:flex-row justify-between items-center gap-4"
          >
            <p class="text-gray-400 text-sm">
              &copy; {{ currentYear }}
              <span class="text-white font-semibold">Ace Cricket Club</span>.
              All rights reserved.
            </p>
            <div class="flex flex-wrap justify-center gap-6 text-sm">
              <a
                href="#"
                class="text-gray-400 hover:text-white transition-colors"
                >Privacy Policy</a
              >
              <span class="text-gray-700">|</span>
              <a
                href="#"
                class="text-gray-400 hover:text-white transition-colors"
                >Terms of Service</a
              >
              <span class="text-gray-700">|</span>
              <a
                href="#"
                class="text-gray-400 hover:text-white transition-colors"
                >Cookie Policy</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";

const currentYear = computed(() => new Date().getFullYear());
const router = useRouter();

const scrollToSection = (sectionId) => {
  // If not on home page, navigate to home first
  if (router.currentRoute.value.path !== "/") {
    router.push("/").then(() => {
      setTimeout(() => {
        const element = document.getElementById(sectionId);
        if (element) {
          element.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }, 100);
    });
  } else {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
};
</script>

<style scoped>
/* Remove all underlines from links */
a,
a:hover,
a:focus,
a:active {
  text-decoration: none !important;
}

/* Ensure proper alignment */
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  display: block;
}

/* Smooth link transitions */
a {
  display: inline-flex;
  align-items: center;
}
</style>
