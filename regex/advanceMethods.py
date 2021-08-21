import re

sentance = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'dne')
# matches = pattern.match(sentance)
# print(matches)


#flags
# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)
matches = pattern.search(sentance)
print(matches)
