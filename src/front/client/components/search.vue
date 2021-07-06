<template>
  <b-row class="mx-0 my-3">
    <div class="col-md-9">
      <vue-autosuggest
        :suggestions="codes"
        :input-props="{id:'code', class: 'form-control', placeholder:'Введите название компании или код отхода'}"
        :get-suggestion-value="getSuggestionValue"
        @selected="onSelected"
        @input="updateCodes"
      >
        <template slot-scope="{suggestion}">
          <span class="my-suggestion-item">{{suggestion.item.id}} - {{suggestion.item.name}}</span>
        </template>
      </vue-autosuggest>
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
      codes: [{data: null}],
    }
  },

  methods: {
    find() {
      if(this.search) window.location = `/companies/search/${this.search}`;
    },
    onSelected(item) {
      this.search = item.item.id;
    },
    getSuggestionValue(suggestion) {
      return suggestion.item.id;
    },
    async updateCodes (code) {
      this.search = code;
      /*await this.$axios.$get(`code/search/${code}`
      ).then((response) => {
        this.codes[0].data = response;
      }).catch((error) => {
        console.log();
      });*/
    }
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
