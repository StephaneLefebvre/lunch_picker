#! /usr/bin/env python3
import json
import random
import statistics
import operator


class LunchPicker:
    @staticmethod
    def median(dict_endroit):
        """ choose the median """
        for key in dict_endroit:
            dict_notation[key] = statistics.median(dict_endroit[key])
        return max(dict_notation, key=(lambda key: dict_notation[key]))

    @staticmethod
    def best(dict_endroit):
        """ who has the best grade """
        return max(dict_endroit, key=(lambda key: dict_endroit[key]))

    @staticmethod
    def random(dict_endroit):
        """ random choice between avaiable propositions """
        return random.choice(data[restaurant])

