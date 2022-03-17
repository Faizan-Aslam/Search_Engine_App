import csv
from connection import estf
from elasticsearch import helpers

with open('car-5.csv', encoding='utf8') as f:
    reader = csv.DictReader(f)
    helpers.bulk(estf, reader, index='our-index')
