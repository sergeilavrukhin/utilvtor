<template>
  <b-row class="mx-0 my-3">
    <div class="col-md-9">
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
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      search: null,
      regions: null,
      codes: [{data: null}],
    }
  },

  methods: {
    find() {
      if(this.search) window.location = `/companies/search/${this.search}`;
    },
  },
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
