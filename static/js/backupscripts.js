$('a#new_video').bind('click', function() {
  var video = $("video")
  $.getJSON($SCRIPT_ROOT + '/_new_video',function(data) {
    $video.removeAttr("src");
    $video.attr("src",data.stream);
});
});
