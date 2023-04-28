#!/usr/bin/node
/* a JavaScript script that fetches from
https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of
hello from that fetch in the HTML tag DIV#hell */
const $ = window.$;

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').append(data.hello);
});
