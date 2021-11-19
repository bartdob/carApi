import requests

make = 'Honda'

url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/%s?format=json'%(make)

r_json = requests.get(url).json()

print(r_json)