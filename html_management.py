#! /usr/bin/env python3

import requests
import json
from flask import Flask, request

app = Flask(__name__)

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


@app.route("/")
def create_html_page(restaurant="real_restaurants"):
    data = json.load(open("restaurant_list.json"))
    list_endroit = data[restaurant]
    supertable = ""
    for elt in list_endroit:
        supertable += TABLE_ELT.format(endroit=elt, **list_endroit[elt])
    return HTML_PAGE.format(table=supertable)


@app.route("/vote", methods=["POST"])
def vote():
    dict_endroit = {}
    for restaurant in request.form:
        if request.form[restaurant] != "0":
            dict_endroit[restaurant] = request.form[restaurant]
    result = max(dict_endroit, key=(lambda key: dict_endroit[key]))
    r = requests.post("http://127.0.0.1:7070/best", data=dict_endroit)
    return "Ton vote à été pris en compte, le vainqueur actuel est '{}'".format(r.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
