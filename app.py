import os, sys, codecs, yaml, ioutils, yaml
from flask import Flask, flash, request, redirect, url_for, send_from_directory, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from flask import json
import uuid

app = Flask(__name__)
CORS(app)
app.config['APP_REFS'] = {}
refFilePath = os.path.join(os.getcwd(), 'appref.yaml')

if os.path.exists(refFilePath):
    app.config['APP_REFS'] = ioutils.loadYaml(refFilePath)


DIR_COLLECTIONS = os.path.join(os.getcwd(), 'collections')
### init
if not os.path.exists(DIR_COLLECTIONS):
    os.makedirs(DIR_COLLECTIONS)


@app.route('/', methods=['GET'])
@cross_origin(origin='localhost')
def index():
    appFolder = os.getcwd()
    return 'Welcome to Project001'
#############################################
##### GET SERVER LIST
@app.route('/servers', methods=['GET'])
@cross_origin(origin='localhost')
def servers_get():
    print('\n get servers list')
    fp = os.path.join(DIR_COLLECTIONS, 'servers.txt')
    if os.path.exists(fp):
        raw = ioutils.loadText(fp)
        jsonStr = decode(raw)
    return '[]'

if __name__ == "__main__":
    serverConfig = { 'file_root': os.getcwd(), 'port' : 5200 }
    configFile = os.path.join(os.getcwd(), 'server_config.json')
    
    if os.path.exists(configFile):
        f = open(configFile)
        content = f.read()
        f.close()
        serverConfig = json.loads(content)
    
    print(json.dumps(serverConfig))
    app.run(port=serverConfig['port'])