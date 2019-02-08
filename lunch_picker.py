#! /usr/bin/env python3
"""
Various methods of election
It try to follow this checklist:
https://devchecklists.com/python-api-checklist/
"""

import random
import statistics


class LunchPicker(object):
    """ Object containing statics methods to be listed and called by the microservice """
    @staticmethod
    def elect(*args):
        """ meta call to elect winner of vote """
        if len(args) == 0:
            return  # should we raise an error ?
        if len(args) > 1:
            return LunchPicker.select(args) # should we raise an error ?
        if isinstance(args[0], dict):
            return LunchPicker.best(args[0])
        if isinstance(args[0], list) and isinstance(args[0][0], dict):
            return LunchPicker.best_of_dicts(args[0])
        raise ValueError


    @staticmethod
    def median(dict_endroit):
        """ choose the median """
        dict_notation = {}
        for key in dict_endroit:
            dict_notation[key] = statistics.median(dict_endroit[key])
        return LunchPicker.best(dict_notation)

    @staticmethod
    def best(dict_endroit):
        """ who has the best grade """
        return max(dict_endroit, key=(lambda key: dict_endroit[key]))

    @staticmethod
    def best_of_dicts(list_dict_endroits):
        """ take a list of options, sum them and return the best one """
        agregate_dict = {}
        for dict_endroit in list_dict_endroits:
            agregate_dict = {
                k: agregate_dict.get(k, 0) + dict_endroit.get(k, 0)
                for k in set(agregate_dict) | set(dict_endroit)
            }
        return LunchPicker.best(agregate_dict)
    
    def best_of_tuples(list_tuples_endroits):
        """ take a list of options as tuples and return the best one """
        return LunchPicker.best(dict((y, x) for x, y in list_tuples_endroits))

    @staticmethod
    def random(list_endroit):
        """ random choice between avaiable propositions """
        return random.choice(list_endroit)
