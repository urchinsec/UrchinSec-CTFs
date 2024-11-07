from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome Home!"

@app.route('/flag', methods=['GET'])
def flag():
    if request.headers['Accept-Language'] != "sw-TZ":
        return "You are not allowed here!", 403
    else:
        return "urchinsec{nilijua_tu_utakuwa_unafahamu!}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)