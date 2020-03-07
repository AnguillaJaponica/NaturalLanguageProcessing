import json
import urllib.parse
import urllib.request

solr_url = 'http://localhost:8983/solr/'
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def load(collection, data):
    