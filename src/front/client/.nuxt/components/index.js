export { default as CmpFooter } from '../../components/cmp-footer.vue'
export { default as Navbar } from '../../components/navbar.vue'

export const LazyCmpFooter = import('../../components/cmp-footer.vue' /* webpackChunkName: "components/cmp-footer" */).then(c => c.default || c)
export const LazyNavbar = import('../../components/navbar.vue' /* webpackChunkName: "components/navbar" */).then(c => c.default || c)
