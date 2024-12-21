from google.cloud import pubsub_v1
import random
import time
import json

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('your-project-id', 'pubsub-first-topic')

def generate_order_data():
    """Generate mock sales data."""
    return {
        'orderid': str(random.randint(1, 10000)),
        'product_name': random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger']),
        'quantity': random.randint(1, 5),
        'price': round(random.uniform(10.0, 500.0), 2)
    }

while True:
    # Generate and publish data
    data = generate_order_data()
    publisher.publish(topic_path, json.dumps(data).encode('utf-8'))
    print(f"Published: {data}")
    time.sleep(2)
