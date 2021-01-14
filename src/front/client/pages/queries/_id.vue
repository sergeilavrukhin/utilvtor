<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 pl-4 pr-4 pt-4">
        <router-link class="text-success" :to="`/queries`">Заявки</router-link>
        <span> &raquo; </span>
        <h1 v-if="item">{{item.query_type.text}} {{item.waste}} <span v-if="item.fkko">{{item.fkko.id}}</span></h1>
      </div>
    </div>
    <div class="row m-0">
      <div class="col-md-12">
        <b-card v-if="item" :sub-title="item.query_type.text"
        class="mx-1 my-3">
          <b-card-text>
            <ul>
              <li v-if="item.fkko"><b>Код отхода:</b> {{item.fkko.id}}</li>
              <li><b>Адрес:</b> {{item.locality}}</li>
              <li><b>Количество:</b> {{item.count}} {{item.unit.text}}</li>
              <li v-if="item.fkko"><b>Класс опасности отхода:</b> {{item.fkko.fkkoclass.text}}</li>
              <li v-if="item.aggr"><b>Агрегатное состояние:</b> {{item.aggr.text}}</li>
              <li><b>Автор:</b> <span v-if="!loggedIn">доступно после регистрации</span>
              <span v-if="loggedIn">{{item.user.firstname}} {{item.user.middlename}}</span></li>
              <li><b>Телефон:</b> <span v-if="!loggedIn">доступно после регистрации</span>
              <span v-if="loggedIn">{{item.user.phone}}</span></li>
              <li><b>Email:</b> <span v-if="!loggedIn">доступно после регистрации</span>
              <span v-if="loggedIn">{{item.user.email}}</span></li>
            </ul>
          </b-card-text>
        </b-card>
        <b-button class="mr-2" v-if="!loggedIn" variant="outline-success" href="/user/signup">Зарегистрироваться</b-button>
        <b-button variant="success" href="/queries/add">Разместить другую заявку</b-button>
        <hr class="my-4">
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params,  $axios }) {
    const item = await $axios.$get(`queries/${params.id}`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { item }
  },
  data() {
    return {
      loggedIn: this.$auth.loggedIn,
      item: null,
      contacts: null,
      title: 'Заявка на утилизацию',
    };
  },
  head() {
    return {
      title: `${this.item.query_type.text} ${this.item.waste ? this.item.waste : ''} | ${this.item.fkko ? this.item.fkko.id : ''} утилизация, транспортирование, обезвреживание, покупка и продажа`,
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
