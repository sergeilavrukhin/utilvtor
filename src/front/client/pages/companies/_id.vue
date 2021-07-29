<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/companies">Компании</b-link>
        <span> &raquo; </span>
        <b-link class="text-success" :href="`/companies/region/${company.region.url}`">{{ company.region.text }}</b-link>
        <span> &raquo; </span>
        <span class="uppercase">{{company.name}}</span>
      </b-col>
    </b-row>
    <br />
    <center><h1>{{company.name}} {{this.company.region.text}} (ИНН: {{this.company.itn}})</h1></center>
    <div class="row">
      <div class="col-md-4 p-4" style="width: 100%; height: 300px;">
        <img :src="`https://static-maps.yandex.ru/1.x/?ll=${company.gps.lat},${company.gps.long}&amp;z=10&amp;l=map&amp;size=300,250`">
      </div>
      <div class="col-md-8">
        <b-card class="mt-3 mb-3" title="Контакты">
          <b-card-text>
            <ul>
              <li v-if="company.locality">Адрес:{{company.locality}}</li>
              <li v-if="!company.locality">Адрес: Нет данных</li>
              <li>ИНН: {{company.itn}}</li>

              <li v-if="company.phones">Телефоны: {{company.phones.join(', ')}}</li>
              <li v-if="!company.phones">Телефоны: Нет данных</li>

              <li v-if="company.emails">Электронная почта: {{company.emails.join(', ')}}</li>
              <li v-if="!company.emails">Электронная почта: Нет данных</li>

              <li v-if="company.site">Сайт: <a :href="`/companies/link/${encode(company.site.join(', '))}/company/${company.id}`">{{company.site.join(', ')}}</a></li>
              <li v-if="!company.site">Сайт: Нет данных</li>
            </ul>
            <i>*В случае если контакты некорректны, просим сообщить нам об этом на электронную почту: <a href="mailto:info@webothod.ru">info@webothod.ru</a></i>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8">
        <b-card v-for="(item, index) in codes" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <i>Код ФККО: {{item.fkko.id}} | {{item.fkko.codespace}}</i>
            <a :href="`/code/${item.fkko.id}`" class="text-dark"><h2>{{item.fkko.name}}</h2></a>
            <ul class="activity" v-if="item.activity">
              <li v-for="(c_item, c_index) in item.activity" :key="c_index">
              <a :href="`/companies/search/${item.fkko.id}/activity/${c_item}`">{{getActivity(activities, c_item)}}</a>
              </li>
            </ul>
          </b-card-text>
        </b-card>
      </div>
      <div class="col-md-4">
        <queryadd></queryadd>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const company = await $axios.$get(`companies/${params.id}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const codes = await $axios.$get(`companies/fkkolist/${params.id}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const coords = [company.gps.long, company.gps.lat];
    return { company, coords, codes }
  },
  data() {
    return {
      company: null,
      coords: null,
      codes: null,
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвреживание',
        transportation: 'Транспортировка',
        utilization: 'Утилизация',
        disposal: 'Захоронение',
      },
    };
  },
  head() {
    return {
      title: `Компания ${this.company.name} из региона ${this.company.region.text} (ИНН: ${this.company.itn}) | утилизация, хранение, переработка, транспортирование, обезвреживание, захоронение отходов, покупка и продажа вторсырья`,
      meta: [
        { hid: 'description', name: 'description',
          content: `Компания ${this.company.name} из региона ${this.company.region.text} (ИНН: ${this.company.itn}) занимается утилизацией, хранением, переработкой, транспортированием, обезвреживанием, захоронением отходов, покупкой и продажей вторсырья так же вы можете найти другие компании по всем регионам России`,
        }
      ],
    }
  },
  methods: {
    getActivity: (activities, val) => activities[val],
    encode(uri) {
      return encodeURIComponent(uri)
    },
    async getContacts(type) {
      await this.$axios.$get(`companies/${this.company.id}/contacts/${type}/`).then((response) => {
        if (type == 'locality') {
          this.company.locality = response.data;
        }
        if (type == 'phones') {
          this.company.phones = response.data;
        }
        if (type == 'emails') {
          this.company.emails = response.data;
        }
        if (type == 'site') {
          this.company.site = response.data;
        }
      }).catch((error) => {
        console.log(error);
      });
    },
  },
};
</script>

<style>
h1 {
  font-size: 16px;
  text-transform: uppercase;
}

h2 {
  font-size: 15px;
  text-transform: uppercase;
}

.uppercase {
  text-transform: uppercase;
}

a {
    color: #28a745;
}

.activity{
  clear: both;
  padding: 0px;
  margin: 0px;
}
.activity li {
  float: left;
  list-style-type: none;
  padding: 5px;
  margin: 2px;
  border: 1px solid #ccc;
}
</style>