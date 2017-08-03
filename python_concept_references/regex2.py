import re

# ? - match preceding group 0 or 1 times

batRegex = re.compile(r'Bat(wo)?man') #wo can match 0 or 1 times the rest must match
mo = batRegex.search('The adventrues of Batman and Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('432-2343')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man') # * matches 0 or more times
mo = batRegex.search('The adventrues of Batman and Batwowowowowoman')
print(mo.group())

# + group before plus must appear 1 or more times
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventrues of Batman and Batwowowowowoman')
print(mo.group())


heRegex = re.compile(r'(Ha){3, 5}') # matches range between 3 and 5 Ha's in a row


digitRegex = re.compile(r'(\d){3,5}?') # non-greedy regex will match 3 before 5
#if you omit ? you will match 5 (greedy match) if you have 5 digits in a row

regexObj = re.compile(r'[^aeiouAEIOU]') # ^ is not for regex
