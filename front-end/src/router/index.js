import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/collectingQuestionnaire' ,
    name: 'CollectingQuestionnaire' ,
    component: () => import('../views/CollectingQuestionnaire')
  },
  {
    path: '/creatingQuestionnaire' ,
    name: 'CreatingQuestionnaire' ,
    component: () => import('../views/CreatingQuestionnaire')
  },
  {
    path: '/showVoteResult' ,
    name: 'ShowVoteResult' ,
    component: () => import('../views/ShowVoteResult')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
