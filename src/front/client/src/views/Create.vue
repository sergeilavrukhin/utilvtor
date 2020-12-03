<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-5">
        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group
            id="input-group-1"
            label="Контактное лицо:"
            label-for="contact"
          >
            <b-form-input
              id="contact"
              v-model="form.contact"
              type="text"
              required
              placeholder="ФИО"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="Сотовый телефон:"
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
          <b-button type="reset" variant="outline-danger">Сбросить значения</b-button>
        </b-form>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  name: 'Create',
  metaInfo: {
    title: 'Регистрация',
  },
  data() {
    return {
      form: {
        contact: '',
        phone: '',
        email: null,
        itn: null,
      },
      show: true,
    };
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();

      await this.$http.post('create/', {
        contact: this.form.contact,
        phone: this.form.phone,
        email: this.form.email,
        itn: this.form.itn,
      }).then((response) => {
        alert(response.data);
      }).catch((error) => {
        alert(error);
      });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.contact = '';
      this.form.phone = '';
      this.form.email = null;
      this.form.itn = null;
    },
  },
};
</script>
