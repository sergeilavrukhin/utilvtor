<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <div class="row">
      <div class="col-md-12 pl-4 pr-4 pt-4">
        <router-link class="text-success" :to="`/queries/list`">Заявки</router-link>
        <span> &raquo; </span>
        <h1 v-if="item">{{item.query_type.text}} {{item.waste}} <span>{{item.region.text}}</span></h1>
      </div>
    </div>
    <div class="row m-0">
      <div class="col-md-8">
        <b-card v-if="item" :sub-title="item.query_type.text"
        class="mx-1 my-3">
          <b-card-text>
            <ul>
              <li><b>Дата заявки:</b> {{item.date_create}}</li>
              <li><b>Автор:</b>{{item.user.firstname}}</li>
              <li><b>Телефон:</b> {{item.user.phone}}</li>
              <li><b>Email:</b> {{item.user.email}}</li>
            </ul>
            {{item.description}}
          </b-card-text>
        </b-card>
      </div>
      <div class="col-md-4">
        <queryadd></queryadd>
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
      item: null,
      contacts: null,
      title: 'Заявка на утилизацию',
    };
  },
  head() {
    return {
      title: `${this.item.query_type.text} ${this.item.waste ? this.item.waste : ''} в ${this.item.region.text} | утилизация, хранение, переработка, захоронение, транспортирование, обезвреживание отходов, покупка и продажа вторсырья`,
      meta: [
        { hid: 'description', name: 'description',
          content: `Заявка с типом ${this.item.query_type.text} по отходу ${this.item.waste} в ${this.item.region.text}, так же вы можете найти заявки на утилизацию, хранение, захоронение, переработку, транспортирование, обезвреживание отходов, покупку и продажу вторсырья по всем регионам России ${this.item.description}`,
        }
      ],
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
