////
//  Uptane Site Script
//
//   
//
/////////////////////////
// Globals

var serveraddress = "https://uptane.umtri.umich.edu:24515";

/////////////////////////

$('#timestamp').click(function(){
var nonce = [1,2,3]; 

var request = $.ajax({
  url: serveraddress + "/timeserver/",
  method: 'POST',
  processData: false,
  data: '[1,2,3]',
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
  $('#log').load(serveraddress + "/director/List"); 
}); 

$('#Enroll').click( function() { 
  $.get(serveraddress + '/director/Enroll', 
  { serial:$('#serial_number').val(), key:$('#public_key').val() }, 
  function(data) { 

	$('#log').html(data); 
  }); 
}); 

