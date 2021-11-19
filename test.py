import random

import requests


def index():
    make = 'honda'
    model = ''
    # url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/%s/%s?format=json' % (make, model)
    # post_fields = {'format': 'json', 'data': '3GNDA13D76S000000;5XYKT3A12CG000000'}
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/%s/%s?format=json' % (make, model)
    payload = {'Model_Name': 'Civic'}
    # #url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/?format=json'
    # post_fields = {'format': 'json', 'data': 'Volkswagen'}
    #
    # url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/honda?format=json';
    # # post_fields = {'format': 'json', 'data': 'make'};
    r = requests.get(url, params=payload).json()

    res = requests.get(url, params=payload)

    print(r['SearchCriteria'])

    model1 = r['Results'][0]['Model_Name']
    print(model1)

    print(res.status_code)

    print(r['Message'])

    # r = requests.post(url.format())
    # print(r.json())


index()

def random_string():
    return str(random.randint(1, 5))


print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())
print(random_string())


