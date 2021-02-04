<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-4">
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
        <fieldset>
        <p>В нашем агрегаторе вы можете найти все фирмы из {{area}} в городе {{city}} которые
         имеют лицензии на обращение с отходами. Вся информация о лицензиях на утилизацию,
         сбор, хранение, обезвреживание и транспортирование отходов является актуальной
         и обновляется ежедневно.</p><p>Несоблюдение экологических и
         санитарно-эпидемиологических требований при сборе, накоплении, использовании,
         обезвреживании, транспортировании, размещении и ином обращении с отходами производства
         и потребления, веществами, разрушающими озоновый слой, или иными опасными веществами
         — влечет наложение административного штрафа на юридические лица до 250 000 рублей,
         при повторном нарушении до 500 000 рублей.</p>
        </fieldset>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const companies = await $axios.$get(`companies/${params.id}/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { companies }
  },
  data() {
    return {
      title: 'Организации занимающиеся утилизацией, переработкой, транспортировкой, обезвреживанием отходов, покупкой и продажей вторсырья',
      companies: null,
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
  },
};
</script>
