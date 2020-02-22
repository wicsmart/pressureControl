from elasticsearch import Elasticsearch
import json
import time
import logging
import sys, os

# Define config
host = "127.0.0.1"
port = 9220
timeout = 10000
index = "geo_incidencia"
doc_type = "_doc"
size = 10000


# Process hits here
def process_hits(hits):
    todos_hits = []
    for item in hits:
        novo = item['_source']
        latitude = novo['latitude']
        longitude = novo['longitude']
        if len(latitude) > 0:
            novo['location'] = {
                        'lat': float(latitude),
                        'lon': float(longitude)
                        }

        todos_hits.append(novo)
    
    return todos_hits

# Escrever arquivo json
def escrever_file(data, numero_file):
    with open('./backup/incidencia'+str(numero_file)+'.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    # Init Elasticsearch instance
    es = Elasticsearch([{'host': host, 'port': port}], timeout=timeout)

    # Init scroll by search
    data = es.search(
        index=index,
        doc_type=doc_type,
        scroll='2m',
        size=size
            )

    sid = data['_scroll_id']
    scroll_size = len(data['hits']['hits'])
    count = 1
    escrever_file(process_hits(data['hits']['hits']), count)

    while scroll_size > 0:
        count = count+1
        "Scrolling..."
        data = es.scroll(scroll_id=sid, scroll='2m')
      
        # Process current batch of hits
        escrever_file(process_hits(data['hits']['hits']), count)

        # Update the scroll ID
        sid = data['_scroll_id']

        # Get the number of results that returned in the last scroll
        scroll_size = len(data['hits']['hits'])
        print count
 
