#!/usr/bin/env python
import re, pyperclip

# Create a regex for phone numers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 1234, x12345

(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
((etx(\.)?\s|x)            # extension word-part (optional)
(\d{2,5}))?                # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# something_.+@something_.+.com

[a-zA-Z0-9_.+]+ # name part
@               # @ at symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the thext off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Extract the email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
