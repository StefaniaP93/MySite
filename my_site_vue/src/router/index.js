import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MyProjects from '../views/MyProjects.vue'
import Project from '../views/Project.vue'
import Contatti from '../views/Contatti.vue'

const routes = [
  {
    path: '/projects/:project_slug/',
    name: 'Project',
    component: Project
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/projects',
    name: 'MyProjects',
    component: MyProjects
  },
  {
    path: '/contatti',
    name: 'Contatti',
    component: Contatti
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
