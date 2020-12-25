<template>
  <div class="container">
    <navbar></navbar>
    <h2>Заявки</h2>
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
      title: 'Заявки',
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
};
</script>
