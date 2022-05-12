<template>
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-5 g-3">
        <div class="col" v-for="movie in movies">
          <div class="card shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail"
                 preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect>
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>

            <div class="card-body">
              <a :href="`/movie/${movie.id}/`" style="a.movie-list-item, a.movie-list-item:hover, a.movie-list-item:visited { color: black; text-decoration: none; }">
              <p class="card-text">{{movie.name}}</p>
              <p class="card-text">{{movie.director}}</p>
                <p class="card-text">{{movie.date}}</p>
                  <span v-for="genres in movie.genres" style="background-color: dimgray; color: whitesmoke; margin-right: 10px; border-radius: 3px; padding: 2px 10px;">{{ genres }}</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#" @click="fetchMovies(previousLink)">Previous</a></li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#" @click="fetchMovies(current)">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#" @click="fetchMovies(nextLink)">Next</a></li>
      </ul>
</nav>
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
