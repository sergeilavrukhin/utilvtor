<template>
  <div class="container">
    <navbar></navbar>
    <search></search>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/companies">Компании</b-link>
        <span> &raquo; </span><h1>Поиск по утилизаторам</h1>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col-md-8">
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
        <b-card v-if="companies" v-for="(item, index) in companies" :key="index" class="mt-3 mb-3">
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
                      <li v-for="(c_item, c_index) in item.activity" :key="c_index">
                      {{getActivity(activities, c_item)}}
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
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
      </div>
      <div class="col-md-4">
        <queryadd :region="region" :query_type="query_type"></queryadd>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    var search = encodeURI(params.search);
    const region_one = await $axios.$get(`companies/search/${search}/region/${params.region}/page/${params.id}/`).then((response) => {
      return response;
    });

    const query_type = await $axios.$get('queries/query_types/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const region = await $axios.$get('regions/').then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });

    if(region_one) {
      const companies = region_one.companies;
      const nofp = region_one.count;
      const region_name = region_one.name;
      return { query_type, region, companies, nofp, region_name }
    } else {
      return { query_type, region}
    }
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      companies: null,
      region: null,
      query_type: null,
      nofp: 10,
      region_name: null,
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвреживание',
        transportation: 'Транспортировка',
        utilization: 'Утилизация',
        disposal: 'Захоронение',
      },
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
  methods: {
    getActivity: (activities, val) => activities[val],
    linkGen(pageNum) {
      return pageNum === 1 ? `/companies/search/${this.$route.params.search}` : `/companies/search/${this.$route.params.search}/page/${pageNum}`
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
