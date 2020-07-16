from time import sleep
from json import dumps 
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9099'])

f = open("Kisch.txt", "r")
line = f.readlines()

for i in range(len(line)):
    producer.send('PythonKafkaTest', json.dumps(line[i]).encode('utf-8'))
    sleep(1)