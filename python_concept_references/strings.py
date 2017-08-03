spam = 'hello world!'
print(spam.upper())
print(spam.lower())
print(spam.islower())
print(spam.isupper())

# isalpha - letters only?
# isalnum - alphpa numeric?
# isspace - single space?
# istitle - every first word capital after space?
print(spam.title())

# startswith('str') | endswith('str')

print('\n\n'.join(['cats','rats','bats'])) # joins list split by /n/n
print(spam.split(' '))
print(spam.rjust(15)) # right justifys letters and makes string len 15
# ljust(num)
print(spam.ljust(15, '*')) #adds * to right of str
print(spam.center(20, '+')) # centers text

#spam.strip() removes white space from string
#ltrip | rstrip justtifys which side to remove white space
spam.replace('e', 'XSA')
print(spam)
print(spam.replace('e', 'XSA'))
      
