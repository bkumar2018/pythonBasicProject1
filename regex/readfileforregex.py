import re

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'[89]\d\d.\d\d\d.\d\d\d\d')

#birenkumar@bogusemail.com
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')   # general email validation

with open('sample.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)