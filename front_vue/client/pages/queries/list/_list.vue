<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <h1>{{ title }}</h1>
    <div class="row m-0">
      <div class="col-md-8">
        <queries :queries="queries" :nofp="nofp"></queries>
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
  async asyncData({ $axios, params }) {
    var url = 'queries/';
    if(params.page) {
      url = url + `page/${params.page}/`;
    }
    const queries_obj = await $axios.$get(url).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    if(queries_obj) {
      const queries = queries_obj.queries;
      const nofp = queries_obj.count;
      return { queries, nofp }
    }
    return { queries }
  },
  data() {
    return {
      queries: null,
      nofp: 10,
      title: 'Заявки на утилизацию, транспортирование, обезвреживание оходов, а так же покупку и продажу вторсырья',
    };
  },
  head() {
    return {
      title: this.title,
    }
  },

  methods: {
  }
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
