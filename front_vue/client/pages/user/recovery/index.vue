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

          <b-button type="submit" variant="success mr-2">Восстановить</b-button>
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
      title: 'Восстановление пароля',
      form: {
        email: null,
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

      await this.$axios.$post('user/recovery/', {
        email: this.form.email
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
