<template>
  <b-container>
    <navbar></navbar>
    <div class="row">
      <div class="col-md-12 p-4">
        <b-card v-for="(item, index) in list" :key="index" class="mt-3 mb-3">
          <b-card-text>
            <ul>
              <li>Код: {{item.id}}</li>
              <li>ISO: {{item.iso}}</li>
              <li>Название: {{item.text}}</li>
              <li>URL: {{item.url}}</li>
              <li>CODE: {{item.value}}</li>
            </ul>
          </b-card-text>
        </b-card>
      </div>
    </div>
    <cmp-footer></cmp-footer>
  </b-container>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const list = await $axios.$get(`regions/`).then((response) => {
      return response;
    }).catch((error) => {
      console.log(error);
    });
    return { list }
  },
  data() {
    return {
      title: 'Список регионов',
      list: null,
      success: null,
      error: null,
    };
  },
  head() {
    return {
      title: this.title,
    }
  },
};
</script>
