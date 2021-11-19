<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
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
    var url = `companies`;
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
      return { companies, nofp }
    }
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием, захоронением, хранением отходов, покупкой и продажей вторсырья',
      companies: null,
      nofp: 10,
    };
  },
  head() {
    return {
      title: this.title,
    }
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
