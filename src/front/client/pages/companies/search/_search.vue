<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/companies">Компании</b-link>
        <span> &raquo; </span>
        <h1>Поиск по утилизаторам</h1>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col-md-8">
        <companies :companies="companies" :nofp="nofp"></companies>
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
    var search = encodeURI(params.search);
    var url = `companies/search/${search}`;
    if(params.region) {
      url = url + `/region/${params.region}`;
    }
    if(params.activity) {
      url = url + `/activity/${params.activity}`;
    }
    if(params.page) {
      url = url + `/page/${params.page}`;
    }
    const region_one = await $axios.$get(url).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    if(region_one) {
      const companies = region_one.companies;
      const nofp = region_one.count;
      const region = region_one.region;
      return { companies, nofp, region }
    }
  },
  data() {
    return {
      title: 'Поиск организаций по запросу занимающиеся утилизацией, хранением, переработкой, транспортировкой, обезвреживанием, захоронением отходов, покупкой и продажей вторсырья',
      companies: null,
      nofp: 10,
      region_name: null,
      activity: null,
      activities: {
        null: '',
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
      title: `Поиск организаций по запросу: ${this.$route.params.search}  ${this.activities[this.activity]}  ${this.region_name} занимающиеся утилизацией, хранением, переработкой, транспортировкой, обезвреживанием, захоронением отходов, покупкой и продажей вторсырья`,
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
