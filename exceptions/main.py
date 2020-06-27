# capture errors with python

try:
    name = input('what is your name: ')
    if len(name)>2:
        print(name)
except:
    print('Please review your name jajaj')
else:
    print('works good')
finally:
    print('out of here')

### In case of multiples errors

try:
    number = int(input('Type a number: '))
    number2 = int(input('Type a number2: '))
    print(number/number2)
## type into a Exception return the type of error
except Exception as e:
    print(f"type error", type(e).__name__)
    print(f"type error", type(e))
except ValueError as value:
    print('Only numbers', value)
except TypeError as typing:
    print('we need numbers', typing)
except ZeroDivisionError as zero:
    print('Zero division', zero)
else:
    print('Works good')
finally:
    print('get out of here')

### customize a exception

age = int(input('Whats your age: '))
if age < 0 or age > 200:
## with the raise reutrn a exception no matter which exception
    raise ValueError('Jajaja are you kidding me')
    raise TypeError('Jajaja are you kidding me')
