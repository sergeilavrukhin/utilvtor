<template>
  <div class="container">
    <navbar></navbar>
    <h1>{{ title }}</h1>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ $axios }) {
  },
  data() {
    return {
      queries: null,
      title: 'Информация о пользователе',
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
};
</script>

<style>
h1 {
  font-size: 16px;
  text-transform: uppercase;
}

h2 {
  font-size: 15px;
  text-transform: uppercase;
}
</style>
