import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueCookies from 'vue-cookies'
import ElementUI from 'element-ui';
import * as vuedraggable from "vuedraggable";
import 'element-ui/lib/theme-chalk/index.css';
import JsonExcel from 'vue-json-excel'

Vue.component('downloadExcel', JsonExcel)
import htmlToPdf from './components/HtmlToPdf'

Vue.use(htmlToPdf)
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(vuedraggable);
Vue.prototype.$axios = axios

Vue.use(VueCookies)
axios.defaults.baseURL="http://35.229.157.90:8000/";

new Vue({
  axios,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
