<template>
  <b-navbar toggleable="sm" class="py-1 px-0 mx-0">
    <b-navbar-brand to="/"><center class="text-success">WEBOTHOD</center></b-navbar-brand>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/queries/">Заявки</b-nav-item>
        <b-nav-item href="/code/">Классификатор отходов</b-nav-item>
        <b-nav-item href="/utilisation/">Утилизация и вторсырье</b-nav-item>
        <b-nav-item href="/request/">Разместить заявку</b-nav-item>
      </b-navbar-nav>

      <!--<b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em>Личный кабинет</em>
          </template>
          <b-dropdown-item href="/login/">Войти</b-dropdown-item>
          <b-dropdown-item href="/cabinet/">Профиль</b-dropdown-item>
          <b-dropdown-item href="/logout/">Выйти</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>-->
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>
