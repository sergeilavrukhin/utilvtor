<template>
  <div class="row">
    <div v-if="companies.length > 0" class="col-md-12">
      <b-pagination-nav v-if="nofp != 0" :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
      <b-card v-for="(item, index) in companies" :key="index" class="mt-3 mb-3">
        <b-card-text>
          <div class="row">
            <div class="col-md-5">
              <a :href="`/companies/${item.id}`">
                <img :src="`https://static-maps.yandex.ru/1.x/?ll=${item.gps.lat},${item.gps.long}&amp;z=10&amp;l=map&amp;size=240,160`">
              </a>
            </div>
            <div class="col-md-7">
              <div class="row">
                <div class="col-md-12">
                  <a :href="`/companies/${item.id}`" class="text-dark"><h2>{{item.name}}</h2></a>
                </div>
              </div>

              <div class="row">
                <div class="col-md-12">
                  <ul class="activity">
                    <li v-if="($route.params.region) && (!$route.params.code) && (!$route.params.search)" v-for="(c_item, c_index) in item.activity" :key="c_index">
                    <a :href="`/companies/region/${$route.params.region}/activity/${c_item}`">{{getActivity(activities, c_item)}}</a>
                    </li>
                    <li v-if="$route.params.code" v-for="(c_item, c_index) in item.activity" :key="c_index">
                    <a :href="`/companies/search/${$route.params.code}/activity/${c_item}`">{{getActivity(activities, c_item)}}</a>
                    </li>
                    <li v-if="$route.params.search" v-for="(c_item, c_index) in item.activity" :key="c_index">
                    <a :href="`/companies/search/${$route.params.search}/activity/${c_item}`">{{getActivity(activities, c_item)}}</a>
                    </li>
                  </ul>
                </div>
              </div>

              <div class="row mt-2">
                <div class="col-md-12">
                  <b-button class="btn btn-success mr-2" :href="`/companies/${item.id}`">Посмотреть контакты</b-button>
                </div>
              </div>
            </div>
          </div>
        </b-card-text>
      </b-card>
      <b-pagination-nav v-if="nofp != 0" :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
    </div>
    <div v-if="companies.length == 0" class="col-md-12">
      <b-card class="mt-3 mb-3">
        <b-card-text>
          Компаний по вашему запросу не найдено
        </b-card-text>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['companies', 'nofp'],
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
      if(this.$route.params.search) {
        var url = `/companies/search/${this.$route.params.search}`;
        if(this.$route.params.region) {
          url = url + `/region/${this.$route.params.region}`;
        }
        if(this.$route.params.activity) {
          url = url + `/activity/${this.$route.params.activity}`;
        }
      } else {
        var url = `/companies/region/${this.$route.params.region}`;
        if(this.$route.params.activity) {
          url = url + `/activity/${this.$route.params.activity}`;
        }
      }
      return pageNum === 1 ? url : `${url}/page/${pageNum}`
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
.activity li a{
  color: #28a745;
}
</style>