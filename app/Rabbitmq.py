import sys
import pika
import json
from app.Elasticsearch import Es
from app.Config import Config
class Rabbitmq:
    def __init__(self,host,port,user,password,queue):
        credentials = pika.PlainCredentials(user,password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host,port,'/',credentials))
        self.channel = self.connection.channel()
        # durable=True
        self.channel.queue_declare(queue=queue) # 宣告一個名為 'hello' 的訊息佇列
        cfg = Config()
        host = cfg.get('es', 'event_ip')
        eventPort = cfg.get('es', 'event_port_9200')
        self.index = cfg.get('es', 'ES_INDEX_NAME')
        self.es = Es(host, eventPort)
    def send(self,routingKey,msg):
        # 把訊息放進名稱為：hello 的佇列中
        self.channel.basic_publish(exchange='',routing_key=routingKey,body=msg)
        print(f" [x] Sent {msg}", flush=True)
    def receive(self,routingKey):
        # ,auto_ack=True
        self.channel.basic_consume(routingKey,self.__callback) # 宣告消費來自 routingKey 的訊息
        self.channel.start_consuming()
    def __callback(self,ch, method, properties, body):
        body = body.decode("utf-8")
        print(f" [x] Received {body}", flush=True)
        try:
            self.addEs(body)
        except Exception as e:
                print(f" [x] error {e}", flush=True)
        ch.basic_ack(delivery_tag = method.delivery_tag)
    def addEs(self,body):
        testMap = json.loads(body)
        testStatusList = testMap.get('test_status')
        if testStatusList is not None:
            try:
                self.es.createIndex(self.index,testStatusList)
            except Exception as e:
                print(f" [x] error {e}", flush=True)
    def close(self):
        self.connection.close()

    
