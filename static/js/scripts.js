$(document).ready(function() {
  $('div.watch-dean p').on('click', function() {
    $(this).removeClass('watch-dean-text').addClass('watch-dean-after-click');
    $(this).text('Another!');
  });
  storage=$.localStorage;
});

$(function() {
  var video = function(e) {
    $.getJSON(
      $SCRIPT_ROOT +'/_new_video',
      {
        current_id: storage.get('video_id')
      },
      function(data) {
        storage.set('video_id',data.video_id);
        var webm_path = $SCRIPT_ROOT+"static/"+data.webm;
        var mp4_path = $SCRIPT_ROOT+"static/"+data.mp4;
        var poster_path = $SCRIPT_ROOT+"static/img/mobile.jpg";
        $(".insert-video").html('<video autoplay="" loop="" poster="' + poster_path +'">\
                                  <source id="webm" type="video/webm" src="'+ webm_path +'">\
                                  <source id="mp4" type="video/mp4" src="'+ mp4_path +'">\
                                </video></br>');
      });
  }
  $("a#new_video").bind('click', video);
});
