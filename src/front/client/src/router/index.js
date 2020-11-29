import Vue from 'vue';
import VueRouter from 'vue-router';

const Front = () => import(/* webpackChunkName: "front" */'../views/Front.vue');
Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Front },
  ],
});
