from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/test/trick', methods=['POST'])
def test_trick():
    payload = request.form.get('query')

    if len(payload) < 59:
        if 'import' in payload:
            return render_template('index.html', message="NICE TRY! We cant be hacked")
        try:
            output = eval(payload)
            return render_template('index.html', message=output)
        except:
            return render_template('index.html', message=f"beep boop beep: {payload}")
    return render_template('index.html', message="Oh it worked! SIKE!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
