eggs = {'name': 'Muphy', 'species':'cat' , 'age':'old'}

for k in eggs.keys():
    print(k)
    print(eggs[k])
for v in eggs.values():
    print(v)
for k,v in eggs.items():
    print(k, v)

# tries to get age, if not there return 0
if 'age' not in eggs.keys():
    eggs['age'] = 'unknown'

# does previes code in one line
# NOTE this just returns unknown or age, no assignment
eggs.get('age', 'unknown') 

# if you want assignment as well, if color exists it does nothing
eggs.setdefault('color','black')
