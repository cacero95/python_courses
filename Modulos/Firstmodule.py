import datetime as date
import math
import random
## Date modules
def actualDate():
    return date.datetime.now()
def today():
    return date.date.today()
def mes():
    return f"{date.datetime.today().month} {date.datetime.today().day} {date.datetime.today().year}"
def customise_date():
    return date.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
def timestamp():
    return date.datetime.today().timestamp()
def time():
    return date.datetime.today().time()
#####################################
"""
Math modules
"""

def math_functions():
    pi_number = math.pi
    sqrt = math.sqrt(10)
    redondear = math.floor(3.4)
    rand = random.randint(1,100)
    return f"------------------\
            \nMath Modules\nPI:{pi_number}\nraiz:{sqrt}\nredondear_Alpiso:{redondear}\naleatorio:{rand} "

