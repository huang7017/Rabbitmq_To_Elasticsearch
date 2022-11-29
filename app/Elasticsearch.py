from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
import json
import time
import geoip2.database
class Es:
    def __init__(self,host,port):
        self.es = Elasticsearch(hosts=host, port=port)
    def createIndex(self,index,testList):
        date = datetime.today().strftime('%Y%m')
        # timestamp
        now = datetime.now()
        insertTime = now.strftime('%Y-%m-%dT%H:%M:%S.%f000+08:00')
        actions = []
        for test in testList:
            action = {
            "_index": index+date,
            '_op_type': 'index',
            "_type": "_doc",
            "_source": test
                }
            actions.append(action)
        if len(actions) > 0:
            helpers.bulk(self.es, actions)
        print('All Finished', flush=True)
        # self.es.indices.create(index=index+date, body=alert,id=serverEsId,type='_doc')