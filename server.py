#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" Create and give the frontend to choose the restaurant """

import json
import requests
from flask import Flask, request

APP = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<style>
tr:hover {{
  background-color: cyan;
}}
</style>
<body>
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

</body>
</html>
"""

TABLE_ELT = """
<tr>
  <td><abbr title="{address} à ~{distance} min, pour {prices}€, c'est du {type}">{endroit}</abbr></td>
  <td><input type="radio" name="{endroit}" value=0 checked></td>
  <td><input type="radio" name="{endroit}" value=1></td>
  <td><input type="radio" name="{endroit}" value=2></td>
  <td><input type="radio" name="{endroit}" value=3></td>
  <td><input type="radio" name="{endroit}" value=4></td>
</tr>
"""

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

@APP.route("/")
def create_html_page(restaurant="real_restaurants"):
    """ Create the page where we can fill the ballot and vote """
    data = json.load(open("restaurant_list.json"))
    list_endroit = data[restaurant]
    supertable = ""
    for elt in list_endroit:
        supertable += TABLE_ELT.format(endroit=elt, **list_endroit[elt])
    return HTML_PAGE.format(table=supertable)


dict_result = {}

@APP.route("/vote", methods=["POST"])
def vote():
    """ Create the page that process the vote and where the result are displayed """
    dict_endroit = {}
    for restaurant in request.form:
        if request.form[restaurant] != "0":
            dict_endroit[restaurant] = request.form[restaurant]
    global dict_result
    dict_result[ip] = dict_endroit

    agregate_dict = {}
    for dict_endroit in dict_result.values():
        agregate_dict = {
            k: int(agregate_dict.get(k, 0)) + int(dict_endroit.get(k, 0))
            for k in set(agregate_dict) | set(dict_endroit)
        }

    winner = requests.post("http://127.0.0.1:7070/best", data=agregate_dict)
    return "Ton vote à été pris en compte, le vainqueur actuel est '{}'".format(winner.text)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080)
