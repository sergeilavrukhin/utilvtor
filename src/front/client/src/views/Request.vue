<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-5">
        <b-form @submit="onSubmit">
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
            label="Адрес местонахождения отхода(регион, населенный пункт):*"
            label-for="address"
          >
            <b-form-input
              id="address"
              v-model="form.address"
              type="text"
              required
              placeholder="Адрес местонахождения отхода"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-2"
            label="Код ФККО или название отхода:*"
            label-for="fkko"
          >
            <b-form-input
              id="fkko"
              v-model="form.fkko"
              type="text"
              required
              placeholder="Код ФККО или название отхода"
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
          >
            <b-form-input
              id="phone"
              v-model="form.phone"
              type="text"
              required
              placeholder="Сотовый телефон"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="*Электронная почта:"
            label-for="email"
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
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'Request',
  metaInfo: {
    title: 'Новая заявка',
  },
  data() {
    return {
      form: {
        lastname: '',
        firstname: '',
        middlename: '',
        phone: '',
        email: '',
        itn: '',
        query_type: '',
        address: '',
        fkko: '',
        count: '',
        bu: '',
      },
      show: true,
      query_type: [{ value: 1, text: 'Утилизация' }, { value: 2, text: 'Обезвреживание' }],
      bu: [{ value: 1, text: 'шт.' }, { value: 3, text: 'кг.' }, { value: 3, text: 'тонн.' }],
    };
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();

      await this.$http.post('queries/', {
        lastname: this.form.lastname,
        firstname: this.form.firstname,
        middlename: this.form.middlename,
        phone: this.form.phone,
        email: this.form.email,
        itn: this.form.itn,
        query_type: this.form.query_type,
        address: this.form.address,
        fkko: this.form.fkko,
        count: this.form.count,
        bu: this.form.bu,
      }).then((response) => {
        alert(response.data);
      }).catch((error) => {
        alert(error);
      });
    },
  },
};
</script>
