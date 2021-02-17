<template>
  <div class="container">
    <navbar></navbar>
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
    <center><h1>{{company.name}}</h1></center>
    <div class="row">
      <div class="col-md-4 p-4" style="width: 100%; height: 300px;">
        <img :src="`https://static-maps.yandex.ru/1.x/?ll=${company.gps.lat},${company.gps.long}&amp;z=10&amp;l=map&amp;size=300,250`">
      </div>
      <div class="col-md-8 p-4">
        <b-card class="mt-3 mb-3" title="Контакты">
          <b-card-text>
            <ul>
              <li v-if="company.locality">Адрес:
                <span v-if="company.locality == 'reg'">Доступно после <a href="/user/signup/">регистрации</a></span>
                <span v-if="company.locality != 'reg'">{{company.locality}}</span>
              </li>
              <li v-if="!company.locality">Адрес: Нет данных</li>
              <li v-if="company.phones">Телефоны:
                <span v-if="company.phones == 'reg'">Доступно после <a href="/user/signup/">регистрации</a></span>
                <span v-if="company.phones != 'reg'">{{company.phones.join(', ')}}</span>
              </li>
              <li v-if="!company.phones">Телефоны: Нет данных</li>
              <li v-if="company.emails">Электронная почта:
                <span v-if="company.emails == 'reg'">Доступно после <a href="/user/signup/">регистрации</a></span>
                <span v-if="company.emails != 'reg'">{{company.emails.join(', ')}}</span>
              </li>
              <li v-if="!company.emails">Электронная почта: Нет данных</li>
              <li v-if="company.site">Сайт:
                <span v-if="company.site == 'reg'">Доступно после <a href="/user/signup/">регистрации</a></span>
                <span v-if="company.site != 'reg'">{{company.site}}</span>
              </li>
              <li v-if="!company.site">Сайт: Нет данных</li>
            </ul>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <b-card class="mt-3 mb-3">
          <b-card-text>
            <small>
              Вы можете зарегистрироваться, получить доступ к контактам и связаться
               с организацией самостоятельно.Либо разместить бесплатную заявку и утилизаторы,
               транспортные компании или покупатели вторсырья увидят ваше объявление и
               смогут откликнуться на него
            </small>
            <br />
            <center><b-button class="m-3" variant="outline-success" to="/user/signup">
              Зарегистрироваться
            </b-button>
            <h2>Оставьте заявку на обращение с отходами в {{company.name}}
             и другие похожие организации</h2>
              <b-button class="m-3" variant="success" to="/queries/add">Разместить заявку</b-button>
            </center>
          </b-card-text>
        </b-card>
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
    const coords = [company.gps.long, company.gps.lat];
    return { company, coords }
  },
  data() {
    return {
      company: null,
      coords: null,
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвереживание',
        transportation: 'Транспортировка',
        utilization: 'Утилизация',
        disposal: 'Захоронение',
      },
    };
  },
  head() {
    return {
      title: `${this.company.name}`,
    }
  },
  methods: {
    getActivity: (activities, val) => activities[val],
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
</style>
