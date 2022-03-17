from elasticsearch import Elasticsearch

estf = Elasticsearch(
        hosts= ["http://localhost:9200"]
        , headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json'}
        )


# doc_setting = {
#     "settings": {
#         "analysis": {
#              },    
#             "analyzer": {
#                 "my_analyzer": {
#                     "type": "stop",
#                     "tokenizer": "lowercase",
#                     "filter": [
#                         "stemmer"
#                     ]
#             }
#         }
#     }
#     , "mappings": {
#         "your_type": {
#             "properties": {
#                 "keyword": {
#                     "type": "string",
#                     "index_analyzer": "my_analyzer",
#                 }
#             }
#         }
#     }
# }

# estf.indices.create('final-index', body=doc_setting)