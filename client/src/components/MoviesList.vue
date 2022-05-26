<template>
  <div class='container'>
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-5 g-3">
        <div class="col" v-for="movie in movies">
          <div class="card shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                 preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect>
              <text x="35%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>

            <div class="card-body">
              <a :href="`/movie/${movie.id}/`" class="movie-list-item">
              <p class="card-text">{{movie.name}}</p>
              <p class="card-text">{{movie.director}}</p>
                <p class="card-text">{{movie.date}}</p>
                  <span v-for="genres in movie.genres" style="background-color: dimgray; color: whitesmoke; margin-right: 2px; border-radius: 3px; padding: 2px 2px;">{{ genres }}</span>
              </a>
            </div>
          </div>
        </div>
      </div>
<hr>
      <nav aria-label="Page navigation example">
        <ul class="pagination">

        <li class="page-item" v-if="previousLink">
          <a class="page-link" @click="fetchMovies(previousLink)">Previous</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">Previous</a>
        </li>

        <li class="page-item" v-if="previousLink">
          <a class="page-link" @click="fetchMovies(previousLink)">{{ previous_number }}</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">{{current-1}}</a>
        </li>

        <li class="page-item active" aria-current="page">
          <span class="page-link">{{current}}</span>
        </li>

        <li class="page-item" v-if="nextLink">
          <a class="page-link" @click="fetchMovies(nextLink)">{{ next_number }}</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">{{current+1}}</a>
        </li>

        <li class="page-item" v-if="nextLink">
          <a class="page-link" @click="fetchMovies(nextLink)">Next</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">Next</a>
        </li>

      </ul>
</nav>
    </div>
</template>

<script>
export default {
  name: "MoviesList",
  data() {
    return {
      movies: [],
      nextLink: null,
      previousLink: null,
      pageNo: null,
      current: null,
      previous_number: null,
      next_number: null,
    }
  },
  async mounted() {
    await this.fetchMovies()
  },
  methods: {
    async fetchMovies(url) {
      const targetUrl = url ? url : '/api/imdb/'
      const res = await fetch(targetUrl)
      const data = await res.json()
      this.movies = data["results"];
      this.nextLink = data["next"]
      this.previousLink = data["previous"]
      this.current = data['current']
      this.previous_number = data["previous_number"];
      this.next_number = data["next_number"];
    },
    async addMovie(url) {
      await fetch('/api/imdb/', {
        'method': 'POST',
        'data': {
        }
      } )
    },
  }
}
</script>

<style scoped>
nav {
  display: block;
  width: 150px;
  margin: 0 auto;
}
div{
  margin-top:20px;
}
</style>
