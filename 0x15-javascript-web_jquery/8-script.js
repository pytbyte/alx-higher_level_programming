$.get('https://swapi.co/api/films/?format=json', data => {
  const listMovies = $('ul#list_movies');
  data.results.forEach(movie => listMovies.append(`<li>${movie.title}</li>`));
});
