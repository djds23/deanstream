$(function() {
  var video = function(e) {
    $.getJSON(
      $SCRIPT_ROOT +'/_new_video',
      { current_video: $('video').attr('src') },
      function(data) {
        var webm_path = $SCRIPT_ROOT+"static/"+data.webm;
        $('#webm').attr('src', webm_path);
        var mp4_path = $SCRIPT_ROOT+"static/"+data.mp4;
        $('#mp4').attr('src', mp4_path);
      });
  }
  $("a#new_video").bind('click', video);
});
