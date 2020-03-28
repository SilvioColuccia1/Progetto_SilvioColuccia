$( document ).ready(function() {
//adding listener on click event on submit button
$( "#polarity" ).click(function() {
 console.log( "Sending request." );
    polarity = 'true'
    irony = 'false'
    sarcasm = 'false'
    subjectivity = 'false'
    input_string = $('#input_string').val();
    request_data = { input_string: input_string, polarity: polarity, irony: irony, sarcasm: sarcasm, subjectivity: subjectivity};

    success_div = $('#success_alert');
    error_div = $('#error_alert');

  var request = $.get( "http://127.0.0.1:5000/callmodel", request_data, function(resp) {
      console.log( "success " + resp );
      success_div.html(JSON.stringify(resp));
      error_div.hide();
      success_div.show();
  })
   /*.done(function(resp) {
     console.log( "success " + resp );
   })*/
   .fail(function(resp) {
     console.log( "error " + resp );
        error_div.show();
        success_div.hide();
   })
   /*.always(function() {
     console.log( "success" );
   });*/
});

$( "#irony" ).click(function() {
 console.log( "Sending request." );
    polarity = 'false'
    irony = 'true'
    sarcasm = 'false'
    subjectivity = 'false'
    input_string = $('#input_string').val();
    request_data = { input_string: input_string, polarity: polarity, irony: irony, sarcasm: sarcasm, subjectivity: subjectivity};

    success_div = $('#success_alert');
    error_div = $('#error_alert');

  var request = $.get( "http://127.0.0.1:5000/callmodel", request_data, function(resp) {
      console.log( "success " + resp );
      success_div.html(JSON.stringify(resp));
      error_div.hide();
      success_div.show();
  })
   /*.done(function(resp) {
     console.log( "success " + resp );
   })*/
   .fail(function(resp) {
     console.log( "error " + resp );
        error_div.show();
        success_div.hide();
   })
   /*.always(function() {
     console.log( "success" );
   });*/
});

$( "#sarcasm" ).click(function() {
 console.log( "Sending request." );
    polarity = 'false'
    irony = 'false'
    sarcasm = 'true'
    subjectivity = 'false'
    input_string = $('#input_string').val();
    request_data = { input_string: input_string, polarity: polarity, irony: irony, sarcasm: sarcasm, subjectivity: subjectivity};

    success_div = $('#success_alert');
    error_div = $('#error_alert');

  var request = $.get( "http://127.0.0.1:5000/callmodel", request_data, function(resp) {
      console.log( "success " + resp );
      success_div.html(JSON.stringify(resp));
      error_div.hide();
      success_div.show();
  })
   /*.done(function(resp) {
     console.log( "success " + resp );
   })*/
   .fail(function(resp) {
     console.log( "error " + resp );
        error_div.show();
        success_div.hide();
   })
   /*.always(function() {
     console.log( "success" );
   });*/
});

$( "#subjectivity" ).click(function() {
 console.log( "Sending request." );
    polarity = 'false'
    irony = 'false'
    sarcasm = 'false'
    subjectivity = 'true'
    input_string = $('#input_string').val();
    request_data = { input_string: input_string, polarity: polarity, irony: irony, sarcasm: sarcasm, subjectivity: subjectivity};

    success_div = $('#success_alert');
    error_div = $('#error_alert');

  var request = $.get( "http://127.0.0.1:5000/callmodel", request_data, function(resp) {
      console.log( "success " + resp );
      success_div.html(JSON.stringify(resp));
      error_div.hide();
      success_div.show();
  })
   /*.done(function(resp) {
     console.log( "success " + resp );
   })*/
   .fail(function(resp) {
     console.log( "error " + resp );
        error_div.show();
        success_div.hide();
   })
   /*.always(function() {
     console.log( "success" );
   });*/
});

$( "#alldimensions" ).click(function() {
 console.log( "Sending request." );
    polarity = 'true'
    irony = 'true'
    sarcasm = 'true'
    subjectivity = 'true'
    input_string = $('#input_string').val();
    request_data = { input_string: input_string, polarity: polarity, irony: irony, sarcasm: sarcasm, subjectivity: subjectivity};

    success_div = $('#success_alert');
    error_div = $('#error_alert');

  var request = $.get( "http://127.0.0.1:5000/callmodel", request_data, function(resp) {
      console.log( "success " + resp );
      success_div.html(JSON.stringify(resp));
      error_div.hide();
      success_div.show();
  })
   /*.done(function(resp) {
     console.log( "success " + resp );
   })*/
   .fail(function(resp) {
     console.log( "error " + resp );
        error_div.show();
        success_div.hide();
   })
   /*.always(function() {
     console.log( "success" );
   });*/
});


})