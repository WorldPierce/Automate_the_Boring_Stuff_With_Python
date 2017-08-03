import re
nameRegex = re.compile(r'Agent \w+')

namesRegex.sub('REDACTED','Agent one, Agent two')
#replaces agent one and agent two

namesRegex = re.compile(r'Agent (\w)\w*') #just returns the group

namesRegex.sub(r'Agent \1****','Agent one, Agent two')
#this will replace second word (group one) with first letter and stars

#verdbose lets you add comments
re.compile(r'''
(\d\d\d)| # area code(without parens)
(\(\d\d\d\)) # area code with parens
-
\d\d\d
-
\d\d\d\d''',re.VERBOSE|re.IGNORECASE|re.DOTALL) # allows multiple options
