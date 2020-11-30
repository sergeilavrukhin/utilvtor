<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card class="mt-3 mb-3" title="Классификация осуществляется по нескольким
         признакам, оцениваемым в совокупности: происхождению, агрегатному состоянию,
          степени вредного воздействия и опасным свойствам.">
          <b-card-text>
          <ul v-for="(item, index) in codes" :key="index">
            <li><router-link class="text-success" :to="`/code/${item.id}/`">
            {{item.id}}</router-link>
             - {{item.name}}</li>
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
  metaInfo: {
    title: 'Коды',
  },
  data() {
    return {
      code: this.$route.params.id,
      codes: null,
    };
  },
  methods: {
    async loadCodes() {
      if (this.$route.params.id != null) {
        await this.$http.get(`code/${this.$route.params.id}/`).then((response) => {
          this.codes = response.data;
        }).catch((error) => {
          console.log(error);
        });
      } else {
        await this.$http.get('code/').then((response) => {
          this.codes = response.data;
        }).catch((error) => {
          console.log(error);
        });
      }
    },
  },
  async created() {
    this.loadCodes();
  },
  async updated() {
    this.loadCodes();
  },
};
</script>
