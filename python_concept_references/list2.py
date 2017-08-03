print(str(list(range(0,100,2))))

cat = ['fat','Orange','loud']
size, color, disposition = cat #muliple assignments
print(size)
print(color)
print(disposition)

size, color = color, size # easy swap

print(size)
print(color)
cat.sort() # sorts in alphabetical with capitals first
print('sorted :' + str(cat))
cat.sort(key=str.lower) #sorts in true alphbetical order
print('sort with key=str.lower: ' + str(cat))


spam = ['hi','jello','hello']
print('index of jello: ' + str(spam.index('jello')))
spam.append('hehrehr')
spam.insert(0,'first')
print('Append and insert at 0 :' + str(spam))
spam.remove('hi')
print('spam.remove(\'hi\'): ' + str(spam))
del spam[1]
print('del spam[1]: ' + str(spam))
