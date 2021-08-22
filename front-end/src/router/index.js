import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home')
  },
  {
    path: '/login ',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "about" */ '../views/Register.vue')
  },
  {
    path: '/collect' ,
    name: 'Collect' ,
    component: () => import('../views/CollectingQuestionnaire')
  },
  {
    path: '/create',
    name: 'create',
    component: () => import(/* webpackChunkName: "about" */ '../views/CreatingQuestionnaire.vue')
  },
  {
    path: '/bin' ,
    name: 'Bin' ,
    component: () => import('../views/Bin')
  },
  {
    path: '/info',
    name: 'Info',
    component: () => import(/* webpackChunkName: "about" */ '../views/Information.vue')
  },
  {
    path: '/sentout',
    name: 'SentOut',
    component: () => import(/* webpackChunkName: "about" */ '../views/SentOut.vue')
  },
  {
    path: '/result',
    name: 'Result',
    component: () => import(/* webpackChunkName: "about" */ '../views/Result.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
