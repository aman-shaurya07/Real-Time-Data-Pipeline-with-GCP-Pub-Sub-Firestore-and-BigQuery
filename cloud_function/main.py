import base64
import json
from google.cloud import firestore
from google.cloud import storage

# Initialize Firestore and Cloud Storage clients
db = firestore.Client()
storage_client = storage.Client()

def transform_sales_data(event, context):
    """Process data from Pub/Sub, transform it, and store it in Firestore and Cloud Storage."""
    # Decode the Pub/Sub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    sales_record = json.loads(pubsub_message)

    # Transform the data
    transformed_data = {
        'orderid': sales_record['orderid'],
        'product_name': sales_record['product_name'],
        'quantity': int(sales_record['quantity']),
        'price': float(sales_record['price']),
        'total': int(sales_record['quantity']) * float(sales_record['price'])
    }

    # Save transformed data to Firestore
    doc_ref = db.collection('pubsub_first_sales').document(transformed_data['orderid'])
    doc_ref.set(transformed_data)

    # Save transformed data to Cloud Storage
    bucket = storage_client.bucket('pubsub-first-bucket')
    blob = bucket.blob(f"orders/{transformed_data['orderid']}.json")
    blob.upload_from_string(json.dumps(transformed_data))
