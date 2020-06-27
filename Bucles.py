array = [1,2,3,4,5,6]
for contador in array:
    print(contador)
    ## para frenar un bucle
    if contador == 5:
        break
else:
    print('array finished')
while contador < array.__len__():
    contador+=1
    print(contador)
print("\n Jump")
for count in range(61):
    print(count**2)

range1 = int(input("Primer rango"))
range2 = int(input("Segundo rango"))

for follow in range(range1, range2):
    print(follow)

print("\n Jump")
for number in range(1,11):
    print(f"### table {number} ####")
    for number2 in range(1,11):
        print(number*number2)
## procentajes

number_porcentaje = int(input('Diga el numero '))
porcentaje = int(input(f'Diga el procentaje {number_porcentaje} '))

print(number_porcentaje*(porcentaje/100))