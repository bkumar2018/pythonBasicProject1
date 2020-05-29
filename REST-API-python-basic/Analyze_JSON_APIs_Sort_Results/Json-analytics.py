import json
import time
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
pkgs_json = r.json()
#print(len(pkgs_json))  #5029 pakgs

#print(pkg_json)
#We can use JSON module to dump to a sring and tell string to how to do fprmat.

# pkg_str = json.dumps(pkg_json, indent=2)
# print(pkg_str)   # Much better and readable format

# #Just listing 1st packages from json data
# pkgs_str = json.dumps(pkgs_json[0], indent=2)
# print(pkgs_str)   # Much better and readable format


# pkg_name = pkgs_json[0]["name"]
# pkg_desc = pkgs_json[0]["desc"]

# pkg_url = f'https://formulae.brew.sh/api/formula/{pkg_name}.json'
# #https://formulae.brew.sh/api/formula/a2ps.json

# r = requests.get(pkg_url)
# pkg_json = r.json()

# pkg_str = json.dumps(pkg_json, indent=2)
# #print(pkg_str)

# installs_30 = pkg_json['analytics']['install_on_request']['30d'][pkg_name]
# installs_90 = pkg_json['analytics']['install_on_request']['90d'][pkg_name]
# installs_365 = pkg_json['analytics']['install_on_request']['365d'][pkg_name]

# print(pkg_name, pkg_desc, installs_30, installs_90, installs_365)


#create a list 
results = []

t1 = time.perf_counter()

for pkg in pkgs_json:
    pkg_name = pkg["name"]
    pkg_desc = pkg["desc"]

    pkg_url = f'https://formulae.brew.sh/api/formula/{pkg_name}.json'  

    r = requests.get(pkg_url)
    pkg_json = r.json()

    installs_30 = pkg_json['analytics']['install_on_request']['30d'][pkg_name]
    installs_90 = pkg_json['analytics']['install_on_request']['90d'][pkg_name]
    installs_365 = pkg_json['analytics']['install_on_request']['365d'][pkg_name]

    #create data dictonary
    data = {
        'name':pkg_name,
        'desc':pkg_desc,
        'analytics': {
            '30d':installs_30,
            '90d':installs_90,
            '365d':installs_365
        }
    }

    results.append(data)
    
    time.sleep(r.elapsed.total_seconds())

    print(f'Got {pkg_name} in {r.elapsed.total_seconds()} seconds')

    break

t2 = time.perf_counter()
   

print(f'Finished in {t2-t1} seconds')
#print(results)
#print(pkg_name, pkg_desc, installs_30, installs_90, installs_365)


#Capture and save into own json file
with open('pkg_info.json','w') as f:
    json.dump(results, f, indent=2)

