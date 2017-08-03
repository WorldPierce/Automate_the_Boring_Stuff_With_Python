#! python3
import re, pyperclip
# Create regex object for phone numbers
phoneRegex = re.compile(r'''
# 000-000-0000, 000-0000, (000) 000-0000, 000-000 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)        # first separator
\d\d\d       # first 3 digits
-        # separator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)        # extension word (optional)
(\d{2,5}))?   #extension number (opotional)
)
''', re.VERBOSE)
# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+  # name part (don't have to escape dots and plus in brackets
@    # @ symbol
[a-zA-Z0-9_.+]+   # domain part
''',re.VERBOSE)
# Get text off the clipboard
text = pyperclip.paste()
# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)
# print(extractedEmail)
# Copy the extracter email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
