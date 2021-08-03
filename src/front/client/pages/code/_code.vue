<template>
  <b-container>
    <navbar></navbar>
    <search></search>
    <b-row>
      <b-col v-if="code" class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/code">Блоки кодов ФККО</b-link>
        <span> &raquo; </span>
        <span v-for="(item, index) in code.breadcrumb" :key="index">
        <router-link class="text-success"
        :to="`/code/${item.id}`">{{item.name}}</router-link> &raquo;
        </span> <h1>{{code.fkko.name}}</h1>
      </b-col>
    </b-row>
    <hr class="my-4">
    <b-row>
      <b-col v-if="code.fkko" class="pb-4 col-md-8">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <h2 v-if="code.fkko.fkkoclass">Отход (код фкко: {{code.fkko.id}} | {{code.fkko.codespace}}) - {{code.fkko.name}}</h2>
          <h2 v-if="!code.fkko.fkkoclass">Категория отхода (код: {{code.fkko.id}} | {{code.fkko.codespace}}) - {{code.fkko.name}}
           в себе содержит:</h2>
          <h4 v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.id}} класс опасности отхода</h4>
          <i v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.text}}</i>
          <h4 v-if="code.fkko.aggr">Агрегатное состояние и физические формы отхода</h4>
          <i v-if="code.fkko.aggr">{{ code.fkko.aggr.text }}</i>
          <ul v-for="(item, index) in code.codes" :key="index">
            <li><b-link class="text-success" :href="`/code/${item.id}`">
            {{item.id}} | {{item.codespace}}</b-link> - {{item.name}}</li>
          </ul>
          <h4 v-if="code.fkko.keywords">Под этим кодом вы можете утилизировать такие отходы:</h4>
          <i v-if="code.fkko.keywords">{{code.fkko.keywords}}</i>
          </b-card-text>
        </b-card>
        <h2>Компании работающие с данным видом отходов:</h2>
        <a v-if="companies" :href="`/companies/search/${this.$route.params.code}`" class="text-success uppercase">Посмотреть все компании</a>
        <companies :companies="companies" nofp="0"></companies>
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
  async asyncData({ params, $axios }) {
    const code = await $axios.$get(`code/${params.code}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    const companies = await $axios.$get(`companies/byfkko/${params.code}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { code, companies }
  },
  data() {
    return {
      code: null,
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвреживание',
        transportation: 'Транспортировка',
        utilization: 'Утилизация',
        disposal: 'Захоронение',
      },
    }
  },
  head() {
    return {
      companies: null,
      title: `Отход ${this.code.fkko.name} | код фкко ${this.code.fkko.id} ${this.code.fkko.codespace} утилизация, переработка, хранение, транспортирование, обезвреживание, захоронение отходов, покупка и продажа вторсырья`,
      meta: [
        { hid: 'description', name: 'description',
          content: `На нашей бирже отходов вы сможете найти где утилизировать, обезвредить, хранить, обезвредить, захоронить отход, купить или продать вторсырье такое как ${this.code.fkko.name} код фкко ${this.code.fkko.id} | ${this.code.fkko.codespace}, а так же найти подрядчика в виде транспортной компании для сбора и вывоза, всего лишь в несколько кликов!`,
        }
      ],
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

.uppercase {
  text-transform: uppercase;
}

.activity{
  clear: both;
  padding: 0px;
  margin: 0px;
}
.activity li {
  float: left;
  list-style-type: none;
  padding: 5px;
  margin: 2px;
  border: 1px solid #ccc;
}
</style>
