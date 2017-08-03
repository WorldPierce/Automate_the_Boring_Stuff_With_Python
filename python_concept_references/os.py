import os
# this figures out your os and joins with appropriate \ for windows or / for amc or linux
os.path.join('folder1', 'folder2','forlder3','file.png')

os.getcwd() # gets current working directory

os.chdir('c:\\') # changes dir

os.path.abspath('spam.png') # returns absolute file path

os.path.isabs() # returns true for absolute paths
os.path.relpath(,) # gives you relative path to first arg from second arg
os.path.dirname() # gives dir of path
os.path.basename() # find file name
os.path.exists() # does path exist?
os.path.isfile()
os.path.isdir()
os.path.getsize()
os.listdir('path') # returns list of strings inside folder

totalsize = 0
for filename in os.listdir('c:\\users'):
    if not os.path.isfile(os.path.join('c:\\users',filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\users',filename))


os.makedirs('c:\\path\\and\\folders\\to\\create') # makes this path
