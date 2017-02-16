/*
 * Copyright 2012 Google Inc.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * Author: Marc Cohen
 *
 */

// Global constants set here.
var PREDICT = 'predict';
var ERR_TAG = '<HttpError>';
var ERR_END = '</HttpError>';
var Chart_type = 'pie';
var Chart_rows = Array();

function response(resp) {

  $('#prediction_result').text("response came!");

}

// Launch a prediction request via AJAX.
/*function predictMood(tweet) {
  // Clear any current results chart, text and chart switching link.
  $('#results_chart').html('');
  $('#prediction_result').text('Obtaining prediction result...');
  $('#switch_chart_link').text('');

  // Build URI params containing selected model and input data.
  var uri = '/predict';


  //uri += model;

    //uri += '&' + escape(elem.id) + '=' + escape(elem.value);
  

  // Send the prediction call in a jQuery AJAX request. The response
  // will be fielded asynchronously by the response() callback function.
  $.ajax({
    url: uri,
    type: 'POST',
    data: data,
    dataType: 'text',
    success: [response]
  });
}
*/
$(document).ready(function(){

console.log("hi")

    function predictMood() {
	console.log("h2")

       $('#prediction_result').text('Obtaining prediction result...');

        var tweet = document.getElementById("tweet").value;
        var uri = '/predict';
       
	console.log("h3")

        $.ajax({
        url: uri,
        type: 'POST',
        data: {tweet : $('#tweet').val() },
        success:function(res){
		console.log("response")
		console.log(res)
                 $('#prediction_result').text(res);

	}
  });
    }
    $("#button-submit-clck").click(predictMood);
});
// Handle user changing selection in the model selection pull-down menu.

// Callback function called when Google Charts Javascript API is loaded.
// Not currently used but available for debugging purposes.


// Invoke this file's initialization function. This is the only line of


