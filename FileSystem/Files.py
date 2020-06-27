from io import open
## con el pathlib coge la ruta absoluta de la pc
import pathlib
import shutil
import os
import os.path
import requests
# file open
folder = str(pathlib.Path().absolute()) + "/FileSystem/assets/"
path = folder + "first.txt"
file = open(path, "a+")
#write a file
file.write("******* Here is your txt python***********\n")
#close file

file.close()

# read a file
file = open(path, "r")
# file.read() read all the file and return all in a object
# read by lines this face a convert to a list
content_lines = file.readlines()

for lines in content_lines:
    if not lines.isnumeric():
        print(lines.center(50))
## with the method center centered the text according the param
file.close()

## at the case of copy file first param old path, second new path

shutil.copy(path,folder+"second.txt")
##shutil.copy(path,folder+"../second.txt") out of the folder

"""
Move a file
"""
shutil.move(path,folder+"second.txt")

"""
Delete a file
"""
## other way for abstract the absolute path
print(os.path.abspath("./"))
if os.path.isfile(folder+"second.txt"):
    os.remove(folder+"second.txt")
# a esay way to comprobate if a file exists
os.remove(folder+"second.txt") if os.path.isfile(folder+"second.txt") else print('File does not exist')

# download images

url_imagen = "https://golang.org/doc/gopher/appenginegophercolor.jpg" # El link de la imagen
nombre_local_imagen = "go.jpg" # El nombre con el que queremos guardarla
imagen = requests.get(url_imagen).content
with open(nombre_local_imagen, 'wb') as handler:
	handler.write(imagen)
