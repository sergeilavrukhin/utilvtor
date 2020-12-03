<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-5">
        <b-form @submit="onSubmit">
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

          <b-form-group id="input-group-2" label="Запрос:" label-for="input-3">
            <b-form-select
              id="input-3"
              v-model="form.waste_type"
              :options="waste_type"
              required
            ></b-form-select>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="Адрес местонахождения отхода:"
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
            id="input-group-1"
            label="Код ФККО или название отхода:"
            label-for="code"
          >
            <b-form-input
              id="code"
              v-model="form.code"
              type="text"
              required
              placeholder="Код ФККО или название отхода"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-1"
            label="Количество:"
            label-for="count"
          >
            <b-form-input
              id="count"
              v-model="form.count"
              type="text"
              required
              placeholder="Количество"
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
        contact: '',
        phone: '',
        email: null,
        itn: null,
      },
      show: true,
      waste_type: ['Утилизация', 'Обезвреживание'],
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
  },
};
</script>
