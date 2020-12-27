<template>
  <b-navbar toggleable="sm" class="py-1 px-0 mx-0">
    <b-navbar-brand href="/"><center class="text-success">ВЕБОТХОД.РУ</center></b-navbar-brand>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/queries">Заявки</b-nav-item>
        <b-nav-item href="/code">Классификатор отходов</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-item right href="/user/signup">Зарегистрироваться</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>
