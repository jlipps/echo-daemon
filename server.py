import requests
import os
import simplejson
import time
import datetime
import echoprint
from bottle import route, run, template, static_file
from listen import *
# run with simplehttpd server

SYSTEM_PATH = os.path.abspath('/'.join(__file__.split('/')[:-1]))
STATIC_PATH = SYSTEM_PATH + '/static/'
TMP_WAV = SYSTEM_PATH + '/echoprint.wav'
ECHONEST_API_KEY = 'OQNVMPZI1VVMY7S7E'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_PATH)

@route('/')
def index():
    return template('index')

@route('/identify/')
def identify():
    record(TMP_WAV)
    d = echoprint.codegen(get_samples_from_file(TMP_WAV))
    endpoint = "http://developer.echonest.com/api/v4/song/identify"
    url = "%s?api_key=%s&code=%s" % (endpoint, ECHONEST_API_KEY, d['code'])
    r = requests.get(url)
    res = simplejson.loads(r.text)
    print res['response']
    return res['response']

run(host='localhost', port=8080)
