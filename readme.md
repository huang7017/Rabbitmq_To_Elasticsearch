修改測試環境參數config底下development.ini<br>
rabbitmq底下可以調整寫入Elasticsearch的資訊<br>


開發環境<br>
```
source rabbitmq/bin/activate
python main.py
```


生成image<br>

```
docker build -t test_info .
```
生產環境<br>

```
docker run -e production=true 
           -e rabbitmqHost=127.0.0.1
           -e rabbitmqPort=22987 
           -e rabbitmqName=guest 
           -e rabbitmqPassword=guest 
           -e rabbitmqQueue=WNC_ALERT_DATA 
           -e esHost=127.0.0.1
           -e esPort=9200 
           -e esIndex=test_info
           --name test_info -d test_info
           --restart always
```

測試環境<br>

```
docker run  --name test_info -d test_info --restart always
```

