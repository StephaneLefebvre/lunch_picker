#! /usr/bin/env python3
import json
import random
import statistics

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

def method_3(restaurant="fake_restaurants_vote"):
    """
    Methode to choose the median
    """
    data = json.load(open("restaurant_list.json"))
    dict_endroit = data[restaurant]
    for key in dict_endroit:
        print(key, str(statistics.median(dict_endroit[key])))

def method_1(restaurant="fake_restaurants"):
    """
    Method 1 is the easiest : random choice between the restaurants
    """
    data = json.load(open("restaurant_list.json"))
    return random.choice(data[restaurant])

def test():
    """
    test if code is ok
    """
    print(method_1())
    method_3()
    create_html_page()

if __name__ == "__main__":
    test()
