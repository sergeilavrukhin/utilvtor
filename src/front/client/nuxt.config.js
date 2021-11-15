const axios = require('axios');

export default {
  mode: process.env.MODE,
  publicRuntimeConfig: {
    baseURL: process.env.BASE_URL,
  },
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Биржа отходов Веботход.ру - утилизация, хранение, переработка, транспортирование, обезвреживание, захоронение отходов, покупка и продажа вторсырья',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Биржа отходов Веботход.ру - утилизация, хранение, переработка, транспортирование, обезвреживание, захоронение отходов, покупка и продажа вторсырья' }
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
    '@plugins/v-mask',
    '@plugins/v-autocomplete'
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
    '@nuxtjs/auth-next',
  ],

  axios: {
    baseURL: process.env.AXIOS_URL
    // proxy: true
  },

  auth: {
    redirect: {
      login: '/user/signin',
      logout: '/',
      callback: '/user/signin',
      home: '/'
    },
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access_token',
          maxAge: 1800,
          // type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh_token',
          data: 'refresh_token',
          maxAge: 60 * 60 * 24 * 30
        },
        user: {
          property: 'user',
         // autoFetch: true
        },
        endpoints: {
          login: { url: '/user/sign-in/', method: 'post' },
          refresh: { url: '/user/refresh/', method: 'post' },
          user: { url: '/user/', method: 'get' },
          logout: { url: '/user/logout/', method: 'post' }
        },
        // autoLogout: false
      },
    },
    fullPathRedirect: true
  },

  sitemap: {
    hostname: process.env.BASE_URL,
    gzip: true,
    exclude: [
      '/companies/**',
      '/user/**'
    ],
    routes: async () => {
      var { data_codes } = await axios.get(process.env.BASE_URL + '/api/client/code/map');
      var maps = data_codes.map((code) => `/code/${code.id}`);

      var { data_query } = await axios.get(process.env.BASE_URL + '/api/client/queries/map');
      var queries = data_query.map((query) => `/queries/${query.id}`);
      maps = maps.concat(queries);

      var { data_companies } = await axios.get(process.env.BASE_URL + '/api/client/companies/map');
      var companies = data_companies.map((query) => `/companies/${query.id}`);
      maps = maps.concat(companies);

      var { data_regions } = await axios.get(process.env.BASE_URL + '/api/client/companies/region/map');
      var companies_region = data_regions.map((query) => `/companies/region/${query.url}`);
      maps = maps.concat(companies_region);


      var { data_activities } = await axios.get(process.env.BASE_URL + '/api/client/companies/region/activity/map');
      var companies_activities = data_activities.map((query) => `/companies/region/${query.url}/activity/${query.activity}`);
      maps = maps.concat(companies_activities);


      var { data_search_codes } = await axios.get(process.env.BASE_URL + '/api/client/companies/search/map');
      var search_codes = data_search_codes.map((code) => `/companies/search/${code.id}`);
      maps = maps.concat(search_codes);

      var { data_search_activity } = await axios.get(process.env.BASE_URL + '/api/client/companies/search/activity/map');
      var search_codes_activity = data_search_activity.map((code) => `/companies/search/${code.id}/activity/${code.activity}`);
      maps = maps.concat(search_codes_activity);

      return maps;
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
  }
};
