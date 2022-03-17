import os
import re
from connection import estf
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from flask import (
    Flask,
    render_template,
    request,
    url_for
)
import requests
import json


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("query")
    s = Search(using=estf, index="our-index")
    m = MultiMatch(query=query, fields=["title", "extract"])
    s = s.query(m)
    results = s.execute()
    data = {
    "search_request": {
    '_source':['title', 'extract'],
    "query": {"match" : { "extract": query }},
  },
    "query_hint": "",
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
    response = requests.post('http://localhost:9200/our-index/_search_with_clusters?pretty', data=json.dumps(data), headers= {
    'Content-Type': 'application/json'
  })

    result =response.text
    d = json.loads(result)
    cluster_labels = [ cluster for cluster in d["clusters"]]
    
    return render_template(
        "search.html",
        results=results,
        query=query,
        cluster_labels=cluster_labels
    )
@app.route('/cluster/', methods=['GET', 'POST'])
def cluster():
    query = request.args.get("query")
    data = {
    "search_request": {
    '_source':['title', 'extract'],
    "query": {"match" : { "extract": 'sedans' }},
  },
    "query_hint": "",
    "field_mapping": {
    "title": ["_source.extact"],
    "content": ["_source.extract"]
  },
    "algorithm": "Bisecting K-Means",
    'labelCount': 2,
    "parameters": {
        "preprocessing": {
            "phraseDfThreshold": 1,
            "wordDfThreshold": 1
    }
  }
} 
    response = requests.post('http://localhost:9200/our-index/_search_with_clusters?pretty', data=json.dumps(data), headers= {
    'Content-Type': 'application/json'
  })

    result =response.text
    d = json.loads(result)
    docs = d['clusters'][1]['documents']
    response_res = [json.loads(requests.get(f'http://localhost:9200/our-index/_doc/{doc}/_source?pretty', headers= {'Content-Type': 'application/json'}).text) for doc in docs]

    return render_template('cluster.html',results =response_res, query=query)


# @app.route('/search/<int:page_num>')
# def search(page_num):
#     searches = Search.query.paginate(per_page=5, page = page_num, error_out=True)

#     return render_template('search.html', searches = searches)


if __name__ == "__main__":
    app.run(debug=True)
