<template>
  <b-navbar toggleable="sm" type="dark" variant="success">
    <b-navbar-brand to="/">WasteCation </b-navbar-brand>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/code/">Классификатор отходов</b-nav-item>
        <b-nav-item to="/utilisation/">Утилизация и вторсырье</b-nav-item>
        <b-nav-item to="/create/">Зарегистрироваться</b-nav-item>
        <b-nav-item to="/request/">Разместить заявку</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em>Личный кабинет</em>
          </template>
          <b-dropdown-item to="/login/">Войти</b-dropdown-item>
          <b-dropdown-item to="/cabinet/">Профиль</b-dropdown-item>
          <b-dropdown-item to="/logout/">Выйти</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>
