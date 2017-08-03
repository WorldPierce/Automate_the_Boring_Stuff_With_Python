import shelve

helloFile = open('c:\\users\\wffpi\\hello.txt') # opens in read mode
content = helloFile.read()
# hellowFile.readlines() returns lists
helloFile.close()
# write overwrites content
helloFile = open('c:\\users\\wffpi\\hello.txt', 'w') # write mode
# ('a' for append) this doesn't overwrite
helloFile.write('Hello!!!!!!\n')
helloFile.close()

# shelve files lets you store lists and dicts and open later
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Chloe', 'Sophie', 'Muph']

list(shelfFile.keys()) # returns cats
list(shelfFile.values()) # returns values

shelfFile.close()

