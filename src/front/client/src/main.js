import Vue from 'vue';
import VueMeta from 'vue-meta';
import YmapPlugin from 'vue-yandex-maps';
import VueYandexMetrika from 'vue-yandex-metrika';
import VueAnalytics from 'vue-analytics';
import { BootstrapVue } from 'bootstrap-vue';
import HTTP_TOKEN from './axios_token';
import HTTP from './axios';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './css/style.css';
import '@fortawesome/fontawesome-free/css/all.css';

const VueInputMask = require('vue-inputmask').default;

const numeral = require('numeral');
// load a locale
numeral.register('locale', 'ru', {
  delimiters: {
    thousands: ' ',
    decimal: ',',
  },
});

const YmapSettings = {
  apiKey: 'f2d34977-882f-4222-89dd-813e281a9401',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1',
};

// switch between locales
numeral.locale('ru');

Vue.filter('formatSumm', (value) => numeral(value).format('0,0.00'));

Vue.config.productionTip = false;
Vue.use(VueMeta);
Vue.use(BootstrapVue);
Vue.use(VueInputMask);
Vue.use(YmapPlugin, YmapSettings);
Vue.use(VueAnalytics, {
  id: 'UA-173361984-1',
  router,
});
Vue.use(VueYandexMetrika, {
  id: 63012667,
  router,
  env: process.env.NODE_ENV,
});
Vue.use(require('vue-moment'));

Vue.prototype.$http_token = HTTP_TOKEN;
Vue.prototype.$http = HTTP;

const Navbar = () => import(/* webpackChunkName: "navbar" */'./components/Navbar.vue');
Vue.component('navbar', Navbar);

const Footer = () => import(/* webpackChunkName: "cmp-footer" */'./components/Footer.vue');
Vue.component('cmp-footer', Footer);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
