import requests

# r = requests.get('http://192.168.0.107:3000/api')
# print(r)   # <Response [200]>
# #print(dir(r))   # ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'] 
# print(r.text) #Hello Welcome to APIServer for userdata.
# print(r.status_code)
# print(r.ok)
# print(r.headers)


payload={
	"id":100,
	"firstname":"Biru",
	"lastname":"Singh",
	"city":"Pune",
	"pin":12345
}
r = requests.post('http://192.168.0.107:3000/api/post',data=payload)
#print(r.text)
#print(r.json())

jsonResponseData = r.json()
# print(jsonResponseData['userInfoData'])

names=[]
for item in jsonResponseData['userInfoData']:
    print(item)
    names.append(item['firstname']+' '+ item['lastname'])

for name in names:
    print(name)

    








# r = requests.get('https://www.google.com/logos/doodles/2020/stay-and-play-at-home-with-popular-past-google-doodles-scoville-2016-6753651837108771-law.gif')
# print(r)
# print(r.status_code)
# print(r.ok)
# with open('google.gif', 'wb') as f:
#     f.write(r.content)


# #Call HTTP GET call
# payload={'page':2, 'count':25}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.text)
# print(r.url)   # http://httpbin.org/get?page=2&count=25


# #Call HTTP Post call
# payload={'username':'biren', 'password':'testing'}
# r = requests.post('http://httpbin.org/post',data=payload)
# #print(r.text)
# #print(r.json())
# dict = r.json()
# print(dict['form'])



# #Call HTTP GET call : Basic Authnetication
# r = requests.get('http://httpbin.org/basic-auth/biren/testing', auth=('biren','testing'))
# print(r)


# r = requests.get('http://httpbin.org/basic-auth/biren/testing',)
# print(r)

