import shutil

shutil.copy('source file', 'destination\\folder\\newName')
shutil.copytree('source folder','dest folder') # copies entire folder and contents to new destination
shutil.move('source folder','dest folder') # moves file(if you go to same folder you can rename)
