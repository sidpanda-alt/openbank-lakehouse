from kafka import KafkaConsumer
import snowflake.connector
from dotenv import load_dotenv
import os
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
load_dotenv()
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = conn.cursor()

print("Listening for Kafka events...")

for message in consumer:
    data = message.value

    print("Received:", data)

    insert_query = """
    INSERT INTO BRONZE_TRANSACTIONS
    (txn_id, account_id, amount, ts)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        insert_query,
        (
            data['txn_id'],
            data['account_id'],
            data['amount'],
            data['ts']
        )
    )

    conn.commit()

    print("Inserted into Snowflake")