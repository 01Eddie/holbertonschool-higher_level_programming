$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    const titleMovie = data.results;
    titleMovie.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
