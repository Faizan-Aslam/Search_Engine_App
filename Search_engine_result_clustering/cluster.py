import requests
import json
from connection import estf
import pprint
data = {
"search_request": {
    '_source':['title', 'extract'],
    "query": {"match" : { "extract": "car" }},
  },
  "query_hint": "sedans",
  "field_mapping": {
    "title": ["_source.extact"],
    "content": ["_source.extract"]
  },
  "algorithm": "Bisecting K-Means",
  'labelCount': 1,
  "parameters": {
    "preprocessing": {
      "phraseDfThreshold": 1,
      "wordDfThreshold": 1
    }
  }
} 
  

#response = requests.post('http://localhost:9200/our-index/_search_with_clusters', data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".

# response = es.transport.perform_request(method='POST',url='http://localhost:9200/our-index/_search_with_clusters', body=json.dumps(data))


response = requests.post('http://localhost:9200/our-index/_search_with_clusters?pretty', data=json.dumps(data), headers= {
    'Content-Type': 'application/json'
  })
result =response.text
d = json.loads(result)

# pprint.pprint(d)
pprint.pprint(d)
# list=
# print()
