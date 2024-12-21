#!/bin/bash
# Create BigQuery dataset
bq mk --dataset --location=us-central1 pubsub_first_dataset

# Create BigQuery external table
bq mk --external_table_definition=pubsub_first_table \
    format=JSON \
    uris=gs://pubsub-first-bucket/orders/*.json \
    pubsub_first_dataset.pubsub_first_table
