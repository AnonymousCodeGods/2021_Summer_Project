import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueCookies from 'vue-cookies'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.prototype.$http = axios
Vue.use(VueCookies)
axios.defaults.baseURL="http://172.16.1.26:8000/";

new Vue({
  axios,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
