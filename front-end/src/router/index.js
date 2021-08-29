import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)

}
const routes = [
    {
        path: '/c',
        name: 'xx',
        component: () => import(/* webpackChunkName: "about" */ '../components/HelloWorld')
    },
    {
        path: '/',
        component: () => import(/* webpackChunkName: "about" */ '../views/main')
    },
    {
        path: '/test',
        name: 'Test',
        component: () => import(/* webpackChunkName: "about" */ '../views/examQuestionnaire')
    },
    {
        path: '/home',
        name: 'Home',
        component: () => import(/* webpackChunkName: "about" */ '../views/Home')
    },
    {
        path: '/login',
        name: 'Login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
    },
    {
        path: '/login2',
        name: 'Login2',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Login_SignUp.vue')
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import(/* webpackChunkName: "about" */ '../views/Register.vue')
    },
    {
        path: '/collectingQuestionnaire',
        name: 'Collect',
        component: () => import('../views/CollectingQuestionnaire')
    },
    {
        path: '/collectingQuestionnaire2',
        name: 'CollectSignUp',
        component: () => import('../views/CollectingSignUpQuestionnaire')
    },
    {
        path: '/bin',
        name: 'Bin',
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
    },
    {
        path: '/creatingQuestionnaire',
        name: 'CreatingQuestionnaire',
        component: () => import('../views/CreatingQuestionnaire')
    },
    {
        path: '/showVoteResult',
        name: 'ShowVoteResult',
        component: () => import('../views/ShowVoteResult')
    },
    {
        path: '/successResult',
        name: 'SuccessResult',
        component: () => import('../views/successResult')
    },
    {
        path: '/failedResult',
        name: 'FailedResult',
        component: () => import('../views/failedResult')
    },
    {
        path: '/failedResult2',
        name: 'FailedResult2',
        component: () => import('../views/failedResult_SignUpQ')
    },
    {
        path: '/failedResult3',
        name: 'FailedResult3',
        component: () => import('../views/failedResult_SignUpQ2')
    },
    {
        path: '/endResult',
        name: 'EndResult',
        component: () => import('../views/endResult')
    }
]

const router = new VueRouter({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    if (to.path === '/') return next();
    // if (to.path === '/register') return next();
    // if (to.path === '/CollectingQuestionnaire') return next();
    // const tokenStr = this.$cookies.get('username')
    // console.log(tokenStr)
    // if (tokenStr === '') return next('/')
    // if (tokenStr&&to.path === '/register') return next('/home')
    // if (tokenStr&&to.path === '/login') return next('/home')
    next()
})

export default router
