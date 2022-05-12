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
          <p>{{movie.name}}</p>
              <span style="background-color: dimgray; color: whitesmoke; border-radius: 3px; padding: 2px 12px;">{{movie.genres}}</span>
        </div>
      </div>
    </div>
  </div>
  <div class="table-responsive" style="width: 42%;">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Position</th>
          <th scope="col">Role</th>
        </tr>
      </thead>
      <tbody>
        <tr>
        <td>{{movie.director}}</td><td>director</td><td></td>
        </tr>
        <tr>
        <td>{{movie.actor}}</td><td>actor</td><td></td>
        </tr>
      <tr>
        <td>{{movie.composer}}</td><td>composer</td><td></td>
        </tr>
      <tr>
        <td>{{movie.producer}}</td><td>producer</td><td></td>
        </tr>
      <tr>
        <td>{{movie.writer}}</td><td>writer</td><td></td>
        </tr>
      <tr>
        <td>{{movie.cinematographer}}</td><td>cinematographer</td><td></td>
        </tr>

      </tbody>
    </table>
</div>
</div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      movie: {}
    }
  },
  async mounted() {
      const res = await fetch(`/api/imdb/${this.$route.params.id}`)
      const data = await res.json()
      this.movie = data;
  }
}
</script>

<style scoped>

</style>
