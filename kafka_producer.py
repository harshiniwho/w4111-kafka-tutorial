import os

from kafka import KafkaProducer
from sqlalchemy import *

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_SERVER = os.environ['DB_SERVER']

DATABASEURI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/proj1part2"

db_engine = create_engine(DATABASEURI)

conn = None

def stringify_payments(payments):
    # simply converting the data to a string for our example
    # you can replace this with whatever you want
    payment_data = []
    for payment in payments:
        payment_data.append(f"{payment.payment_id}: User {payment.columbia_uni} paid {payment.amount} on {payment.timestamp}")
    return payment_data

try:
    # connect to our database to fetch payment info
    conn = db_engine.connect()
    # can replace this query with any query of your requirement
    payments = conn.execute("SELECT payment_id, amount, columbia_uni, to_char(payment_timestamp, 'Day DD Mon YYYY HH:MM:ss') as timestamp FROM payments").fetchall()
    payments = stringify_payments(payments)

    # stream this data to our local kafka instance
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    for payment in payments:
        value = producer.send('payments', payment.encode('ascii'))
    # flushes the producer
    producer.flush()
finally:
    # finally close connection
    if conn != None:
        conn.close()
