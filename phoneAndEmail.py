#!/usr/bin/env python
import pyperclip, re, sys

# Create a regex for phone numers
phoneRegex = re.compile(r'''(
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 1234, x12345

(\d{3}|\(\d{3}\))?              # area code (optional)
(\s|-|\.)?                      # first separator
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext\.)\s*\d{2,5})?   # extension number-part (optional)
)''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''(
# something_.+@something_.+.com

[a-zA-Z0-9._+-]+   # username
@                   # at symbol
[a-zA-Z0-9.-]+      # domain name
(\.[a-zA-Z]{2,4})   # top level domain
)''', re.VERBOSE)

if pyperclip.is_available == None:
    print("The clipboard is empty.")
    sys.exit(1)


# Get the thext off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allEmails = []
for email in extractedEmail:
    allEmails.append(email[0])

if len(allPhoneNumbers) == 0 and len(allEmails) == 0:
    print("No phone numbers or email addresses found.")
    sys.exit(1)

# Extract the email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmails)
pyperclip.copy(results)

