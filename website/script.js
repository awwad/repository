$('#timestamp').click(function(){
var nonce = [1,2,3]; 

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var request = $.ajax({
  url: "https://uptane.umtri.umich.edu:24515/timeserver/",
  method: 'POST',
  processData: false,
  data: '[1,2,3]',
  crossDomain: true,
});

 
request.done(function( msg ) {
  console.log( msg );  
  $('#log').html('See Browser console for full output.');
});
 
request.fail(function( jqXHR, textStatus ) {
  alert( "Request failed: " + textStatus );
});
});


$('#List').click( function() { 
  $('#log').load("https://uptane.umtri.umich.edu:24515/director/List"); 
}); 

$('#Enroll').click( function() { 
  $.get('https://uptane.umtri.umich.edu:24515/director/Enroll', 0, function(data) { 
	$('#log').html(data); 
   }); 
}); 

