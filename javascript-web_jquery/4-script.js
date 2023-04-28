#!/usr/bin/node
/* 
 * Write a JavaScript script that changes the class 
 * of the <header> element when the user clicks the 
 * DIV#toggle_header tag:
 * */
$(function () {
  $('#toggle_header').addClass('red');
});

$('#toggle_header').click(function () {
  $(this).toggleClass('red');
  $(this).toggleClass('green');
});
