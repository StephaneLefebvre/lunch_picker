#! /usr/bin/env python3
import json
import random


def method_1():
    """
    Method 1 is the easiest : random choice between the restaurants
    """
    data = json.load(open("restaurant_list.json"))
    return random.choice(data["restaurants"])

if __name__ == "__main__":
    print(method_1())
