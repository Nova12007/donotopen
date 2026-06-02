import math
from datetime import datetime


def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"


def get_time():
    return datetime.now().strftime("%H:%M:%S")