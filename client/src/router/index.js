import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import MovieDetatilView from '../views/MovieDetailView.vue'
import RegistrationView from '../views/RegistrationView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movie/:id',
      name: 'movie-detail',
      component: MovieDetatilView
    },
    {
      path: '/registration/',
      name: 'registration',
      component: RegistrationView
    },
  ]
})

export default router
