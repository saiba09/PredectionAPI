#!/usr/bin/env python


'''Configures all page handlers for the application.'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask, render_template, request,url_for
import argparse
import logging
import os
import pprint
import sys
import time
import httplib2
from apiclient.discovery import build
from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client



app = Flask(__name__)


@app.route('/')
def mainPage():
	return render_template('home.html')
@app.route('/predict', methods=['POST'])
def prediction():
        ERR_TAG = '<HttpError>'
        ERR_END = '</HttpError>'
	
        service = build('prediction', 'v1.6')
	try:
		papi = service.trainedmodels()
		val = request.form['tweet']
		body = {'input': {'csvInstance': [val] }}
		result = papi.predict(body=body, id='mood-identifier-v1', project='moodanalysis-1402').execute()
	  	#result = "Happy!!"
		return  result
	except Exception, err:
		err_str = str(err)
		if err_str[0:len(ERR_TAG)] != ERR_TAG:
			err_str = ERR_TAG + err_str + ERR_END
			return  err_str



@app.errorhandler(500)
def server_error(e):
# Log the error and stacktrace.
	logging.exception('An error occurred during a request.')
	return 'An internal error occurred.', 500


