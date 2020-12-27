import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from '@nuxt/ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _2aa76b8e = () => interopDefault(import('../pages/code/index.vue' /* webpackChunkName: "pages/code/index" */))
const _9250b7a0 = () => interopDefault(import('../pages/companies/index.vue' /* webpackChunkName: "pages/companies/index" */))
const _7877430a = () => interopDefault(import('../pages/queries/index.vue' /* webpackChunkName: "pages/queries/index" */))
const _4aa6d562 = () => interopDefault(import('../pages/companies/area/index.vue' /* webpackChunkName: "pages/companies/area/index" */))
const _14a0a0c0 = () => interopDefault(import('../pages/companies/city/index.vue' /* webpackChunkName: "pages/companies/city/index" */))
const _badcd3e6 = () => interopDefault(import('../pages/queries/add/index.vue' /* webpackChunkName: "pages/queries/add/index" */))
const _0f30147b = () => interopDefault(import('../pages/user/signin/index.vue' /* webpackChunkName: "pages/user/signin/index" */))
const _d5658b1e = () => interopDefault(import('../pages/user/signup/index.vue' /* webpackChunkName: "pages/user/signup/index" */))
const _76d20d14 = () => interopDefault(import('../pages/code/_id.vue' /* webpackChunkName: "pages/code/_id" */))
const _493e1ad0 = () => interopDefault(import('../pages/companies/_id.vue' /* webpackChunkName: "pages/companies/_id" */))
const _a78478ba = () => interopDefault(import('../pages/queries/_id.vue' /* webpackChunkName: "pages/queries/_id" */))
const _5bf263e4 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/code",
    component: _2aa76b8e,
    name: "code"
  }, {
    path: "/companies",
    component: _9250b7a0,
    name: "companies"
  }, {
    path: "/queries",
    component: _7877430a,
    name: "queries"
  }, {
    path: "/companies/area",
    component: _4aa6d562,
    name: "companies-area"
  }, {
    path: "/companies/city",
    component: _14a0a0c0,
    name: "companies-city"
  }, {
    path: "/queries/add",
    component: _badcd3e6,
    name: "queries-add"
  }, {
    path: "/user/signin",
    component: _0f30147b,
    name: "user-signin"
  }, {
    path: "/user/signup",
    component: _d5658b1e,
    name: "user-signup"
  }, {
    path: "/code/:id",
    component: _76d20d14,
    name: "code-id"
  }, {
    path: "/companies/:id",
    component: _493e1ad0,
    name: "companies-id"
  }, {
    path: "/queries/:id",
    component: _a78478ba,
    name: "queries-id"
  }, {
    path: "/",
    component: _5bf263e4,
    name: "index"
  }],

  fallback: false
}

function decodeObj(obj) {
  for (const key in obj) {
    if (typeof obj[key] === 'string') {
      obj[key] = decode(obj[key])
    }
  }
}

export function createRouter () {
  const router = new Router(routerOptions)

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    const r = resolve(to, current, append)
    if (r && r.resolved && r.resolved.query) {
      decodeObj(r.resolved.query)
    }
    return r
  }

  return router
}
