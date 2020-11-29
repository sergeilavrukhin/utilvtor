import Vue from 'vue';
import VueMeta from 'vue-meta';
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

// switch between locales
numeral.locale('ru');

Vue.filter('formatSumm', (value) => numeral(value).format('0,0.00'));

Vue.config.productionTip = false;
Vue.use(VueMeta);
Vue.use(BootstrapVue);
Vue.use(VueInputMask);
Vue.use(require('vue-moment'));

Vue.prototype.$http_token = HTTP_TOKEN;
Vue.prototype.$http = HTTP;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
