import requests
import pprint
import json
docs = ['eS2Jan4BcFkGhlhEBg7O','Wy2Jan4BcFkGhlhEBg3O']
response = [json.loads(requests.get(f'http://localhost:9200/our-index/_doc/{doc}/_source?pretty', headers= {
    'Content-Type': 'application/json'}).text) for doc in docs]
pprint.pprint(response[0])