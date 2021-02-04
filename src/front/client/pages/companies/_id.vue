<template>
  <div class="container">
    <navbar></navbar>
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
              <li>Контактное лицо: Нет данных</li>
              <li>Телефон: Нет данных</li>
              <li>Электронная почта: Нет данных</li>
              <li>Сайт: Нет данных</li>
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
    console.log(coords);
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
</style>
