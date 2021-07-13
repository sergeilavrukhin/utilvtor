<template>
  <b-container>
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card v-for="(item, index) in list" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <h2>Имя: {{item.firstname}}</h2>
            <b>E-mail:</b>{{item.email}}<br />
            <b>Телефон:</b>{{item.phone}}<br />
          </b-card-text>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </b-container>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const list = await $axios.$get(`user/list`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { list }
  },
  data() {
    return {
      title: 'Список пользователей',
      list: null,
      success: null,
      error: null,
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
};
</script>
