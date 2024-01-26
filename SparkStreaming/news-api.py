import requests
import json
import time
from confluent_kafka import Producer

conf = {'bootstrap.servers': 'localhost:9092'}  
producer = Producer(conf)

while True:
    url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=8f218***************4ff8ea84')
    response = requests.get(url)

    data = response.json()
    if data['status'] == 'ok':
        for article in data['articles']:
            content = article['content']
            if content is not None:
                producer.produce('input_topic_1', value=content) 
                producer.flush()

    time.sleep(150)  
