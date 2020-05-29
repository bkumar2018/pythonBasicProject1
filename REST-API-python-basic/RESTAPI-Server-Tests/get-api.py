import requests


base_url = 'http://13.233.60.41:3000/'

def get_api():

    api_url= base_url+'api/'
    r=requests.get(api_url)
    print(r)

    #print(dir(r))
    #print(help(r))

    print(r.content)  #binary output
    print(r.headers)
    print(r.text)   #unicode output


def get_api_users():
    api_users_url = base_url + 'api/users'
    r = requests.get(api_users_url)
    #print(r.text)
    r_json = r.json()
    #print(r_json[0]["firstname"])  #single data is displayed

    results = []

    for data in r_json:
        #print(data['firstname'])
        #first_names.append(data['firstname'])
        data = {
            'firstname':data['firstname'],
            'city':data['city']
        }

        results.append(data)

    
    for result in results:
        print(result)

    




#get_api()
get_api_users()