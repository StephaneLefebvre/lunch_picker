#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" Create and give the frontend to choose the restaurant """

import json
import requests
from flask import Flask, request, send_from_directory
from random import randint, shuffle

APP = Flask(__name__)

FORMULAIRE = """
<form action="/vote" method="post">
<table>
<tr>
  <td></td>
  <td>&#9940;</td>
  <td>&#9785;</td>
  <td>&#9863;</td>
  <td>&#9786;</td>
  <td>&#9924;</td>
</tr>
{table}
</table>
  <input type="submit" value="Submit">
</form> 
"""

HTML_PAGE = open("lazy-load.html").read()

TABLE_ELT = """
<tr>
  <td><abbr title="{address} à ~{distance} min, pour {prices}€, c'est du {type}">{endroit}</abbr></td>
  <td><input type="radio" name="{endroit}" value=0></td>
  <td><input type="radio" name="{endroit}" value=1></td>
  <td><input type="radio" name="{endroit}" value=2 checked></td>
  <td><input type="radio" name="{endroit}" value=3></td>
  <td><input type="radio" name="{endroit}" value=4></td>
</tr>
"""

class ServeurState:
    """ To avoid using globals """
    __shared_state = {}
    dict_result = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

@APP.route("/")
def create_html_page(restaurant="real_restaurants"):
    """ Create the page where we can fill the ballot and vote """
    data = json.load(open("restaurant_list.json"))
    restaurant_dict = data[restaurant]
    list_endroit = list(restaurant_dict.keys())
    supertable = ""
    shuffle(list_endroit)
    for elt in list_endroit[0:20]:
        supertable += TABLE_ELT.format(endroit=elt, **restaurant_dict[elt])
    return HTML_PAGE.replace("$#@!FORMULAIRE!@#$", FORMULAIRE.format(table=supertable))

@APP.route("/<filename>")
def fullpage(filename):
    return open(filename).read()

@APP.route("/fullPage.js/dist/<filename>")
def dist(filename):
    return send_from_directory("fullPage.js/dist/", filename)

@APP.route("/imgs/<filename>")
def imgs(filename):
    return send_from_directory("imgs", filename)

@APP.route("/vote", methods=["POST"])
def vote():
    """ Create the page that process the vote and where the result are displayed """
    dict_endroit = {}
    for restaurant in request.form:
        if request.form[restaurant] != "2":  # optimize network load
            dict_endroit[restaurant] = request.form[restaurant]
    serveur_state = ServeurState()
    serveur_state.dict_result[request.remote_addr] = dict_endroit

    agregate_dict = {}
    for dict_endroit in serveur_state.dict_result.values():
        agregate_dict = {
            k: int(agregate_dict.get(k, 0)) + int(dict_endroit.get(k, 2))
            for k in set(agregate_dict) | set(dict_endroit)
        }

    winner = requests.post("http://127.0.0.1:7070/best", data=agregate_dict)
    return "Ton vote à été pris en compte, le vainqueur actuel est '{}' with relevant vote being : {}".format(winner.text, json.dumps(agregate_dict))

@APP.route("/vote", methods=["GET"])
def result():
    """ Create the page that process the vote and where the result are displayed """
    serveur_state = ServeurState()
    agregate_dict = {}
    for dict_endroit in serveur_state.dict_result.values():  # order problem here
        agregate_dict = {
            k: int(agregate_dict.get(k, 0)) + int(dict_endroit.get(k, 2))
            for k in set(agregate_dict) | set(dict_endroit)
        }

    winner = requests.post("http://127.0.0.1:7070/elect", data=agregate_dict)
    return "Ton vote à été pris en compte, le vainqueur actuel est '{}' with relevant vote being : {} and {}".format(winner.text, json.dumps(agregate_dict), json.dumps(serveur_state.dict_result))


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080)

