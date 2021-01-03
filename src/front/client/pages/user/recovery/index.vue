<template>
  <b-container>
    <navbar></navbar>
    <b-row>
      <b-col class="p-5">
        <b-form v-if="!success" @submit="onSubmit">
          <b-form-group
            id="input-group-1"
            label="Электронная почта:"
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
            label="Пароль:"
            label-for="password"
          >
            <b-form-input
              id="password"
              v-model="form.password"
              type="password"
              required
              placeholder="Пароль"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="success mr-2">Войти</b-button>
          <b-button variant="outline-success" href="/user/signup">Зарегистрироваться</b-button>
          <b-button variant="outline-success" href="/user/recovery">Восстановить пароль</b-button>
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
      title: 'Авторизация',
      form: {
        email: null,
        password: null,
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

      await this.$axios.$post('user/sign-in/', {
        email: this.form.email,
        password: this.form.password
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
