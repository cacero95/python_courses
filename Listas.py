"""
La diferenia entre una tupla y una lista
es que la lista se puede modificar los items
mientras que una tupla no
"""

movies = ["spider man", "batman", "halo origins"]

pelis = ('avatar', 'prince of persia')

movies[0] = 'spider man 3'
movies.append(True)
print(movies)
print(pelis)
print(pelis[-2]) # comienza de adelante hacia atras -1, -2 ....
print(pelis[1:3]) # rango de una lista
## para eliminar el contenido de una lista se usa
del movies[:]
print(pelis)

## para lista multidimensionales

tmp_list = [
    [
        1,2
    ],
    [
        3,4
    ]
]
print(tmp_list[0][1])
for tmp in tmp_list:
    print(tmp)
    print(tmp_list.index(tmp)) 
    for second_level in tmp:
        print(second_level)

## ternarios en python

results = 20 if 1==2 else 10
print(results)

## con el metodo sort se ordena una array

numbers = [2,1,4,5,3]

numbers.sort()
print(numbers)

## para insertar un elemento en una posición especifica

numbers.insert(len(numbers),6)
print(numbers)

# para darle la vuelta a un arreglo
numbers.reverse()

# para eliminar el primer elemento en un array

numbers.pop()
#eliminar un objeto segun el nombre 
numbers.remove(6)
print(numbers)

# para sabe si un elemento esta en una lista 
print(2 in numbers)
# dice la posicion del elemento dentro del array
print(numbers.index(2))
# cuantas veces aparece un elemento dentro de la lista
print(numbers.count(2))
# Para unir listas

numbers.extend([7,8,9,10])
print(numbers)

