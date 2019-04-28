from flask import *
import requests
import json
import hashlib
import sys

app = Flask(__name__)

def secretEncrypt(c, k):
    realKey = k * int(len(c) / len(k) + 1)
    realKey = realKey[:len(c)]
    return ''.join([chr(ord(x) ^ y) for x, y in zip(c, realKey)])

@app.route('/')
def index():
    return 'yeet me. I\'m your yeet server'

@app.route('/yeet', methods=["POST"])
def yeet():
    username = request.form['username']
    password = request.form['password']
    auth = requests.auth.HTTPBasicAuth(username, password)
    d = { 'grant_type' : 'client_credentials' }
    r = requests.post('http://lab3-oauth-provider/token.php', data=d, auth=auth)
    res = r.json()
    sys.stderr.write("Response from oauth provider: " + str(res) + '\n')
    if r.status_code == 400:
        return jsonify(auth='fail', token='')
    if 'access_token' in res:
        m = hashlib.sha256()
        m.update(bytes(password, 'utf-8'))
        k = m.digest()
        token = secretEncrypt(r.text, b'YEET')
        newRes = json.dumps({ 'auth': 'success', 'token': token})
        newRes = secretEncrypt(newRes, k)
        return jsonify(res=newRes)
    else:
        return 'segfault'

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)
