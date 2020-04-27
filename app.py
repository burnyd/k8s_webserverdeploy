from flask import Flask, request, send_from_directory, url_for, jsonify
import socket
import os
import json
import platform


app = Flask(__name__, static_url_path='/static')

@app.route('/info')
def example():
   hostname = socket.gethostname()
   operating_system = platform.platform()
   source = request.remote_addr
   return('hello from ' + hostname + ' with operating system of ' + operating_system )

@app.route('/api/<path:filename>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api(filename):
    cwd = os.getcwd() #Get current working directory
    if request.method == 'GET':
        with open(cwd+"/"+filename, "r") as f:
            return f.read()
            f.close()

    if request.headers['Content-Type'] == 'application/json':
        with open(cwd+"/"+filename, "r") as f:
            return f.read()
            f.close()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


#static/allvars.json
