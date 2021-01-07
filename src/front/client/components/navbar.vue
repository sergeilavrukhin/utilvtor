<template>
  <b-navbar toggleable="sm" class="py-1 px-0 mx-0">
    <b-navbar-brand href="/"><center class="text-success">ВЕБОТХОД.РУ</center></b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/queries">Заявки</b-nav-item>
        <b-nav-item href="/code">Классификатор отходов</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-if="!loggedIn">
        <b-nav-item right href="/user/signin">Войти</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto" v-if="loggedIn">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em>{{ user }}</em>
          </template>
          <b-dropdown-item href="/user/profile">Профиль</b-dropdown-item>
          <b-dropdown-item @click="onLogout">Выйти</b-dropdown-item>
        </b-nav-item-dropdown>
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
      user: this.$auth.user,
    }
  },
  methods: {
    async onLogout() {
      await this.$auth.logout();
      this.$router.go("/");
    },
  },
};
</script>
