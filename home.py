  #!/usr/bin/env python

'''Render Home Page.'''

import os
import json
import logging
import pickle
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

  


class HomePage(webapp.RequestHandler):
  '''This class renders the main home page for the "Try Prediction" app.'''

  def post(self):
    '''Use the same logic for posts and gets.'''
    self.get()

  def get(self):
    '''Process get requests.'''
    self.response.out.write(template.render('home.html'))



  
  

