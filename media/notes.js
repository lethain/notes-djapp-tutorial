
var display_error = function(msg, elem) {
  var msg_div = $('<div class="error_msg"><p>'+msg+'</p></div>');
  msg_div.insertAfter(elem).fadeIn('slow').animate({opacity: 1.0}, 5000).fadeOut('slow',function() { msg_div.remove(); });
}; 

var display_success = function(msg, elem) {
  var msg_div = $('<div class="success_msg"><p>'+msg+'</p></div>');
  msg_div.insertAfter(elem).fadeIn('slow').animate({opacity: 1.0}, 5000).fadeOut('slow',function() { msg_div.remove(); });
}; 
