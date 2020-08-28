# -*- coding: utf-8 -*-

# Check whether a varible is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
