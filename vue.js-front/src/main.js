import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import VueI18n from 'vue-i18n'
import Vuelidate from 'vuelidate';

import App from './App.vue';
//import router from './router';

import translations from "./resources/translation";


Vue.use(VueI18n);
Vue.use(Vuelidate);
Vue.config.productionTip = false;
//Vue.config.formApiUrl = process.env.FORM_API_URL;

const i18n = new VueI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: translations
})

new Vue({
  el: '#app',
  i18n,
  render: h => h(App)
})