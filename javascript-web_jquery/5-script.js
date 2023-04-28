!/usr/bin/node
/* JavaScript script that adds a <li>item to a 
 * list when the user clicks the DIV#add_item tag:*/
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
