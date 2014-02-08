$(function() {
  var video = function(e) {
    $.getJSON($SCRIPT_ROOT +'/_new_video', {
    }, function(data) {
      $('video').removeAttr('src');
      $('video').Attr('src', data.stream);
    });
  }
  $("a#new_video").bind('click', video);
});
