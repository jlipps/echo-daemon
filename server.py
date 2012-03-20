import requests
import os
import simplejson
import time
import datetime
import echoprint
from bottle import route, run, template, static_file
from listen import record
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
    return template('index', **tpl_p)

@route('/identify/')
def identify():
    samples = record(TMP_WAV)
    d = echoprint.codegen(samples)
    d['api_key'] = ECHONEST_API_KEY
    res = requests.get('http://developer.echonest.com/api/v4/song/identify', d).content
    return res
    # start_time = time.time()
    # tpl_p = {}
    # tpl_p['time'] = start_time
    # tpl_p['song'] = ''
    # tpl_p['artist'] = ''
    # tpl_p['album'] = ''
    # return tpl_p

run(host='localhost', port=8080)
