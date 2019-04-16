from flask import *
import json

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
    token = request.get_json()
    if 'token' in token:
        token = token['token']
        token = secretDecrypt(token, b'YEET')
        token = json.loads(token)
        print(token)
        if 'access_token' in token:
            return 'you are granted the yeet power'
        else:
            return 'you tried to yeet me? how dare you?'
    else:
        return 'yeet off!'

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)
