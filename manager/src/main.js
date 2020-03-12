// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import router from './plugins/router'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
// main.js
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import axios from 'axios'

 Vue.prototype.$axios = axios;
Vue.use(axios);
Vue.use(Vuetify, {
  iconfont: 'md'
})

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
