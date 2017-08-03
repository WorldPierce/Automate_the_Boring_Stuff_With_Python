import copy
def eggs(param):
    cheese = copy.deepcopy(param)
    cheese.append('Hello')
    param.append('World')
    print(cheese)

spam = [1,2,3,4]
eggs(spam)
print(spam)
