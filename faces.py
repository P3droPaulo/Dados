import re


def one():
    one = ''' _______
|       |
|   o   |
|       |
 -------'''
    return one

def two():
    two = ''' _______
| o     |
|       |
|     o |
 -------'''
    return two

def three():
    three = ''' _______
| o     |
|   o   |
|     o |
 -------'''
    return three

def four(): 
    four = ''' _______
| o   o |
|       |
| o   o |
 -------'''
    return four 

def five():
    five = ''' _______
| o   o |
|   o   |
| o   o |
 -------'''
    return five

def six():
    six = ''' _______
| o   o |
| o   o |
| o   o |
 -------'''
    return six

def check(check):
    if not check.isdigit():
        if check in 'Yy':
            return True
        elif check in 'Nn':
            return False
        else:
            return True
    else:
        return True
    
