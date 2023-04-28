#!/usr/bin/node
/* Write a JavaScript script that updates the text of the 
<header>New Header!!! element when the user clicks DIV#update_header */

$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').replaceWith('New Header!!!');
  });
});
