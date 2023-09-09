from elasticsearch import Elasticsearch
import json

out_json =  f"output_{now.strftime('%Y-%m-%d-%H-%M')}.json"
# Read JSON file
with open(out_json, 'r') as file:
    json_data = json.load(file)

# Connect to Elasticsearch
es = Elasticsearch(['http://192.168.1.26:9200'])

# Define index and document type
index = 'hdfc_nav_index'
#doc_type = 'doc_type'

# Add JSON data to Elasticsearch
es.index(index=index, body=json_data)