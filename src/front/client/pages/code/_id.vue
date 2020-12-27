<template>
  <b-container>
    <navbar></navbar>
    <b-row>
      <b-col v-if="code" class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/code">Блоки кодов ФККО</b-link>
        <span> &raquo; </span>
        <span v-for="(item, index) in code.breadcrumb" :key="index">
        <router-link class="text-success"
        :to="`/code/${item.id}/`">{{item.name}}</router-link> &raquo;
        </span> <h1>{{code.fkko.name}}</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-if="code.fkko" class="p-4">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <h2 v-if="code.fkko.fkkoclass">Отход (код: {{code.fkko.id}}) - {{code.fkko.name}}</h2>
          <h2 v-if="!code.fkko.fkkoclass">Категория отхода (код: {{code.fkko.id}}) - {{code.fkko.name}}
           в себе содержит:</h2>
          <h4 v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.id}} класс опасности отхода</h4>
          <i v-if="code.fkko.fkkoclass">{{code.fkko.fkkoclass.name}}</i>
          <h4 v-if="code.fkko.aggr">Агрегатное состояние и физические формы отхода</h4>
          <i v-if="code.fkko.aggr">{{ code.fkko.aggr.name }}</i>
          <ul v-for="(item, index) in code.codes" :key="index">
            <li><b-link class="text-success" :href="`/code/${item.id}`">
            {{item.id}}</b-link> - {{item.name}}</li>
          </ul>
          </b-card-text>
        </b-card>
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
    return { code }
  },
  data() {
    return {
      title: 'Информация по коду',
      code: null,
    }
  },
  head() {
    return {
      title: this.code.fkko.name,
    }
  },
};
</script>
