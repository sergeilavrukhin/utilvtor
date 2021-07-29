<template>
  <div class="container">
    <navbar></navbar>
    <b-row>
      <b-col class="pl-4 pr-4 pt-4">
       <center><h2>Вы переходите на сайт: <a :href="`${$route.params.link}`" class="text-dark">{{$route.params.link}}</a></h2></center>
      </b-col>
    </b-row>
    <cmp-footer></cmp-footer>
  </div>
</template>

<script>
export default {
  async asyncData({ params, $axios }) {
    const company = await $axios.$get(`companies/siteclick/${params.company}/`).then((response) => {

    }).catch((error) => {
      console.log(error);
    });
    console.log(params);
  },
  data() {
    return {
    };
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

.uppercase {
  text-transform: uppercase;
}

a {
    color: #28a745;
}
</style>