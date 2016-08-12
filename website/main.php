<html>
 <head>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js"   
          integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="   
          crossorigin="anonymous"></script>
  <link href='//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css' rel='stylesheet' />
  <link href='//uptane.umtri.umich.edu:3000/page.css' rel='stylesheet' type='text/css' />
  <link href='//fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext' 
          rel='stylesheet' type='text/css'>
  <title> Uptane Client Portal </title> 
 </head>
 <body>
   <h4> Uptane Client Portal </h4> 
    <hr /> 
     <div class="clientdata"> 
      Client: 
       <input type="text" id="serial_number" value="" /> 
       <input type="text" id="public_key" value="" /> 
       <select name="cryptography_method"> <option value="ed25519">ed25519</option></select> 
 
     </div> 
     <br /> 
   <input type="button" id="timestamp" value="timestamp" /> &nbsp;
   <input type="button" id="List" value="List Clients" /> &nbsp; 
   <input type="button" id="Enroll" value="Enroll Client" /> &nbsp; 
   <div id="response"></div> 
   <br />
   <div id="log"> log: </div> 
 </body>

  <script src="script.js"> 
  </script> 
</html>

