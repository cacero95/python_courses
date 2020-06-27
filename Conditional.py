## For the use of contional is not supported the {}
## for add more conditions use the and | or
"""
compare operators
    == equal
    >  high
    <  low
    <= high or equal
    >= low or equal
    != different
"""
"""
logic operators
    and y
    cr  O
    !   refuse
    not no
"""

#--------------so------------------------#
if "rojo" == "Rojo":
    print('are the same')
else:
    print('are different')
if 1 == 1 and 2 == 2:
    print('is correct')
if 1 == 1 or 2 == 2:
    print('is correct')

## Week example

day = input('What is today: ')
if int(day) == 1:
    print('Monday')
elif int(day) == 2:
    print('Thursday')
elif int(day) == 3:
    print('Wensday')
elif int(day) == 4:
    print('Tuesday')
elif int(day) == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
else:
    print('Sunday')

## ternarios en python

results = 20 if 1==2 else 10