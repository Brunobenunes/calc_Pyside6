import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')
SPECIAL_KEYS = r"^[<C=]"
ACCEPT_KEYS = r"^\d*\.?\d+([+\-*/^]\d*\.?\d+)*$"
ACCEPT_KEYS_GROUPS = r"^(\d*\.?\d+)([+\-*/^])(\d*\.?\d+)*$"



def isNumberOrDot(string):
    return bool(NUM_OR_DOT.search(string))


def numberEquation(string):
    if string in '+-/*^':
        return None, string, None
    result = re.match(ACCEPT_KEYS_GROUPS, string)
    left_number = result.group(1)
    operator = result.group(2)
    right_number = result.group(3)
    return left_number, operator, right_number

def onlyNumer(string):
    result = re.findall(r'\d+\.?\d*', string)
    return result[0]

def isSpecialKeys(string):
    specialKeys = re.compile(SPECIAL_KEYS)
    result = re.findall(specialKeys, string)
    return bool(result)