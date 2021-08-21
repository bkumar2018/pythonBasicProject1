import re

#email validation
emails= '''
BirenMaster@gmail.com
Abhi.Singh@university.edu
Ramesh-321-Patt@my-work.net
'''

#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')   # email matches with '.com'
# pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')   # email matches with '.com' and 'edu'
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-]+\.(com|edu|net)')   # email matches with - digit and all .coms

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')   # general email validation

matches = pattern.finditer(emails)
for match in matches:
    print(match)