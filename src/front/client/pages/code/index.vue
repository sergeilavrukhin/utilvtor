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
        <queryadd></queryadd>
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
    return { codes }
  },
  data() {
    return {
      title: 'Блоки кодов ФККО',
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
