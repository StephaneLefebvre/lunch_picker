#! /usr/bin/env python3
"""
Election as a microservice
Listen to port 7070
Allow route according to methods available in LunchPicker
The methods are given by the / with their name and documentation
"""

from flask import Flask, request
from lunch_picker import LunchPicker

APP = Flask(__name__)


@APP.route("/")
def list_avaiable():
    """ Dynamically list all method in LunchPicker object """
    available = []
    for key, obj in LunchPicker.__dict__.iteritems():
        if str(type(obj)) == "<type 'function'>":
            available.append(
                "- {}:{}".format(key, getattr(LunchPicker, key).__doc__).strip()
            )
    return "Methods available:\n{}".format(",\n".join(available))


@APP.route("/<method>", methods=["POST"])
def dispatch_method(method):
    """ Call the method given in url """
    return getattr(LunchPicker, method)(request.form)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=7070)
