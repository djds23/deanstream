$(function() {
  var video = function(e) {
    $.getJSON($SCRIPT_ROOT +'/_new_video', {
    }, function(data) {
      var full_path = $SCRIPT_ROOT+"static/webm/"+ data.stream
      $('video').removeAttr('src');
      $('video').attr('src', full_path  );
    });
  }
  $("a#new_video").bind('click', video);
});
