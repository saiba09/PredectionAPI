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

  '''Render Home Page.'''

import os
import json
import logging
import pickle
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

  # NOTE: You need to edit the redirect URI into the Dev Console, and that value 
  # needs to be updated when you move from running this app locally to running
  # on Google App Engine (else you'll get a 'redirect_uri_mismatch' error).

  # Static configuation constants.


  class HomePage(webapp.RequestHandler):
    '''This class renders the main home page for the "Try Prediction" app.'''

    def post(self):
      '''Use the same logic for posts and gets.'''
      self.get()

    def get(self):
      '''Process get requests.'''
     
      
      self.response.out.write(template.render('home.html')
        
  def parse_json_file(file):
    '''Utility function to open, read, and parse the contents of
       a file containing text encoded as a JSON document, and
       return resulting json object to caller.
    '''
    f = open(file, 'r')
    json_str = f.read()
    f.close()
    return json.loads(json_str)
