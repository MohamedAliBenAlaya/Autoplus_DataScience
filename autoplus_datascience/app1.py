from flask import Flask, request
import json
import requests

app = Flask(__name__)


@app.route('/api/foo/', methods=['GET'])
def foo():
    bar = request.args.to_dict()
    #japp_json = json.dumps(bar)

    response = app.response_class(
        response=json.dumps(bar),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':   
    app.run(debug=True)