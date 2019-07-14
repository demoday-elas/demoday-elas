alert("Hello World");

$(document).ready(function() {
    setInterval(function() {
      $current = $('.simple-carousel-show');
      $next = $current.next('div').length > 0 ? $current.next('div') : $current.parent().find('div:first-child');
      
      $current.removeClass('simple-carousel-show');
      $next.addClass('simple-carousel-show');
    }, 2000);
  });