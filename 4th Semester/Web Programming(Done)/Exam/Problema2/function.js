var divs = $('div');
$(document).ready(function(){
    divs.filter(':even').css("background-color", "yellow");
    divs.filter(':odd').css("color", "green");
    divs.clone(true, true).contents().appendTo('div.B');
});