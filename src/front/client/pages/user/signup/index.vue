<template>
  <b-container>
    <navbar></navbar>
    <b-row>
      <b-col class="p-5">
        <b-form v-if="!success" @submit="onSubmit">
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
              v-mask="'+7 (###) ###-##-##'"
              type="text"
              required
              placeholder="+7 (###) ###-##-##"
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
        <div v-if="error" class="alert alert-danger mt-4" role="alert">
          {{ error }}
        </div>
        <div v-if="success" class="alert alert-success mt-4" role="alert">
          {{ success }}
        </div>
      </b-col>
    </b-row>
    <cmp-footer></cmp-footer>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      title: 'Регистрация',
      form: {
        firstname: '',
        middlename: '',
        lastname: '',
        phone: '',
        email: null,
        itn: '',
      },
      success: null,
      error: null,
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();

      await this.$axios.$post('user/sign-up/', {
        firstname: this.form.firstname,
        middlename: this.form.middlename,
        lastname: this.form.lastname,
        phone: this.form.phone,
        email: this.form.email,
        itn: this.form.itn,
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
