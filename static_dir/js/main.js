function autoHeight() {
    $('#content').css('min-height', 0);
    $('#content').css('min-height', (
     $(document).height()
     - $('#header').height()
     - $('#footer').height()
    ));
}

$(window).resize(function() {
    autoHeight();
});

$(document).ready(function() {
    autoHeight();
});