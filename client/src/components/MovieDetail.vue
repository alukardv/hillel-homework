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
          <p>{{movieName}}</p>
              <span style="background-color: dimgray; color: whitesmoke; border-radius: 3px; padding: 2px 12px;">{{movieGenres}}</span>
          <p>{{movieDirector}}</p>
          <p>{{movieDate}}</p>
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

          <tr v-for="participant in movieParts">
            <td>{{ participant.name }}</td><td>{{ participant.position }}</td><td>{{ participant.role }}</td>
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
      movieId: null,
      movieName: null,
      movieDirector: null,
      movieDate: null,
      movieGenres: null,
      movieParts: null,
    }
  },
  async mounted() {
    await this.fetchMovieDetail()
  },
  methods: {
    async fetchMovieDetail(url) {
      const targetUrl = url ? url : `/api/imdb/movie/${this.$route.params.id}`;
      const res = await fetch(targetUrl);
      const data = await res.json();
      this.movieId = data["id"];
      this.movieName = data["name"];
      this.movieDirector = data["director"];
      this.movieDate = data["date"];
      this.movieGenres = data["genres"];
      this.movieParts = data["participants"];
    }
  }
}
</script>

<style>

</style>
