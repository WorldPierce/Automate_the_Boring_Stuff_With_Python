import re

message = 'Call me 415-555-1234 or at 415-555-5312 sometime.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message) # store in a 'match object' search finds first occurance
print(mo.group()) # mo.group() prints text that matches
print(phoneNumRegex.findall(message)) # returns list of string matches


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

#( and ) denotes groups in regex if you want ( or ) must escape with \(

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#matches first pattern followed by one of suffixes
#mo.group(1) will give us the suffix
