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
          :to="`/code/${item.code}`">{{item.name}}</router-link> &raquo;
        </span> <h1>{{code.name}}</h1>
      </b-col>
    </b-row>
    <hr class="my-4">
    <b-row>
      <b-col v-if="code" class="pb-4 col-md-8">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <h2 v-if="!children.length">Отход (код фкко: {{code.code}} | {{code.code_space}}) - {{code.name}}</h2>
          <h2 v-if="children.length > 0">Категория отхода (код: {{code.code}} | {{code.code_space}}) - {{code.name}}
           в себе содержит:</h2>
          <h4 v-if="code.category">{{code.category.id}} класс опасности отхода</h4>
          <i v-if="code.category">{{code.category.text}}</i>
          <h4 v-if="code.aggregation">Агрегатное состояние и физические формы отхода</h4>
          <i v-if="code.aggregation">{{ code.aggregation.text }}</i>
          <ul v-for="(item, index) in children" :key="index">
            <li><b-link class="text-success" :href="`/code/${item.code}`">
            {{item.code}} | {{item.code_space}}</b-link> - {{item.name}}</li>
          </ul>
          <h4 v-if="code.keywords">Под этим кодом вы можете утилизировать такие отходы:</h4>
          <i v-if="code.keywords">{{code.keywords}}</i>
          </b-card-text>
        </b-card>
        <h2>Компании работающие с данным видом отходов:</h2>
        <a v-if="companies" :href="`/companies/search/${this.$route.params.code}`" class="text-success uppercase">Посмотреть все компании</a>
        <companies v-if="companies" :companies="companies" nofp="0"></companies>
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
    const code = await $axios.$get(`waste_codes/code/${params.code}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    const children = await $axios.$get(`waste_codes/children/${params.code}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    /*const companies = await $axios.$get(`companies/by_code/${params.code}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });*/
    const companies = null;
    return { code, children, companies }
  },
  data() {
    return {
      code: null,
      children: [],
      companies: [],
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
      title: `Отход ${this.code.name} | код фкко ${this.code.code} ${this.code.code_space} утилизация, переработка, хранение, транспортирование, обезвреживание, захоронение отходов, покупка и продажа вторсырья`,
      meta: [
        { hid: 'description', name: 'description',
          content: `На нашей бирже отходов вы сможете найти где утилизировать, обезвредить, хранить, обезвредить, захоронить отход, купить или продать вторсырье такое как ${this.code.name} код фкко ${this.code.code} | ${this.code.code_space}, а так же найти подрядчика в виде транспортной компании для сбора и вывоза, всего лишь в несколько кликов!`,
        }
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
