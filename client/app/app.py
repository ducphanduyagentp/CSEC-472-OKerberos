from flask import *
import requests
import json
import hashlib
import sys

app = Flask(__name__)

def secretDecrypt(c, k):
    realKey = k * int(len(c) / len(k) + 1)
    realKey = realKey[:len(c)]
    return ''.join([chr(ord(x) ^ y) for x, y in zip(c, realKey)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yeet', methods=["POST"])
def yeet():
    username = request.form['username']
    password = request.form['password']
    d = { 'username': username, 'password': password }
    r = requests.post('http://lab3-auth-server/yeet', data=d)
    res = r.json()
    sys.stderr.write("Response from auth server: " + str(res) + '\n')
    if 'auth' in res and res['auth'] == 'fail':
        return 'Your creds sucks'
    elif 'res' in res:
        m = hashlib.sha256()
        m.update(bytes(password, 'utf-8'))
        k = m.digest()
        res = json.loads(secretDecrypt(res['res'], k))
        sys.stderr.write("Decrypted response from auth server: " + str(res) + '\n')
        token = res['token']
        r = requests.post('http://lab3-app-server/yeet', json={ 'token': token })
        return r.text
    else:
        return 'segfault'
    

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)
