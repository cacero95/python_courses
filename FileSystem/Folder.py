import os
import shutil
folder = os.path.abspath("./MyFolder")
## comprobate and create a folder
os.mkdir(folder) if not os.path.isdir(folder) else print('folder already exists')
#for copy a folder
shutil.copytree(folder,"./second_copy")
#delete a folder
shutil.rmtree("./second_copy")
#os.rmdir("./second_copy") this only delete the folder ignore the tree into the folder
# fot list the content of a folder
print('---------------------\n-----------------\n')
content = os.listdir(folder)
print(content)