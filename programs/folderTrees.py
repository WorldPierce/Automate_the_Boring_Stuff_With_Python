import os
import shutil

for folderName, subfolders, filenames in os.walk('c:\\users\\wffpi\\desktop'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are ' + str(subfolders))
    print('The filesnames in ' + folderName + ' are ' + str(filenames))

# delete all "fishy" folders
    for subfolder in subfolders:
        if 'fishy' in subfolder"
        # os.rmdir(subfolder) # consider dry run!

# backup all .py files
    for file in filenames:
        if file.endswith('.py'):
            # shutil.copy(os.path.join(folderName, file, os.path.join(folderName, file + '.backup')))
