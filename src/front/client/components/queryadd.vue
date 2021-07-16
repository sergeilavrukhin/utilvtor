<template>
  <b-card title="Отправить заявку:"
  class="mx-1 my-3">
    <b-card-text>
      <b-form v-if="!success" @submit="onSubmit">

        <b-form-group
          id="input-group-1"
          label="Имя:*"
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
          label="Номер телефона:*"
          label-for="phone"
        >
          <b-form-input
            id="phone"
            v-model="form.phone"
            v-mask="'+7 (###) ###-##-##'"
            type="text"
            required
            placeholder="Номер телефона"
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
            placeholder="Электронная почта"
          ></b-form-input>
        </b-form-group>

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
          id="input-group-1"
          label="Описание:"
          label-for="description">
          <b-form-textarea
          id="description"
          v-model="form.description"
          placeholder="Введите описание..."
          rows="3"
          max-rows="6">
          </b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="success mr-2">Отправить заявку</b-button>
      </b-form>
      <div v-if="error" class="alert alert-danger mt-4" role="alert">
        {{ error }}
      </div>
      <div v-if="success" class="alert alert-success mt-4" role="alert">
        {{ success }}
      </div>
    </b-card-text>
  </b-card>
</template>

<script>
export default {
  data() {
    return {
      title: 'Заявка на утилизацию, транспортировку или обезвреживание отходов, покупку или продажу вторсырья',
      form: {
        firstname: '',
        phone: '',
        email: '',
        query_type: null,
        region: null,
        waste: '',
        description: '',
      },
      show: true,
      success: null,
      error: null,
      region: null,
      query_type: null,
    };
  },
  async fetch() {
    this.region = await fetch(
      `${this.$config.baseURL}api/client/regions/list/`
    ).then(res => res.json())
    this.query_type = await fetch(
      `${this.$config.baseURL}api/client/queries/query_types/`
    ).then(res => res.json())
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();

      await this.$axios.$post('queries/', {
        firstname: this.form.firstname,
        phone: this.form.phone,
        email: this.form.email,
        query_type: this.form.query_type,
        waste: this.form.waste,
        region: this.form.region,
        description: this.form.description,
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
