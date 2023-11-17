import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')


def isNumberOrDot(string):
    return bool(NUM_OR_DOT.search(string))