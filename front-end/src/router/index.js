import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/info',
        name: 'Info',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Information.vue')
    },
    {
        path: '/bin',
        name: 'bin',
        component: () => import(/* webpackChunkName: "about" */ '../views/Bin.vue')
    },
    {
        path: '/create',
        name: 'create',
        component: () => import(/* webpackChunkName: "about" */ '../views/CreatingQuestionnaire.vue')
    },
    {
        path: '/collect',
        name: 'collect',
        component: () => import(/* webpackChunkName: "about" */ '../views/CollectingQuestionnaire.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
