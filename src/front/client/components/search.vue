<template>
  <b-form v-on:submit.prevent="find()">
    <b-row class="mx-0 my-3">
      <div class="col-md-3">
        <b-form-group
          id="input-group-1"
        >
          <b-form-select
            id="regions"
            v-model="form.regions"
            :options="regions"
            required
          ></b-form-select>
        </b-form-group>
      </div>
      <div class="col-md-6">
        <b-form-group
          id="input-group-1"
        >
          <b-form-input
            id="search"
            v-model="search"
            type="text"
            placeholder="Введите код или название отхода, или название компании"
          ></b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-3">
        <b-button class="btn btn-block btn-success" @click="find">Найти где утилизировать</b-button>
      </div>
    </b-row>
  </b-form>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      form: {
        regions: this.$route.params.region || 0,
      },
      search: this.$route.params.search,
      regions: null,
      codes: [{data: null}],
    }
  },

  methods: {
    find() {
      if (this.search) {
        if (this.form.regions == 0) {
          window.location = `/companies/search/${this.search}`;
        } else {
          window.location = `/companies/search/${this.search}/region/${this.form.regions}`;
        }
      }
    },
  },
  async fetch() {
    this.regions = await fetch(
      `${this.$config.baseURL}api/client/regions/list/all/`
    ).then(res => res.json())
  }
};
</script>

<style>
.form-control::placeholder {
  color: #ccc;
  opacity: 1;
}
.form-control:focus::placeholder {
  color: #ccc;
  opacity: 0;
}
</style>
