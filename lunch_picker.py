#! /usr/bin/env python3
import json
import random
import statistics
import operator

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
    """
    Who as the best grade
    """
    data = json.load(open("restaurant_list.json"))
    dict_endroit = data[restaurant]
    return max(dict_endroit, key=(lambda key: dict_endroit[key]))

def method_1(restaurant="fake_restaurants"):
    """
    Method 1 is the easiest : random choice between the restaurants
    """
    data = json.load(open("restaurant_list.json"))
    return random.choice(data[restaurant])

def best_grade(dict_endroit)
    return max(dict_endroit, key=(lambda key: dict_endroit[key]))