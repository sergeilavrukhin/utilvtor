<template>
  <b-container>
    <navbar></navbar>
    <search></search>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
        <h1>{{ title }}</h1>
        <h4>{{ subtitle }}</h4>
      </b-col>
    </b-row>
    <hr class="my-4">
    <b-row>
      <b-col class="col-md-8">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <ul v-for="(item, index) in codes" :key="index">
            <li><b-link class="text-success" :href="`/code/${item.id}`">
            {{item.id}}</b-link> - {{item.name}}</li>
          </ul>
          </b-card-text>
        </b-card>
      </b-col>
      <b-col class="col-md-4">
        <queryadd :region="region" :query_type="query_type"></queryadd>
      </b-col>
    </b-row>
    <cmp-footer></cmp-footer>
  </b-container>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const codes = await $axios.$get('code/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    const query_type = await $axios.$get('queries/query_types/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const region = await $axios.$get('regions/list/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { query_type, region, codes }
  },
  data() {
    return {
      loggedIn: this.$auth.loggedIn,
      title: 'Блоки кодов ФККО',
      region: null,
      query_type: null,
      subtitle: 'Классификация осуществляется по нескольким признакам, оцениваемым в совокупности: происхождению, \
      агрегатному состоянию, степени вредного воздействия и опасным свойствам.',
      description: 'В Федеральном Классификационном Каталоге Отходов (ФККО) вы можете найти необходимую информацию по каждому виду отходов.',
    };
  },
  head() {
    return {
      title: this.title,
      meta: [
        { hid: 'description', name: 'description', content: this.description }
      ],
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
