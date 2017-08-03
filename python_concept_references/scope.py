spam = 42 #global scope var

def eggs():
    global spam # makes spam = global scope spam
    spam = 0 # local variable
eggs()
print(spam)
