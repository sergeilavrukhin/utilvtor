<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 pl-4 pr-4 pt-4">
        <router-link class="text-success" href="/queries/">Заявки</router-link>
        <span> &raquo; </span>
        <h1 v-if="item">{{item.query_type.name}} {{item.waste}} {{item.fkko.id}}</h1>
      </div>
    </div>
    <div class="row m-0">
      <div class="col-md-12">
        <b-card v-if="item" :sub-title="item.query_type.name"
        class="mx-1 my-3">
          <b-card-text>
            <ul>
              <li v-if="item.fkko"><b>Код отхода:</b> {{item.fkko.id}}</li>
              <li><b>Адрес:</b> {{item.locality}}</li>
              <li><b>Количество:</b> {{item.count}} {{item.unit.name}}</li>
              <li v-if="item.aggr"><b>Агрегатное состояние:</b> {{item.aggr.name}}</li>
              <li><b>Автор:</b> доступно после регистрации</li>
              <li><b>Телефон:</b> доступно после регистрации</li>
              <li><b>Email:</b> доступно после регистрации</li>
            </ul>
          </b-card-text>
        </b-card>
        <b-button class="mr-2" variant="outline-success" href="/user/signup/">Зарегистрироваться</b-button>
        <b-button variant="success" href="/queries/add/">Разместить заявку</b-button>
        <hr class="my-4">
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      item: null,
      contacts: null,
      title: 'Заявки',
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
  methods: {
    async loadPage() {
      /*await this.$http.get(`queries/${this.$route.params.id}`).then((response) => {
        this.item = response.data;
      }).catch((error) => {
        console.log(error);
      });*/
    },
  },
  async created() {
    this.loadPage();
  },
  watch: {
    $route(to, from) {
      if (to.params.id !== from.params.id) {
        this.loadPage();
      }
    },
  },
};
</script>
