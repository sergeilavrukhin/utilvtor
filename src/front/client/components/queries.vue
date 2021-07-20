<template>
  <div class="row">
    <div v-if="queries.length > 0" class="col-md-12">
      <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
      <b-card v-for="(item, index) in queries" :key="index"
       :title="`${item.query_type.text} ${item.waste}`" :sub-title="`Регион: ${item.region.text}`"
      class="mx-1 my-3">
        <b-card-text>
        Дата заявки: {{ item.date_create }}<br />
        {{ item.description }}
        </b-card-text>
        <router-link :to="`/queries/${item.id}`" class="text-success">Посмотреть</router-link>
      </b-card>
      <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
    </div>
    <div v-if="queries.length == 0" class="col-md-12">
      <b-card class="mt-3 mb-3">
        <b-card-text>
          Заявки не найдены
        </b-card-text>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['queries', 'nofp'],
  data () {
    return {
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвреживание',
        transportation: 'Транспортировка',
        utilization: 'Утилизация',
        disposal: 'Захоронение',
      },
    }
  },
  methods: {
    getActivity: (activities, val) => activities[val],
    linkGen(pageNum) {
      return pageNum === 1 ? '/queries/list' : `/queries/list/page/${pageNum}`
    }
  },
};
</script>

<style>
.page-item .page-link {
    color: #28a745;
}

.page-item.active .page-link {
    color: #fff;
    background-color: #28a745;
    border-color: #28a745;
}

.activity{
  clear: both;
  padding: 0px;
  margin: 0px;
}
.activity li {
  float: left;
  list-style-type: none;
  padding: 5px;
  margin: 2px;
  border: 1px solid #ccc;
}
</style>