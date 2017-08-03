import pprint
message = 'It was a bright cold dat in April, and the clocks were stricking thriteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)
pprint.pprint(count) # pretty print to order characters alphabetically
string = pprint.pformat(count) # allows you to handle as string
print(string)
