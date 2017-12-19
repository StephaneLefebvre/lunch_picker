#! /usr/bin/env python3
import json
import random
import statistics
import operator


HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

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

</body>
</html>
"""

TABLE_ELT = """
<tr>
  <td>{endroit}</td>
  <form>
  <td><input type="radio" name="{endroit}" value=0 checked></td>
  <td><input type="radio" name="{endroit}" value=1></td>
  <td><input type="radio" name="{endroit}" value=2></td>
  <td><input type="radio" name="{endroit}" value=3></td>
  <td><input type="radio" name="{endroit}" value=4></td>
  </form>
</tr>
"""


def create_html_page(restaurant="fake_restaurants"):
    data = json.load(open("restaurant_list.json"))
    list_endroit = data[restaurant]
    supertable = ""
    for elt in list_endroit:
        supertable += TABLE_ELT.format(endroit=elt)
    print(HTML_PAGE.format(table=supertable))

def method_3(restaurant="fake_restaurants_notation"):
    """
    Methode to choose the median
    """
    data = json.load(open("restaurant_list.json"))
    dict_endroit = data[restaurant]
    dict_notation = {}
    for key in dict_endroit:
        dict_notation[key] = statistics.median(dict_endroit[key])
    return max(dict_notation, key=(lambda key: dict_notation[key]))

def method_2(restaurant="fake_restaurants_selection"):
    data = json.load(open("restaurant_list.json"))
    dict_endroit = data[restaurant]
    return max(dict_endroit, key=(lambda key: dict_endroit[key]))

def method_1(restaurant="fake_restaurants"):
    """
    Method 1 is the easiest : random choice between the restaurants
    """
    data = json.load(open("restaurant_list.json"))
    return random.choice(data[restaurant])

def test_methods():
    """
    test if code is ok
    """
    print(method_1())
    print(method_2())
    print(method_3())
def test_html():
    create_html_page()

if __name__ == "__main__":
    test_methods()
