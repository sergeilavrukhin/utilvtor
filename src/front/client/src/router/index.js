import Vue from 'vue';
import VueRouter from 'vue-router';

const Front = () => import(/* webpackChunkName: "Front" */'../views/Front.vue');
const Cabinet = () => import(/* webpackChunkName: "Cabinet" */'../views/Cabinet.vue');
const Code = () => import(/* webpackChunkName: "Code" */'../views/Code.vue');
const Utilisation = () => import(/* webpackChunkName: "Utilisation" */'../views/Utilisation.vue');
const UtilisationArea = () => import(/* webpackChunkName: "UtilisationArea" */'../views/UtilisationArea.vue');
const UtilisationCity = () => import(/* webpackChunkName: "UtilisationCity" */'../views/UtilisationCity.vue');
const Create = () => import(/* webpackChunkName: "Create" */'../views/Create.vue');
const Login = () => import(/* webpackChunkName: "Login" */'../views/Login.vue');
const Request = () => import(/* webpackChunkName: "Request" */'../views/Request.vue');
const Queries = () => import(/* webpackChunkName: "Queries" */'../views/Queries.vue');
const Partner = () => import(/* webpackChunkName: "Partner" */'../views/Partner.vue');
Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Front },
    { path: '/code/', component: Code },
    { path: '/code/:id/', component: Code },
    { path: '/utilisation/', component: Utilisation },
    { path: '/utilisation/:area/', component: UtilisationArea },
    { path: '/utilisation/:area/:city/', component: UtilisationCity },
    { path: '/partner/:id/', component: Partner },
    { path: '/create/', component: Create },
    { path: '/login/', component: Login },
    { path: '/logout/', component: Front },
    { path: '/cabinet/', component: Cabinet },
    { path: '/request/', component: Request },
    { path: '/queries/', component: Queries },
  ],
});
