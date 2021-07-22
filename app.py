import logging
from flask import Flask, json, request
app = Flask(__name__)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, filename='app.log', level=logging.DEBUG)

@app.before_first_request
def before_request():
    app.logger.info(f'{request.path} endpoint was reached')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    res = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json"
    )
    return res

@app.route("/metrics")
def metrics():
    res = app.response_class(
        response=json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype="application/json"
    )
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0')
