<template>
  <b-navbar toggleable="sm" class="py-1 px-0 mx-0">
    <b-navbar-brand href="/"><center class="text-success">ВЕБОТХОД.РУ</center></b-navbar-brand>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/queries">Заявки</b-nav-item>
        <b-nav-item href="/code">Классификатор отходов</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto" v-if="!loggedIn">
        <b-nav-item right href="/user/signin">Войти</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-if="loggedIn">
        <b-nav-item right @click="onLogout">Выйти</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      loggedIn: this.$auth.loggedIn,
    }
  },
  methods: {
    async onLogout() {
      await this.$auth.logout();
      if(this.$auth.loggedIn == false) this.$router.go("/");

    },
  },
};
</script>
