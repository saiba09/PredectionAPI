#!/usr/bin/env python
#
# Copyright 2012 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#        
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Marc Cohen
#

'''Implementation of prediction request API.'''
from __future__ import print_function

import argparse
import os
import pprint
import sys
import time
import httplib2
from google.appengine.ext import webapp
from apiclient.discovery import build
from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client

ERR_TAG = '<HttpError>'
ERR_END = '</HttpError>'

class PredictAPI(webapp.RequestHandler):

  '''This class handles Ajax prediction requests, i.e. not user initiated
     web sessions but remote procedure calls initiated from the Javascript
     client code running the browser.
  '''

  def post(self):
    service = build('prediction', 'v1.6')
    try:
      papi = service.trainedmodels()
      # Read server-side OAuth 2.0 credentials from datastore and
      # raise an exception if credentials not found.
      val = self.request.get('tweet').encode('utf-8')
      body = {'input': {'csvInstance': val}}
      result = papi.predict(body=body, id='mood-identifier-v1', project='moodanalysis-1402').execute()
      print('Prediction results for "%s"...' % val)
      pprint.pprint(result)
      self.response.out.write(json.dumps(ret))

    except Exception, err:
      err_str = str(err)
      if err_str[0:len(ERR_TAG)] != ERR_TAG:
        err_str = ERR_TAG + err_str + ERR_END
        self.response.out.write(err_str)
