<template>
  <b-navbar toggleable="sm" class="py-1 px-0 mx-0">
    <b-navbar-brand href="/"><center class="text-success">ВЕБОТХОД.РУ</center></b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/queries/list">Заявки</b-nav-item>
        <b-nav-item href="/code">Классификатор отходов</b-nav-item>
        <b-nav-item href="/companies">Утилизаторы</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
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
