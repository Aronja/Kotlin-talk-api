from flask import Flask, Response, request, abort
import json

from process_kotlin import process_kotlin


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/kotlin', methods=['POST'])
def parse_code():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        response = process_kotlin(request)
    return Response(response)  


if __name__ == '__main__':
    app.run()

