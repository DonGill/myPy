# ================================================================================================ #
# Project: myPyTookkit.py                                                                          #
# Version: 0.42                                                                                    #
# Lst Mod: 09.09.2016                                                                              #
# Author: Don Gill                                                                                 #
# ================================================================================================ #
# A personal collection of helper functions used in various programs

# TODO: These functions should be generalized and then some error logic applied.

def double_digit_date (date_to_pad):
    '''returns a padded string date format where the month and day are two digits'''
    tmp_return = _padNum(date_to_pad.year, False)
    tmp_return += _padNum(date_to_pad.month, True)
    tmp_return += _padNum(date_to_pad.day, True)
    return tmp_return

def _padNum (num, needs_itterator):
    '''private function called by double_digit date to structure the date format as desired'''
    tmp_return = ''
    if needs_itterator:
        tmp_return = '.'

    if num < 10:
        return tmp_return + '0' + str(num)
    else:
        return tmp_return + str(num)
