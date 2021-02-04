import Vue from 'vue'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
  apiKey: 'f2d34977-882f-4222-89dd-813e281a9401',
  lang: 'ru_RU',
  coordorder: 'latlong',
  version: '2.1',
} // настройки плагина

Vue.use(YmapPlugin, settings);
