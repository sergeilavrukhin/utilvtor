<template>
  <b-container>
    <navbar></navbar>
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
      <b-button class="mr-2" v-if="!loggedIn" variant="outline-success" href="/user/signup">Зарегистрироваться</b-button>
      <b-button variant="success" href="/queries/add">Разместить заявку</b-button>
    <hr class="my-4">
    <b-row>
      <b-col v-if="code.fkko" class="p-4">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <h2 v-if="code.fkko.fkkoclass">Отход (код: {{code.fkko.id}}) - {{code.fkko.name}}</h2>
          <h2 v-if="!code.fkko.fkkoclass">Категория отхода (код: {{code.fkko.id}}) - {{code.fkko.name}}
           в себе содержит:</h2>
          <h4 v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.id}} класс опасности отхода</h4>
          <i v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.text}}</i>
          <h4 v-if="code.fkko.aggr">Агрегатное состояние и физические формы отхода</h4>
          <i v-if="code.fkko.aggr">{{ code.fkko.aggr.text }}</i>
          <ul v-for="(item, index) in code.codes" :key="index">
            <li><b-link class="text-success" :href="`/code/${item.id}`">
            {{item.id}}</b-link> - {{item.name}}</li>
          </ul>
          </b-card-text>
        </b-card>
     </b-col>
    </b-row>
    <b-row v-if="companies">
      <b-col align="center">
        <h2>Компании работающие с данным видом отходов:</h2>
      </b-col>
    </b-row>
    <b-row>
      <div v-for="(item, index) in companies" :key="index">
        <b-card class="m-5" v-if="item.company" style="width: 280px;">
          <b-card-text align="center">
            <img :src="`https://static-maps.yandex.ru/1.x/?ll=${item.company.gps.lat},${item.company.gps.long}&amp;z=10&amp;l=map&amp;size=240,160`">
            <br /><a :href="`/companies/${item.company.id}`" class="text-dark uppercase">{{item.company.name}}</a>
          </b-card-text>
        </b-card>
      </div>
    </b-row>
    <b-row v-if="companies">
      <b-col align="center">
        <a href="/companies" class="text-success uppercase">Посмотреть все компании</a>
      </b-col>
    </b-row>
    <cmp-footer></cmp-footer>
  </b-container>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const code = await $axios.$get(`code/${params.id}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    const companies = await $axios.$get(`companies/byfkko/${params.id}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { code, companies }
  },
  data() {
    return {
      loggedIn: this.$auth.loggedIn,
      code: null,
    }
  },
  head() {
    return {
      companies: null,
      title: `Утилизация ${this.code.fkko.name} | ${this.code.fkko.id} утилизация, транспортирование, обезвреживание, покупка и продажа`,
      meta: [
        { hid: 'description', name: 'description',
          content: `На нашей бирже отходов вы сможете утилизировать или обезвредить ${this.code.fkko.name}, а так же найти подрядчика в виде транспортной компании для сбора и вывоза, всего лишь в несколько кликов!`,
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
</style>
