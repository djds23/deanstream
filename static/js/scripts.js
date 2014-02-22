$(function() {
  var video = function(e) {
    $.getJSON(
      $SCRIPT_ROOT +'/_new_video',
      { current_video: $('video').attr('src') },
      function(data) {
        var webm_path = $SCRIPT_ROOT+"static/"+data.webm;
        var mp4_path = $SCRIPT_ROOT+"static/"+data.mp4;
        var poster_path = $SCRIPT_ROOT+"static/img/mobile.jpg";
        $(".insert-video").html('<video autoplay="" loop="" poster="' + poster_path +'">\
                                  <source type="video/webm" src="'+ webm_path +'">\
                                  <source type="video/mp4" src="'+ mp4_path +'">\
                                  </video></br>');
      });
  }
  $("a#new_video").bind('click', video);
});
