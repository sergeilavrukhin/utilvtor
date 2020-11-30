import Vue from 'vue';
import VueRouter from 'vue-router';

const Front = () => import(/* webpackChunkName: "front" */'../views/Front.vue');
const Cabinet = () => import(/* webpackChunkName: "front" */'../views/Cabinet.vue');
const Code = () => import(/* webpackChunkName: "front" */'../views/Code.vue');
const Utilisation = () => import(/* webpackChunkName: "front" */'../views/Utilisation.vue');
const Create = () => import(/* webpackChunkName: "front" */'../views/Create.vue');
const Login = () => import(/* webpackChunkName: "front" */'../views/Login.vue');
const Request = () => import(/* webpackChunkName: "front" */'../views/Request.vue');
Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Front },
    { path: '/code/', component: Code },
    { path: '/utilisation/', component: Utilisation },
    { path: '/create/', component: Create },
    { path: '/login/', component: Login },
    { path: '/logout/', component: Front },
    { path: '/cabinet/', component: Cabinet },
    { path: '/request/', component: Request },
  ],
});
