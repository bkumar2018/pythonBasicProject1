import re

#urls validation
urls = '''
https://www.google.com
http://abcd.com
https://youtube.com
https://www.isro.gov
'''

# pattern = re.compile(r'http') #match http
#pattern = re.compile(r'http') #match https
# pattern = re.compile(r'https?')  #macth http and https using ?
# pattern = re.compile(r'https?://')  #

#pattern = re.compile(r'https?://(www\.)')  #
# pattern = re.compile(r'https?://(www\.)?')  #
#pattern = re.compile(r'https?://(www\.)?\w')  #
#pattern = re.compile(r'https?://(www\.)?\w+')  #

# pattern = re.compile(r'https?://(www\.)?\w+\.')  #
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')  #

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  #group to get domains etc

matches = pattern.finditer(urls)
for match in matches:
    #print(match)
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    print(match.group(3))


#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  #group to get domains etc
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)