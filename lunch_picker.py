#! /usr/bin/env python3
""" Various methods of election """

import random
import statistics


class LunchPicker(object):
    """
    Object containing statics methods to be listed and called by the
    microservice
    """
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
    def best_of_many(list_dict_endroits):
        """ take a list of options, sum them and return the best one """
        agregate_dict = {}
        for dict_endroit in list_dict_endroits:
            agregate_dict = {
                k: agregate_dict.get(k, 0) + dict_endroit.get(k, 0)
                for k in set(agregate_dict) | set(dict_endroit)
            }
        return LunchPicker.best(agregate_dict)

    @staticmethod
    def random(list_endroit):
        """ random choice between avaiable propositions """
        return random.choice(list_endroit)
