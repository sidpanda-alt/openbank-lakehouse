from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

accounts = ['A100', 'A200', 'A300', 'A400']

while True:
    transaction = {
        "txn_id": str(random.randint(1000, 9999)),
        "account_id": random.choice(accounts),
        "amount": round(random.uniform(100, 1000), 2),
        "ts": time.time()
    }

    producer.send('transactions', transaction)
    print("Sent:", transaction)

    time.sleep(2)