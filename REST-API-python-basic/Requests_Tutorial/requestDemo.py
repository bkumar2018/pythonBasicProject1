import requests


base_url = 'https://xkcd.com/353/'
r = requests.get(base_url)
#print(dir(r))  # show all the methods and attribute of r i.e response object
#print(help(r))   # Help on Response in module requests.models object

#print(r.content)
#print(r.text)
#print(r.headers)
print(r.status_code) #200
print(r.ok)   #True




#Dealing with images
# image_url = 'https://imgs.xkcd.com/comics/python.png'
# r = requests.get(image_url)
#print(r.content)

#open in wb mode write binary mode
# with open('comic.png','wb') as f:
#     f.write(r.content)









