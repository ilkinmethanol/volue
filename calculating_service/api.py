from os import name
import flask
from flask import request
from connection import *
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

c = Calculator(collection)

@app.route('/api/<customer>', methods=['GET'])
def main(customer):
    ts_to = None
    ts_from = None
    if request.args:
        try:
            ts_from = int(request.args.get('from'))
            ts_to = int(request.args.get('to'))
        except Exception as e:
            print(e)
            return app.response_class(response=json.dumps({"error":"Please provide correct timestamp data"}),status=404,mimetype='application/json')

    results = c.get_customer_data(name=customer, ts_from=ts_from, ts_to=ts_to)
    calculated = c.value_operations(results)

    response = app.response_class(response=json.dumps(calculated),status=200,mimetype='application/json')
    return response

app.run()
