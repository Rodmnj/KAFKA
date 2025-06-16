from kafka import KafkaProducer
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for _ in range(10):
    temp = round(random.uniform(20.0, 30.0), 1)
    humidity = round(random.uniform(40.0, 80.0), 1)

    message = f"temp={temp},humidity={humidity}"
    print("Enviado:", message)

    producer.send('sensor-data', message.encode('utf-8'))
    time.sleep(1)

producer.flush()
