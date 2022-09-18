import os
from flask import Flask, request,render_template

app = Flask(__name__)
import warnings
warnings.filterwarnings("ignore")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    name = request.args.get('name', 'World')
    return f'Hello {name}!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))