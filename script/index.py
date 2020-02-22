from elasticsearch import Elasticsearch, helpers
from datetime import datetime, timedelta
import random
import json
import time
import logging
import sys, os

INDEX_NAME, DOC_TYPE = 'pressure', '_doc'

class elastic(object):
    
    _es None

     def __init__(self, host, endereco, porta):
         self.host = host
         self.endereco = endereco
         self.port = porta

    def store_record(elastic_object, record):
        try:
            print elastic_object.index(
                index=INDEX_NAME, doc_type=DOC_TYPE, body=record)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))


    def store_bulk(elastic_object, bulk):
        try:
            print helpers.bulk(elastic_object, bulk, True)
        except Exception as ex:
            print('Error in indexing data')
            # print(str(ex))


    def connect_elasticsearch(endereco, porta):
        _es = None
        _es = Elasticsearch([{'host': endereco, 'port': porta}])
        if _es.ping():
            print 'Elastisearch Connect'
        else:
            print 'Elastisearch is not connect!'
        return _es

        def create_index(es_object):
        created = False
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },
            "mappings": {
                "_doc": {
                    "properties": {
                        "data_hora": {
                            "type":   "date",
                            "format": "dd/MM/yyyy HH:mm:ss||dd/MM/yyyy||epoch_millis"
                        }        
                    }
                }
            }
        }
        try:
            if not es_object.indices.exists(INDEX_NAME):
                es_object.indices.create(
                    index=INDEX_NAME, body=settings)
                print('Created Index')
                created = True
            else:
                print ('Index already exists')
        except Exception as ex:
            print(str(ex))
        finally:
            return created

        def create_empty_index(es_object):
        created = False
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },
            "mappings": {
                "_doc": {
                    "properties": {
                        "data_hora": {
                            "type":   "date",
                            "format": "dd/MM/yyyy HH:mm:ss||epoch_millis"
                        }
                    }
                }
            }
        }
        try:
            if not es_object.indices.exists(INDEX_NAME):
                es_object.indices.create(
                    index=INDEX_NAME, body=settings)
                print('Created Index')
                created = True
            else:
                print es_object.indices.delete(index=INDEX_NAME) 
                
                print es_object.indices.create(
                    index=INDEX_NAME, body=settings)
                
                created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

    def gerar_bulk():
        bulk = []
        documento = {}
        bulk.append(documento)
        return bulk

# def load_json(directory):
#     for filename in os.listdir(directory):
#         if filename.endswith(".json"):
#             f = open(filename)
#             docket_content = f.read()
#             body=json.loads(docket_content)
#             print(helpers.bulk(es, body, index=INDEX_NAME, doc_type=DOC_TYPE))

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    es = connect_elasticsearch("127.0.0.1","9200")