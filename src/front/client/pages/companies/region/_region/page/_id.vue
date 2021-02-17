<template>
  <div class="container">
    <navbar></navbar>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
        <b-link class="text-success" href="/companies">Компании</b-link>
        <span> &raquo; </span><h1>{{region_name}}</h1>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
        <b-card v-for="(item, index) in companies" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <div class="row">
              <div class="col-md-3">
                <img :src="`https://static-maps.yandex.ru/1.x/?ll=${item.gps.lat},${item.gps.long}&amp;z=10&amp;l=map&amp;size=240,160`">
              </div>
              <div class="col-md-9">
                <a :href="`/companies/${item.id}`" class="text-dark"><h2>{{item.name}}</h2></a>
                <i>{{item.address}}</i>
                <ul class="activity">
                  <li v-for="(c_item, c_index) in item.activity" :key="c_index">
                  {{getActivity(activities, c_item)}}
                  </li>
                </ul>
              </div>
            </div>
          </b-card-text>
        </b-card>
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="nofp" align="center"></b-pagination-nav>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const region = await $axios.$get(`companies/${params.region}/page/${params.id}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    const companies = region.companies;
    const nofp = region.count;
    const region_name = region.name;
    return { companies, nofp, region_name }
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      companies: null,
      nofp: 10,
      region_name: null,
      activities: {
        processing: 'Переработка',
        collection: 'Хранение',
        deactivation: 'Обезвереживание',
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
      return pageNum === 1 ? `/companies/region/${this.$route.params.region}/` : `/companies/region/${this.$route.params.region}/page/${pageNum}/`
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

</style>
