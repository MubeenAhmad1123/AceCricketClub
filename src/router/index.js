// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// Lazy-load views for better initial performance
const Home = () => import("../views/Home.vue");
const Team = () => import("../views/Team.vue");
const Fixtures = () => import("../views/Fixtures.vue");
const News = () => import("../views/News.vue");
const Article = () => import("../views/Article.vue");
const Contact = () => import("../views/Contact.vue");
const Facilities = () => import("../views/Facilities.vue");
const SuccessStories = () => import("../views/Testimonials.vue");
const Coaches = () => import("../views/Coaches.vue");
const Programs = () => import("../views/program.vue");
const PartnersView = () => import("../views/partner.vue"); // renamed to avoid duplicate identifier

const routes = [
  { 
    path: "/", 
    name: "Home", 
    component: Home,
    meta: { title: "Home — Ace Cricket Club" }
  },
  { 
    path: "/team", 
    name: "Team", 
    component: Team,
    meta: { title: "Team — Ace Cricket Club" }
  },
  { 
    path: "/programs", 
    name: "Programs", 
    component: Programs,
    meta: { title: "Programs — Ace Cricket Club" }
  },
  { 
    path: "/partners", 
    name: "PartnersSection", 
    component: PartnersView,
    meta: { title: "Sponsors — Ace Cricket Club" }
  },
  { 
    path: "/fixtures", 
    name: "Fixtures", 
    component: Fixtures,
    meta: { title: "Fixtures — Ace Cricket Club" }
  },
  {
    path: "/news",
    name: "News",
    component: News,
    meta: { title: "News — Ace Cricket Club" }
  },
  {
    // Dynamic route: same Article component renders all articles based on slug
    path: "/news/:slug",
    name: "Article",
    component: Article,
    props: true,
    meta: { title: "Article — Ace Cricket Club" }
  },
  {
    path: "/facilities",
    name: "Facilities",
    component: Facilities,
    meta: { title: "Facilities — Ace Cricket Club" }
  },
  {
    path: "/success-stories",
    name: "SuccessStories",
    component: SuccessStories,
    meta: { title: "Success Stories — Ace Cricket Club" }
  },
  {
    path: "/coaches",
    name: "Coaches",
    component: Coaches,
    meta: { title: "Coaches — Ace Cricket Club" }
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
    meta: { title: "Contact Us — Ace Cricket Club" }
  },
  // Catch-all fallback -> redirect to home
  { 
    path: "/:catchAll(.*)", 
    redirect: "/" 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    return { top: 0, behavior: 'smooth' };
  }
});

router.afterEach((to) => {
  const DEFAULT = "Ace Cricket Club";
  if (to.meta && to.meta.title) {
    document.title = to.meta.title;
  } else {
    document.title = DEFAULT;
  }
});

export default router;
