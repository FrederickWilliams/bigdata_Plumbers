from json import loads
from kafka import KafkaConsumer
consumer = KafkaConsumer('PythonKafkaTest',
    bootstrap_servers=['localhost:9099'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id = 'my-group')

b_file = open('receiving.txt','w')
for line in consumer:
    line = line.value
    b_file.write(line.decode('utf-8'))

b_file.close()