<template>
  <div class="container">
    <navbar></navbar>
    Вход
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Авторизация',
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
};
</script>
