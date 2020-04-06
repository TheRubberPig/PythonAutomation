import re, pyperclip

# Number Regexs
mobilePhoneRegEx = re.compile(r'(07\d{9})')
landlineRegEx = re.compile(r'''(
0\d{4}
(\s)?
\d{6}
)''', re.VERBOSE)

# Email Regex
emailRegEx = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-z]{2,4})
)''', re.VERBOSE)

#Find Matches in cliboard text
text = str(pyperclip.paste())
matches = []

for groups in mobilePhoneRegEx.findall(text):
    matches.append(groups[0])

for groups in landlineRegEx.findall(text):
    phoneNumber = groups[0] + ' ' + groups[1]
    matches.append(phoneNumber)

for groups in emailRegEx.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')