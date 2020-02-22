from elasticsearch import Elasticsearch, helpers
import random
import json
import time
import logging
import sys, os
import mapping_incidencia

INDEX_NAME, DOC_TYPE = 'geo_incidencia', '_doc'

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


def create_empty_index(es_object):
    created = False
    try:
        print mapping_incidencia.mapping
        if not es_object.indices.exists(INDEX_NAME):
            es_object.indices.create(
                index=INDEX_NAME, body=mapping_incidencia.mapping)
            print('Created Index')
            created = True
        else:
            print es_object.indices.delete(index=INDEX_NAME) 
            
            print es_object.indices.create(
                index=INDEX_NAME, body=mapping_incidencia.mapping)
           
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created

def load_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            print filename
            f = open(directory+"/"+filename)
            docket_content = f.read()
            body=json.loads(docket_content)
            print(helpers.bulk(es, body, index=INDEX_NAME, doc_type=DOC_TYPE))

if __name__ == '__main__':
    
    path_backup = '/home/wictor/Documentos/backup'

    logging.basicConfig(level=logging.ERROR)

    es = connect_elasticsearch("127.0.0.1","9220")

    create_empty_index(es)

    load_json(path_backup)