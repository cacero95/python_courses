nombre = "Carlos Andres"
apellido = "Acero Sanchez"
print(f"{nombre} {apellido}")
"""
El format permite mandar parametros a {}
que esten dentro de un string
"""
print("Hola me llamo {} {} ".format(nombre,apellido))

"""
for known the type of variables on python use the type function
"""
print(type(1))
print(type("dos"))
print(type(True))
print(type(None))
print(type(1.757))
print(type(1.75774827483))
## for make the lists or the tuples

lists  = [1,2,34,54,]
tuples = ("hola", "Adios", "bienvenidos")

print(lists)
print(tuples)
print(type(lists))
print(type(tuples))

## the dictionaries are like json objects
dictionary = {
    "nombre": "Carlos",
    "last_name": "Acero"
}
print(dictionary)
print(type(dictionary))

## other type of variable are the ranges

rango = range(9)
print(rango)
print(type(rango))

data_bites = b"andres"
print(data_bites)
print(type(data_bites))
year = 25
## for convert variables for example a number to string for print the result

print(f" {nombre} {apellido} y tengo {str(year)} ")
print(f" {nombre} {apellido} y tengo {int(year)} ") # with the function int change the type of strings to integer
print(f" {nombre} {apellido} y tengo {float(year)} ") # with the function float change the type of strings to float
print(f" {nombre} \"{apellido}\" y tengo {float(year)} ") # with the \ escape the value on na string for that reason the last will have ""
print(f' {nombre} "{apellido}" y tengo {float(year)} ') # or only place '' for keep the ""
print(f' {nombre} \n "{apellido}" y tengo {float(year)} ') # \n jump the text below
print(f' {nombre} \r "{apellido}" y tengo {float(year)} ') # \r delete the text behind the \r

#increment operators

year = 2020
print(year)
year = year+1
print(year)
year = year-1
print(year)
year = 1+year
print(year)
year = 1-year
print(year)

## Board entry

name = input('What is your name: ')
print(name)

# exercise make the diferention between types of variables

def variableType(value, tiping):
    return True if isinstance(value, tiping) else type(value)

print(variableType((),int)) 
print(variableType("hola",str)) 
print(variableType("hola",bool)) 
print(variableType(12,float)) 
print(variableType(True,list)) 
print(variableType([],set)) 
print(variableType({},dict)) 


