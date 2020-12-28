<template>
  <div class="container">
    <navbar></navbar>
    <h1>{{ title }}</h1>
    <hr class="my-4">
      <b-button class="mr-2" variant="outline-success" href="/user/signup">Зарегистрироваться</b-button>
      <b-button variant="success" href="/queries/add">Разместить заявку</b-button>
    <hr class="my-4">
    <div class="row m-0">
      <div class="col-md-12">
        <b-card v-for="(item, index) in queries" :key="index"
        :title="item.waste" :sub-title="item.query_type.name"
        class="mx-1 my-3">
          <b-card-text>
            <ul>
              <li v-if="item.fkko"><b>Код отхода:</b> {{item.fkko.id}}</li>
              <li><b>Адрес:</b> {{item.locality}}</li>
              <li><b>Количество:</b> {{item.count}} {{item.unit.name}}</li>
              <li v-if="item.aggr"><b>Агрегатное состояние:</b> {{item.aggr.name}}</li>
            </ul>
          </b-card-text>
          <router-link :to="`${item.id}`" class="text-success">Посмотреть</router-link>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const queries = await $axios.$get('queries/').then((response) => {
      console.log(response);
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { queries }
  },
  data() {
    return {
      queries: null,
      title: 'Заявки на утилизацию, транспортирование, обезвреживание оходов, а так же покупку и продажу вторсырья',
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
