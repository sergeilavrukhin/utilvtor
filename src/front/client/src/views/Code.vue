<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 pl-4 pr-4 pt-4">
        <a v-if="code" class="text-success" to="/code/">Блоки кодов ФККО</a>
        <span v-if="code"> &raquo; </span>
        <span v-for="(item, index) in breadcrumb" :key="index">
        <a class="text-success"
        :to="`/code/${item.id}/`">{{item.name}}</a> &raquo;
        </span> <h1>{{title}}</h1>
        <h5>{{subtitle}}</h5>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card class="mt-3 mb-3">
          <b-card-text>
          <h2 v-if="w_class">Отход (код: {{code}}) - {{title}}</h2>
          <h2 v-if="!w_class && code">Категория отхода (код: {{code}}) - {{title}}
           в себе содержит:</h2>
          <h4 v-if="w_class">{{w_class}} класс опасности отхода</h4>
          <i v-if="w_class_desc">{{w_class_desc}}</i>
          <h4 v-if="aggrname">Агрегатное состояние и физические формы отхода</h4>
          <i v-if="aggrname">{{aggrname}}</i>
          <ul v-for="(item, index) in codes" :key="index">
            <li><router-link class="text-success" :to="`/code/${item.id}/`">
            {{item.id}}</router-link> - {{item.name}}</li>
          </ul>
          </b-card-text>
        </b-card>
     </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'Code',
  metaInfo() {
    return {
      title: this.title,
    };
  },
  data() {
    return {
      code: this.$route.params.id,
      codes: null,
      title: 'Блоки кодов ФККО',
      subtitle: null,
      breadcrumb: null,
      aggrname: null,
      w_class: null,
      w_class_desc: null,
      w_state: null,
    };
  },
  methods: {
    async loadCodes() {
      if (this.$route.params.id != null) {
        await this.$http.get(`code/${this.$route.params.id}`).then((response) => {
          this.codes = response.data.codes;
          this.code = this.$route.params.id;
          this.title = response.data.title;
          this.subtitle = response.data.subtitle;
          this.breadcrumb = response.data.parents;
          this.title = response.data.title;
          this.w_class = response.data.fkkoclass.id;
          this.w_class_desc = response.data.fkkoclass.name;
          this.aggrname = response.data.aggrname;
        }).catch((error) => {
          console.log(error);
        });
      } else {
        await this.$http.get('code/').then((response) => {
          this.codes = response.data.codes;
          this.code = null;
          this.title = response.data.title;
          this.metaInfo.title = this.title;
          this.subtitle = response.data.subtitle;
          this.breadcrumb = null;
          this.w_class = response.data.w_class;
          this.w_class_desc = response.data.w_class_desc;
          this.w_state = response.data.w_state;
        }).catch((error) => {
          console.log(error);
        });
      }
    },
  },
  async created() {
    this.loadCodes();
  },
  watch: {
    $route(to, from) {
      if (to.params.id !== from.params.id) {
        this.loadCodes();
      }
    },
  },
};
</script>
