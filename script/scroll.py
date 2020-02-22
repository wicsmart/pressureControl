from elasticsearch import Elasticsearch
import json
import pandas as pd


# Define config
host = "127.0.0.1"
port = 9220
timeout = 1000
index = "incidencia"
doc_type = "_doc"
size = 10000

body = {
     "_source": [
              "data_inicio",
              "data_fim",
              "clientes_afetados_3min_max",
              "calculo_conh_total",
              "conjunto",
              "latitude",
              "longitude",
              "causa",
              "nivel_tensao",
              "polo",
              "tipo",
              "sucursal"
    ]
}


array = []

# Init Elasticsearch instance
es = Elasticsearch([{'host': host, 'port': port}], timeout=timeout)

# Process hits here
def process_hits(hits):
    for item in hits:
        novo = item['_source']
        novo['dia_inicio'] = novo['data_inicio'].split("T")[0]
        novo['hora_inicio'] = novo['data_inicio'].split("T")[1][:-1:]
        novo['dia_fim'] = novo['data_fim'].split("T")[0]
        novo['hora_fim'] = novo['data_fim'].split("T")[1][:-1:]

        array.append(novo)
        


# Check index exists
if not es.indices.exists(index=index):
    print("Index " + index + " not exists")
    exit()

# Init scroll by search
data = es.search(
    index=index,
    doc_type=doc_type,
    scroll='2m',
    size=size,
    body=body
)

# Get the scroll ID
sid = data['_scroll_id']
scroll_size = len(data['hits']['hits'])

# Before scroll, process current batch of hits
process_hits(data['hits']['hits'])
count = 0
while scroll_size > 0:
    count = count+1
    "Scrolling..."
    data = es.scroll(scroll_id=sid, scroll='2m')

    # Process current batch of hits
    process_hits(data['hits']['hits'])

    # Update the scroll ID
    sid = data['_scroll_id']

    # Get the number of results that returned in the last scroll
    scroll_size = len(data['hits']['hits'])
    print count
    # if count > 2:
    #   break


df = pd.DataFrame(array)

df.to_csv('/home/wictor/NetBeansProjects/sinapase/script/incidenciav2.csv',index=False, sep=',',encoding='utf-8')

print df.describe()

