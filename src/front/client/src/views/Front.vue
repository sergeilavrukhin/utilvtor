<template>
  <div class="container">
    <b-navbar toggleable="sm" type="light" variant="light">
      <b-navbar-brand href="#">УтильВтор</b-navbar-brand>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Объявления</b-nav-item>
          <b-nav-item href="#">Организации</b-nav-item>
          <b-nav-item href="#">Классификаторы</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em>Личный кабинет</em>
            </template>
            <b-dropdown-item href="#">Профиль</b-dropdown-item>
            <b-dropdown-item href="#">Выйти</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Front',
  metaInfo: {
    title: 'УтильВтор',
  },
  data() {
    return {
    };
  },
};
</script>
