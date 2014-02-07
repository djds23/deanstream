$('a#new_video').bind('click', function() {
  var a_button = $("a#new_video");
  var video_source = $("video").attr("src");
  var video = $("video");
  $.getJSON($SCRIPT_ROOT + '/_new_video',function(data) {
    $video.removeAttr("src")
    $video.attr("src",data.stream)
});
