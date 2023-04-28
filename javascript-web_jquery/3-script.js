#!/usr/bin/node
/* JavaScript script that adds the class redal <header> 
 * element when the user clicks the DIV#red_header tag */

$('#red_header').click(function () {
  $('header').addClass('red');
});
