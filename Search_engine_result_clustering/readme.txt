1. To run the code first make a virtual environment and install the relevant dependencies as given in the requirements.txt

2. Download elasticsearch version 7.14.2 and also install the carrot plugin using instructions on https://github.com/carrot2/elasticsearch-carrot2

3. Run the elasticsearch.bat file in the downloaded elasticsearch folder

3. Run the http://localhost:9200/ to see if the server is running.

4. Run the connection.py to establish a client to the localhost server.

5. Use client.indices.create(index='index-name') to create index on the elastic search server.

6. Run eland_loader to ingest the data.csv onto the elasticsearch index.

7. Run the python app.py to see the flask app running on http://127.0.0.1:5000/.