<template>

<div class='container'>
  <div class="card mb-3" style="max-width: 540px;">
      <div class="row g-0">
        <div class="col-md-4">
          <img src="" class="img-fluid rounded-start" width="100%" height="100%" alt="Photo_movie">
        </div>
        <p></p>
        <div class="col-md-8">
          <div class="card-body" style="position: relative;">
            <p>{{personName}}</p>
            <p>Рейтинг: {{personRating}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonDetail",
  data() {
    return {
      personId: null,
      personName: null,
      personRating: null,
    }
  },
  async mounted() {
    await this.fetchPersonDetail()
  },
  methods: {
    async fetchPersonDetail(url) {
      const targetUrl = url ? url : `/api/imdb/person/${this.$route.params.id}`;
      const res = await fetch(targetUrl);
      const data = await res.json();
      this.personId = data["id"];
      this.personName = data["name"];
      this.personRating = data["rating_avg"];
    }
  }
}
</script>

<style>

</style>
