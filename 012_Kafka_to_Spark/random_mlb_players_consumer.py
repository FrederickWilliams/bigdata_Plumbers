import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming.kafka import utf8_decoder
from kafka import KafkaConsumer


# app creation
sc = SparkContext(appName='MLB_Player_Data')

# streaming in the data
ssc = StreamingContext(sc, 5)
kfk_cs = KafkaUtils.createDirectStream(ssc,["MLBplayers"], {"bootstrap.servers":"localhost:9092"},valueDecoder=utf8_decoder)

kfk_cs.pprint()


ssc.start()
ssc.awaitTermination()
