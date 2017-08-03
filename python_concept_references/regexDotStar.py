import re

beginsWithHelloRegex = re.compile(r'^Hello')

print(beginsWithHelloRegex.search('Hello there!'))

endsWithRegex = re.compile(r'world!?')

allDigitsRegex = re.compile(r'^\d+$') # must begin and end with this pattern (one or more digits)


# . wildcard character any character except newline

atRegex = re.compile(r'.at') # anything followed by at (.only get single char here)

atRegex = re.compile(r'.{1,2}at')

# .* any character at all

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

# .*? non-greedy match

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')

greedy = re.compile(r'<(.*)>')

prime = 'Serve the public. \nProtect the innocent.\nUpload the law.'

dotStar = re.compile(r'.*') # matches until newline(\n)
dotStar = re.compile(r'.*', re.DOTALL) # now will match newlines

vowelRegex = re.compile(r'[aeiou]', re.I) # ignore case!

