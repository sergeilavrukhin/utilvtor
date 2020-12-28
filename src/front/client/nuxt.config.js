const axios = require('axios')

export default {
  mode: process.env.MODE,
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Биржа отходов Веботход.ру - утилизация отходов, покупка и продажа вторсырья',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Биржа отходов Веботход.ру - утилизация, обезвреживание, переработка, транспортирование отходов, покупка и продажа вторсырья' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    [
      '@nuxtjs/yandex-metrika',
      {
        id: '70796944',
        webvisor: true,
        // clickmap:true,
        // useCDN:false,
        // trackLinks:true,
        // accurateTrackBounce:true,
      }
    ],
    '@nuxtjs/gtm',
    '@nuxtjs/sitemap',
  ],

  gtm: {
    id: 'G-V4VL08V30N',
  },

  axios: {
    baseURL: process.env.AXIOS_URL
    // proxy: true
  },

  sitemap: {
    hostname: process.env.BASE_URL,
    gzip: true,
    exclude: [
      '/companies/**',
      '/user/**'
    ],
    routes: async () => {
      const { data } = await axios.get(process.env.BASE_URL + '/api/client/code/map')
      return data.map((code) => `/code/${code.id}`)
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
  }
}
