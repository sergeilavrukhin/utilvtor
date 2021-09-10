<template>
  <b-container>
    <navbar></navbar>
    <b-row>
      <b-col class="p-5">
        <b-form @submit="onSubmit" v-if="form">

          <b-form-group
            id="input-group-1"
            label="*Email:"
            label-for="email"
          >
            <b-form-input
              id="email"
              v-model="form.email"
              type="text"
              required
              placeholder="Email"
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
            label="*Сотовый телефон:"
            label-for="phone"
          >
            <b-form-input
              id="phone"
              v-model="form.phone"
              v-mask="'+# (###) ###-##-##'"
              type="text"
              required
              placeholder="+7 (###) ###-##-##"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="success mr-2">Редактировать</b-button>
        </b-form>
        <div v-if="!form" class="alert alert-danger mt-4" role="alert">
          Доступ закрыт
        </div>
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
  async asyncData({ params, $axios }) {
    const form = await $axios.$get(`user/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { form }
  },
  data() {
    return {
      title: 'Редактирование профиля',
      form: {
        email: null,
        firstname: null,
        phone: '',
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

      await this.$axios.$post('user/edit/', {
        firstname: this.form.firstname,
        email: this.form.email,
        phone: this.form.phone,
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
