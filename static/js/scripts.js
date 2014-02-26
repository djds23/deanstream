$("p#watch-dean-text").click(function() {
  $(this).html("Another!")
});

$(function() {
  var video = function(e) {
    $.getJSON(
      $SCRIPT_ROOT +'/_new_video',
      {
        current_id:   $('span#id_number').val()
      },
      function(data) {
        var id_number = data.id;
        var webm_path = $SCRIPT_ROOT+"static/"+data.webm;
        var mp4_path = $SCRIPT_ROOT+"static/"+data.mp4;
        var poster_path = $SCRIPT_ROOT+"static/img/mobile.jpg";
        $(".insert-video").html('<video autoplay="" loop="" poster="' + poster_path +'">\
                                  <source id="webm" type="video/webm" src="'+ webm_path +'">\
                                  <source id="mp4" type="video/mp4" src="'+ mp4_path +'">\
                                  <span id="id_number"></span>\
                                </video></br>');
      });
  }
  $("a#new_video").bind('click', video);
});
