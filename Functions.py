def showPeoples(person):
    print(person)
    print(person['name'])
    print(person['apellido'])
showPeoples({
    "name": "Andres",
    "apellido": "Acero"
})
def optionalParams(person, business = None):
    if business:
        print(business)
    print(person)
optionalParams({
    "name": "Andres",
    "apellido": "Acero"
},True)
## Funciones Lambda son funciones pequeñas
## Tienen que ser de una linea
import datetime as date
actual_date = lambda year: f"Today is {year}"
print(actual_date(date.datetime.now()))

## comprobación de parametros

name = "andres"
## isinstance comprube si una variable es algun tipo
## de variable
is_about = isinstance(name, int)
print(is_about)
## para eliminar todos los espacios enun string
frase = " hola chao    adios   ".strip()
print(frase)
## eliminar una variable
del name

## arroja el tamaño de un objeto

print(len(frase))

## para buscar un elemento en un objeto
print(frase.find("adios"))

## para reemplazar en un string

new_frase = frase.replace("adios", "ya se va")

print(new_frase)
## para hacer lower y upper case

print(new_frase.lower())
print(new_frase.upper())


