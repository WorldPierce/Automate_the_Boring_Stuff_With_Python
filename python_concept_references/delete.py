import os
# "DRY RUN" test what files you are going to delete
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink('filename') - deletes files
        print(filename)

# can pip install send2trash to move files to trash instead of permanintly deletes
