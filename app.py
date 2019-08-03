from flask import Flask, Response, request, abort
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
        print(request.json)    
    return Response(json.dumps(request.json))

if __name__ == '__main__':
    app.run()
