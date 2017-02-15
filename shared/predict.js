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

// Toggle between pie and bar charts.

// Render results chart based on data received from AJAX call.

// Process AJAX response. This is the respond from the app engine's predict
// method, which simply passes the JSON encoded response from the prediction
// API call run on the server, so we can assume this response looks exactly
// like what we would see if made the prediction call directly, with one
// exception: errors are wrapped in a special HttpError tag to make it
// easy to distinguish them on the client side.
function response(resp) {
  err_tag_len = ERR_TAG.length;
  if (resp.substr(0, err_tag_len) == ERR_TAG) {
    // We received an error - display the error to the user and return.
    // The following substr() peels off the leading and trailing <HttpError>
    // tags for user-friendly presentation of the contained error message.
    err_str = resp.substr(err_tag_len, resp.length - (err_tag_len * 2) - 1);
    $('#prediction_result').text('ERROR:' + err_str);
    return;
  }

  // We got a successful response. Parse the JSON text and interpret content.
  var obj = JSON.parse(resp);
  if ('kind' in obj) {
    if (obj['kind'] == 'prediction#output') {
      result = 'unknown';
      if ('outputLabel' in obj) {
        // An outputLabel means we have a classification result.
        result = obj['outputLabel'];
      } else if ('outputValue' in obj) {
        // An outputValue means we have a regression result.
        result = obj['outputValue'];
      }
  } else {
    // Unparsable response not enveloped by an HttpError tag -
    // flag as error and display reponse to aid debugging.
    alert('failed request: ' + resp);
  }
}

// Launch a prediction request via AJAX.
function predict(tweet) {
  // Clear any current results chart, text and chart switching link.
  $('#results_chart').html('');
  $('#prediction_result').text('Obtaining prediction result...');
  $('#switch_chart_link').text('');

  // Build URI params containing selected model and input data.
  var uri = '/predict';
  var data = {}
  data['tweet'] = tweet;

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

// Handle user changing selection in the model selection pull-down menu.

// Callback function called when Google Charts Javascript API is loaded.
// Not currently used but available for debugging purposes.


// Invoke this file's initialization function. This is the only line of


