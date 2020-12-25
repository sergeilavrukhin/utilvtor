<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card v-for="(item, index) in companies" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <a :href="`${item.uri}/`" class="text-dark"><h2>{{item.name}}</h2></a>
            <i>Актуальное количество фирм, которое занимается обращением с отходами</i>
            <ul class="activity">
              <li v-for="(c_item, c_index) in item.activity" :key="c_index">
              {{getActivity(activities, c_index)}}: {{c_item}}
              </li>
            </ul>
            <h6 class="mt-2">Статистика по отходам в регионе <span>{{item.name}}</span></h6>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'Utilisation',
  metaInfo() {
    return {
      title: this.title,
    };
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      companies: null,
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
    async loadCompanies() {
      await this.$http.get('companies/').then((response) => {
        this.companies = response.data.companies;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  async created() {
    this.loadCompanies();
  },
};
</script>
