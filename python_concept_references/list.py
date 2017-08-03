spam = ['cat','bat','rat','elephant']

print(spam[-1]) # Starts from end of list
print(spam[1:3]) #Slice from 1 to 2 (3 not included like substr)
print(spam[:2])
print(str(len(spam)))
del spam[2] #unassignment statement
print(str(len(spam)))

print(list('Hello'))
print('howdy' in ['hello', 'hi','howdy'])
print('howdy' not in ['hello', 'hi','howdy'])
