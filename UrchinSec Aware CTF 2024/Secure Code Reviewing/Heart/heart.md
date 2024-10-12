# Heart - 100 points

## Description

Review the code below and identify the vulnerability:

```python=
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/name/<input_name>', methods=['GET'])
def say_name(input_name):
    if request.method == 'GET':
        if input_name is not None:
            return render_template_string(f"Hello {input_name}")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)
```

    Flag Format : urchinsec{line_number_of_vulnerable_code_vulnerability_name}
    Example : urchinsec{1_XSS}

# Flag

**urchinsec{9_SSTI}**