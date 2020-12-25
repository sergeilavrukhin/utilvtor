<template>
  <div class="container">
    <navbar></navbar>
    <br />
    <center><h1>{{title}}</h1></center>
    <div class="row">
      <div class="col-md-12 p-4" style="width: 100%; height: 300px;">
        <yandex-map
          v-if="coords"
          :coords="coords"
          :zoom="10"
        >
          <ymap-marker
            :coords="coords"
            marker-id="123"
            hint-content="some hint"
          />
        </yandex-map>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card class="mt-3 mb-3" title="Контакты">
          <b-card-text>
            <ul>
              <li>Контактное лицо: Нет данных</li>
              <li>Телефон: Нет данных</li>
              <li>Электронная почта: Нет данных</li>
              <li>Сайт: Нет данных</li>
            </ul>
            <small>
              Вы можете зарегистрироваться, получить доступ к контактам и связаться
               с организацией самостоятельно.Либо разместить бесплатную заявку и утилизаторы,
               транспортные компании или покупатели вторсырья увидят ваше объявление и
               смогут откликнуться на него
            </small>
            <br />
            <center><b-button class="m-3" variant="outline-success" to="/create/">
              Зарегистрироваться
            </b-button>
            <h2>Оставьте заявку на обращение с отходами в {{title}}
             и другие похожие организации</h2>
              <b-button class="m-3" variant="success" to="/request/">Разместить заявку</b-button>
            </center>
          </b-card-text>
        </b-card>
        <b-card class="mt-3 mb-3" :title="`Лицензии на обработку отходов у ${title}`">
          <b-card-text>
            <ul v-for="(item, index) in codes" :key="index">
              <li><a class="text-success" :href="`/code/${item.id}/`">
              Код ФККО {{item.id}}</a><br />{{item.name}}</li>
            </ul>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'UtilisationArea',
  metaInfo() {
    return {
      title: this.title,
    };
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      companies: null,
      coords: null,
      codes: null,
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
  methods: {
    getActivity: (activities, val) => activities[val],
    async loadPartner() {
      await this.$http.get(`partner/${this.$route.params.id}/`).then((response) => {
        this.coords = [response.data.coords.long, response.data.coords.lat];
        this.title = response.data.entity;
        this.codes = response.data.codes;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  async created() {
    this.loadPartner();
  },
};
</script>
