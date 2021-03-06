#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Google Prediction API

Command-line application that trains on your input data. This sample does
the same thing as the Hello Prediction! example. You might want to run
the setup.sh script to load the sample data to Google Storage.

Usage:
  $ python prediction.py "bucket/object" "model_id" "project_id"

You can also get help on all the command-line flags the program understands
by running:

  $ python prediction.py --help

To get detailed log output run:

  $ python prediction.py --logging_level=DEBUG
"""
from __future__ import print_function

__author__ = ('jcgregorio@google.com (Joe Gregorio), '
              'marccohen@google.com (Marc Cohen)')

import argparse
import os
import pprint
import sys
import time
import httplib2
from apiclient.discovery import build
from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client


# Time to wait (in seconds) between successive checks of training status.
SLEEP_TIME = 10


# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('object_name',
    help='Full Google Storage path of csv data (ex bucket/object)')
argparser.add_argument('model_id',
    help='Model Id of your choosing to name trained model')
argparser.add_argument('project_id',
    help='Project Id of your Google Cloud Project')


def print_header(line):
  '''Format and print header block sized to length of line'''
  header_str = '='
  header_line = header_str * len(line)
  print('\n' + header_line)
  print(line)
  print(header_line)


def main(argv):
  # If you previously ran this app with an earlier version of the API
  # or if you change the list of scopes below, revoke your app's permission
  # here: https://accounts.google.com/IssuedAuthSubTokens
  # Then re-run the app to re-authorize it.
  #  http = AppAssertionCredentials('https://www.googleapis.com/auth/prediction').authorize(httplib2.Http())
  service = build('prediction', 'v1.6')
  try:
    # Get access to the Prediction API.
    papi = service.trainedmodels()

    # List models.
    print_header('Fetching list of first ten models')
    result = papi.list(maxResults=10, project='moodanalysis-1402').execute()
    print('List results:')
    pprint.pprint(result['kind'])

    # Start training request on a data set.
    #print_header('Submitting model training request')
    #body = {'id': 'mood-identifier-v1', 'storageDataLocation': 'mood-predection/Mood_id.txt'}
    #start = papi.insert(body=body, project='moodanalysis-1402').execute()
    #print('Training results:')
    #pprint.pprint(start)

    # Wait for the training to complete.
    #print_header('Waiting for training to complete')
    #while True:
     # status = papi.get(id='mood-identifier-v1', project='moodanalysis-1402').execute()
      #state = status['trainingStatus']
      #print('Training state: ' + state)
      #if state == 'DONE':
       # break
      #elif state == 'RUNNING':
       # time.sleep(SLEEP_TIME)
        #continue
      #else:
       # raise Exception('Training Error: ' + state)

      # Job has completed.
      #print('Training completed:')
      #pprint.pprint(status)
      #break
      # Describe model.
    #print_header('Fetching model description')
    #result = papi.analyze(id='mood-identifier-v1', project='moodanalysis-1402').execute()
    #print('Analyze results:')
    #pprint.pprint(result)
    # Make some predictions using the newly trained model.
    print_header('Making some predictions')
    for sample_text in ['i am happy', 'on cloud 9']:
      body = {'input': {'csvInstance': [sample_text]}}
      result = papi.predict(
        body=body, id='mood-identifier-v1', project='moodanalysis-1402').execute()
      print('Prediction results for "%s"...' % sample_text)
      pprint.pprint(result['outputLabel'])
    print('-----------------------------'% sample_text)
    print('-----------------------------'% body) 
  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize.')


if __name__ == '__main__':
  main(sys.argv)

