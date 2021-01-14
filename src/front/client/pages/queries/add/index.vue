<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-5">
        <b-form v-if="!success" @submit="onSubmit">
          <b-form-group
            id="input-group-2"
            label="Запрос:*"
            label-for="query_type">
            <b-form-select
              id="query_type"
              v-model="form.query_type"
              :options="query_type"
              required
            ></b-form-select>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Регион местонахождения отхода:*"
            label-for="region">
            <b-form-select
              id="region"
              v-model="form.region"
              :options="region"
              required
            ></b-form-select>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Населенный пункт местонахождения отхода:*"
            label-for="address"
          >
            <b-form-input
              id="address"
              v-model="form.address"
              type="text"
              required
              placeholder="Населенный пункт местонахождения отхода"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Код ФККО:"
            label-for="fkko"
          >
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
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Название отхода:*"
            label-for="waste"
          >
            <b-form-input
              id="waste"
              v-model="form.waste"
              type="text"
              required
              placeholder="Название отхода"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Количество отхода:*"
            label-for="count"
          >
            <b-form-input
              id="count"
              v-model="form.count"
              type="text"
              required
              placeholder="Количество отхода"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Ед.изм:*"
            label-for="bu">
            <b-form-select
              id="bu"
              v-model="form.bu"
              :options="bu"
              required
            ></b-form-select>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Фамилия:"
            label-for="lastname"
            v-if="!loggedIn"
          >
            <b-form-input
              id="lastname"
              v-model="form.lastname"
              type="text"
              required
              placeholder="Фамилия"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Имя:"
            label-for="firstname"
            v-if="!loggedIn"
          >
            <b-form-input
              id="firstname"
              v-model="form.firstname"
              type="text"
              required
              placeholder="Имя"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Отчество:"
            label-for="middlename"
            v-if="!loggedIn"
          >
            <b-form-input
              id="middlename"
              v-model="form.middlename"
              type="text"
              required
              placeholder="Отчество"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Сотовый телефон:"
            label-for="phone"
            v-if="!loggedIn"
          >
            <b-form-input
              id="phone"
              v-model="form.phone"
              v-mask="'+7 (###) ###-##-##'"
              type="text"
              required
              placeholder="Сотовый телефон"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Электронная почта:"
            label-for="email"
            v-if="!loggedIn"
          >
            <b-form-input
              id="email"
              v-model="form.email"
              type="email"
              required
              placeholder="Электронная почта"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="ИНН:"
            label-for="itn"
            v-if="!loggedIn"
          >
            <b-form-input
              id="itn"
              v-model="form.itn"
              type="text"
              placeholder="ИНН"
            ></b-form-input>
          </b-form-group>
          <b-button type="submit" variant="success mr-2">Отправить заявку</b-button>
        </b-form>
        <div v-if="error" class="alert alert-danger mt-4" role="alert">
          {{ error }}
        </div>
        <div v-if="success" class="alert alert-success mt-4" role="alert">
          {{ success }}
        </div>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    const query_type = await $axios.$get('queries/query_types/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const bu = await $axios.$get('queries/units/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const region = await $axios.$get('regions/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { query_type, bu, region }
  },
  data() {
    return {
      title: 'Заявка на утилизацию, транспортировку или обезвреживание отходов, покупку или продажу вторсырья',
      form: {
        lastname: '',
        firstname: '',
        middlename: '',
        phone: '',
        email: '',
        itn: '',
        query_type: null,
        region: null,
        address: '',
        fkko: '',
        waste: '',
        count: '',
        bu: null,
      },
      show: true,
      query_type: null,
      bu: null,
      region: null,
      success: null,
      error: null,
      loggedIn: this.$auth.loggedIn,
      codes: [{data: null}],
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
  methods: {
    onSelected(item) {
      this.form.fkko = item.item.id;
      this.form.waste = item.item.name;
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
    },

    async onSubmit(evt) {
      evt.preventDefault();

      await this.$axios.$post('queries/', {
        lastname: this.form.lastname,
        firstname: this.form.firstname,
        middlename: this.form.middlename,
        phone: this.form.phone,
        email: this.form.email,
        itn: this.form.itn,
        query_type: this.form.query_type,
        address: this.form.address,
        fkko: this.form.fkko,
        waste: this.form.waste,
        count: this.form.count,
        bu: this.form.bu,
        region: this.form.region,
      }).then((response) => {
        this.success = response.msg;
        this.error = null;
      }).catch((error) => {
        this.success = null;
        if (error.response) {
          if (error.response.status === 403) {
            this.error = error.response.data.msg;
          }
        }
      });
    },
  },
};
</script>

<style>

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
  width: 100%;
  background-color: #fff;
  z-index: 9999;
}
.autosuggest__results-item--highlighted {
  background-color: rgba(40, 167, 69, 0.2);
}
</style>
