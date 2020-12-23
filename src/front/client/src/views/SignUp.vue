<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-5">
        <b-form @submit="onSubmit">
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

          <b-button type="submit" variant="success mr-2">Зарегистрироваться</b-button>
        </b-form>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  metaInfo: {
    title: 'Регистрация',
  },
  data() {
    return {
      form: {
        firstname: '',
        middlename: '',
        lastname: '',
        phone: '',
        email: null,
        itn: '',
      },
    };
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();

      await this.$http.post('signup/', {
        firstname: this.form.firstname,
        middlename: this.form.middlename,
        lastname: this.form.lastname,
        phone: this.form.phone,
        email: this.form.email,
      }).then((response) => {
        alert(response.data);
      }).catch((error) => {
        alert(error);
      });
    },
  },
};
</script>
