$(document).ready(function(){
    $('div.watch-dean').mouseenter(function() {
        $(this).fadeOut('fast', 1);
    });
    $('div.watch-dean').mouseleave(function() {
        $(this).fadeIn(1,'fast',0.25);
    });
})

$('a#new_video').bind('click', function() {
  $.getJSON($SCRIPT_ROOT + '/_new_video'
}
