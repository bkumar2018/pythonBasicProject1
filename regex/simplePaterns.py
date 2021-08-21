import re

#multi line string
text_to_serach = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

google.com

321-555-4321
321--555---4321
123.555.3213

123-666.3453
123.999.4233
321*111*4233

800.999.4233
900.999.4233


Mr. Singh
Mr Suraj
Ms Sharma
Mrs. Verma
Mr. T

cat
mat
pat
bat

'''

sentance = 'Start a sentence and then bring it to an end'

## ? what raw string Is?
# print('\tTab')  # backslash is shown
# print(r'\tTab')  #This is raw string : backslash is nolonger available


# pattern = re.compile(r'abc')  # search for 'abc'
# pattern = re.compile(r'cba')  #no match for cba
# pattern = re.compile(r'.')  #matches almost everything
# pattern = re.compile(r'\.')   #matches period .?
# pattern = re.compile(r'google\.com')

# pattern = re.compile(r'\d')  #matches all digits 0 to 9
# pattern = re.compile(r'\D')   #not a digit 0 to 9, all macthes no digit
# pattern = re.compile(r'\w')   # match any word char, i.e all lower upper digit letter,
# pattern = re.compile(r'\W')   #these are not a word char, no letter lower upper digit
#pattern = re.compile(r'\W')
#pattern = re.compile(r'\s')   #matches space
# pattern = re.compile(r'\S')   #matches all, not space

# pattern = re.compile(r'\bHa')   #matches word boundary 'Ha HaHa'   ---- 'Ha Ha  '
# pattern = re.compile(r'\BHa')   #matches not word boundary  'Ha HaHa'   ---- '    Ha'

# pattern = re.compile(r'\d\d\d')   # all combination of 3 digits
# pattern = re.compile(r'\d\d\d.')  # macth period . as well
# pattern = re.compile(r'\d\d\d.\d\d\d')   #match all combinations of 3digits with . and -
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

#Charcter set   --- macthes one char only use '+' for more char
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d')   # matches 800 and 900 numbers
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')   # matches 800 and 900 numbers

# pattern = re.compile(r'[1-5]')   # specify range
# pattern = re.compile(r'[a-z]')   # range of lower case a-z
# pattern = re.compile(r'[a-zA-Z]')   # range of lower case a-z and A-Z
# pattern = re.compile(r'[a-zA-Z0-9]')   # range of lower case a-z and A-Z  and 0-9 digit


# []  - mactches char in brackets
# [^] - macthes char NOT in brackets
# pattern = re.compile(r'[^a-zA-Z]')   # carot ^ negates the set, that is not a-z or A-Z, all space digit
# pattern = re.compile(r'[^b]at')   #negate letter b, no match bat rest all its maches



# |     -  Either or
# (  )   - Group
# Qunatifiers:   to mactch multiple char at a time
# ---------------------
# *	   - 0 or more
# +    - 1 or more
# ?	   - 0 or one
# {3}  - exact number
# {3,4} - range of numbers(min, max)


#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # {3} exact match of 3 digits numbers

# pattern = re.compile(r'Mr') # match Mr
# pattern = re.compile(r'Mr\.') # match Mr.
# pattern = re.compile(r'Mr\.?') # match Mr and Mr.    one or more period.
# pattern = re.compile(r'Mr\.?\s[A-Z]')  # Mr. S etc
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  # Mr. S etc
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # using group parenthesis() for Mr and Mrs
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  # using group parenthesis() for Mr and Mrs
#matches = pattern.finditer(text_to_serach)

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  # using group parenthesis() for Mr and Mrs
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')  #matched digit to get phone number
matches = pattern.findall(text_to_serach)   # find all the groups

for match in matches:
    print(match)



# pattern = re.compile(r'^Start')   # string begin with Start word
# pattern = re.compile(r'^a')    # start with
# pattern = re.compile(r'end$')   # staring ends with word 'end'
# pattern = re.compile(r'a$')   # ends with 'a'
# matches = pattern.finditer(sentance)
# for match in matches:
#     print(match)

# print(text_to_serach[1:4])
#<re.Match object; span=(1, 4), match='abc'>  #begning and ending index of matched string.
