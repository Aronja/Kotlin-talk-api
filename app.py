from flask import Flask, Response, request, abort
from parse_kotlin import parse_kotlin
from compile_kotlin import compile_kotlin
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/kotlin', methods=['POST'])
def parse_code():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        kotlin_file = parse_kotlin(request) 
        compile_kotlin(kotlin_file)
    return Response(json.dumps(request.json))

if __name__ == '__main__':
    app.run()
