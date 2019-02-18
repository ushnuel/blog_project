$(window).on("load", function(){
  $('#preload').delay(5000).fadeOut('slow', function(){
     $(this).remove();
  });
});
