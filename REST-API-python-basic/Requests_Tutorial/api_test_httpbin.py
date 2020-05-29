import requests


url = 'http://httpbin.org/'



#Call get using parameters below
def call_get_with_params():

    get_url = url + 'get'
    #payload is dictionary of params to call get call
    payload = {
        'page':2,
        'count':25
    }    

    r = requests.get(get_url, params=payload)  #http://httpbin.org/get?page=2&count=25   This url is to call get api with parameters
    #print(r.text)
    print(r.url)


def call_post_with_data():

    post_url = url + 'post'
    #payload is dictionary of params to call get call
    payload = {
        'username':'biru',
        'password':'test123'
    }

    r = requests.post(post_url, data=payload)
    print(r.text)


def call_post_with_data_get_Json():

    post_url = url + 'post'
    #payload is dictionary of params to call get call
    payload = {
        'username':'biru',
        'password':'test123'
    }

    r = requests.post(post_url, data=payload)
    r_dict = r.json()

    #print(r.json())
    print(r_dict['form'])


#test basic auth 
def call_get_to_basic_auth():
    r = requests.get('https://httpbin.org/basic-auth/biru/test123', auth=('biru','test123'))
    print(r)
    print(r.text)

    # #Try to access with wrong or invalid password to check the response code 401
    # r = requests.get('https://httpbin.org/basic-auth/biru/test123', auth=('biru','test123123'))
    # print(r)
    # print(r.text)

  

#The api will take 5 seonds to give response, but we have set timeout to 3 sec, that is after 3 sec we get erorr
#Read timed out  exception, we expect to get response out within 3 sec. else error read out.

def call_get_delay_api_with_timeout():
    r = requests.get('https://httpbin.org/delay/5', timeout=3)
    print(r)



#call_get_with_params()
#call_post_with_data()
#call_post_with_data_get_Json()
#call_get_to_basic_auth()
call_get_delay_api_with_timeout()





