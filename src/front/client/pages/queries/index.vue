<template>
  <div class="container">
    <navbar></navbar>
    <h1>{{ title }}</h1>
    <hr class="my-4">
      <b-button class="mr-2" v-if="!loggedIn" variant="outline-success" href="/user/signup">Зарегистрироваться</b-button>
      <b-button variant="success" href="/queries/add">Разместить заявку</b-button>
    <hr class="my-4">
    <div class="row m-0">
      <div class="col-md-8">
        <b-card v-for="(item, index) in queries" :key="index"
        :title="item.waste" :sub-title="item.query_type.text"
        class="mx-1 my-3">
          <b-card-text>
            <ul>
              <li v-if="item.fkko"><b>Код отхода:</b> {{item.fkko.id}}</li>
              <li><b>Адрес:</b> {{item.region.text}}, {{item.locality}}</li>
              <li><b>Количество:</b> {{item.count}} {{item.unit.text}}</li>
              <li v-if="item.fkko"><b>Класс опасности отхода:</b> {{item.fkko.fkkoclass.text}}</li>
              <li v-if="item.aggr"><b>Агрегатное состояние:</b> {{item.aggr.text}}</li>
            </ul>
          </b-card-text>
          <router-link :to="`queries/${item.id}`" class="text-success">Посмотреть</router-link>
        </b-card>
        <b-card v-if="queries.length == 0">
          Заявки не найдены
        </b-card>
      </div>
      <div class="col-md-4">
        <b-card title="Фильтрация:"
        class="mx-1 my-3">
          <b-card-text>
            Код ФККО:<br />
            <vue-autosuggest
              :suggestions="codes"
              :input-props="{id:'code', class: 'form-control', placeholder:'Код или название отхода'}"
              :get-suggestion-value="getSuggestionValue"
              @selected="onSelected"
              @input="updateCodes"
            >
              <template slot-scope="{suggestion}">
                <span class="my-suggestion-item">{{suggestion.item.id}} - {{suggestion.item.name}}</span>
              </template>
            </vue-autosuggest>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const queries = await $axios.$get('queries/').then((response) => {
      console.log(response);
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { queries }
  },
  data() {
    return {
      loggedIn: this.$auth.loggedIn,
      searchcode: null,
      queries: null,
      title: 'Заявки на утилизацию, транспортирование, обезвреживание оходов, а так же покупку и продажу вторсырья',
      codes: [{data: null}],
    };
  },
  head() {
    return {
      title: this.title,
    }
  },

  methods: {
    async updateQueries(code) {
      if(code) {
        await this.$axios.$get(`queries/code/${code}`).then((response) => {
          this.queries = response;
        }).catch((error) => {
          console.log(error);
        });
      } else {
        await this.$axios.$get(`queries/`).then((response) => {
          this.queries = response;
        }).catch((error) => {
          console.log(error);
        });
      }
    },
    onSelected(item) {
      if(item) {
        this.searchcode = item.item.id;
        this.updateQueries(item.item.id);
      } else {
        this.searchcode = document.getElementById('code').value;
        this.updateQueries(this.searchcode);
      }
    },
    getSuggestionValue(suggestion) {
      return suggestion.item.id;
    },
    async updateCodes (code) {
      await this.$axios.$get(`code/search/${code}`
      ).then((response) => {
        this.codes[0].data = response;
      }).catch((error) => {
        console.log();
      });
    }
  }
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

.autosuggest__results ul {
  width: 100%;
  color: rgba(30, 39, 46,1.0);
  list-style: none;
  margin: 0;
  padding: 0.5rem 0 .5rem 0;
}
.autosuggest__results li {
  margin: 0 0 0 0;
  border-radius: 5px;
  padding: 0.75rem 0 0.75rem 0.75rem;
  display: flex;
  align-items: center;
}
.autosuggest__results li:hover {
  cursor: pointer;
}

#autosuggest {
  width: 95%;
  background-color: #fff;
  z-index: 9999;
}
.autosuggest__results-item--highlighted {
  background-color: rgba(40, 167, 69, 0.2);
}
</style>
