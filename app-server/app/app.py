from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yeet', methods=["POST"])
def yeet():
    return 'yeet'

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)
