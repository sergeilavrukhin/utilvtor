<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <div class="row">
      <div class="col-md-8">
        <b-card v-for="(item, index) in region" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <a :href="`companies/region/${item.url}`" class="text-dark"><h2>{{item.text}}</h2></a>
            <i>Актуальное количество фирм, которое занимается обращением с отходами</i>
            <ul class="activity" v-if="item.activity">
              <li v-for="(c_item, c_index) in item.activity" :key="c_index">
              {{getActivity(activities, c_index)}}: {{c_item}}
              </li>
            </ul>
            <h6 class="mt-2">Статистика по отходам в регионе <span>{{item.text}}</span></h6>
          </b-card-text>
        </b-card>
      </div>
      <div class="col-md-4">
        <queryadd :region="region" :query_type="query_type"></queryadd>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const query_type = await $axios.$get('queries/query_types/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const region = await $axios.$get('regions/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { query_type, region }
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      region: null,
      query_type: null,
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
      title: this.title,
    }
  },
  methods: {
    getActivity: (activities, val) => activities[val],
  },
};
</script>

<style>
.activity{
  clear: both;
  padding: 0px;
  margin: 0px;
}
.activity li {
  list-style-type: none;
  padding: 5px;
  margin: 2px;
  border: 1px solid #ccc;
}
</style>
