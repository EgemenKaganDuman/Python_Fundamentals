# API üzerinden çektiğimiz DATA'nın üzerinde CRUD Operasyonunu gerçekleştireceğiz.
from uuid import uuid4
from pprint import pprint
from requests import get
from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats()

data3 = career.get_data_frames()[0]

data = career.get_json()

# dictionary
data2 = career.get_dict()

pprint(playercareerstats)
print('-------------------------------')
pprint(data)
print('-------------------------------')
pprint(data3)
print('-------------------------------')
pprint(data2)
print('-------------------------------')

for key in data.value():
    print(key)
api_key = "aa39e167407545ccbfe184743251203"
url = 'https://www.weatherapi.com/my/'

while True:
    crudOperation = input('Process: ')
    match crudOperation:

        case 'exit':
            print('Application has been closing..!')
            break
        case 'create':
            pass