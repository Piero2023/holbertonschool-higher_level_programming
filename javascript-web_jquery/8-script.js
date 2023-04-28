#!/usr/bin/node
/* a JavaScript script that fetches and lists the title for 
 * all movies by using this 
 * URL: https://swapi-api.hbtn.io/api/films/?format=json */

$(document).ready(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (data) {
    $.each(data.results, function (index, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
