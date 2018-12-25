#! /usr/bin/env python3

import json
from flask import Flask, request
from lunch_picker import LunchPicker

app = Flask(__name__)

@app.route("/")
def list_avaiable():
    available = []
    for key, obj in LunchPicker.__dict__.iteritems():
        if str(type(obj)) == "<type 'function'>":
            available.append("- {}:{}".format(key, getattr(LunchPicker, key).__doc__).strip())
    return 'Methods available:\n{}'.format(',\n'.join(available))


@app.route('/<method>', methods=["POST"])
def dispatch_method(method):
    return getattr(LunchPicker, method)(request.form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)
