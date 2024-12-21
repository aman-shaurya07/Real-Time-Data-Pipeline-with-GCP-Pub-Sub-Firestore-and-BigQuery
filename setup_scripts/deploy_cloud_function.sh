#!/bin/bash
# Deploy Cloud Function
gcloud functions deploy pubsub-first-function \
    --runtime python39 \
    --trigger-topic pubsub-first-topic \
    --entry-point transform_sales_data \
    --region us-central1 \
    --source ../cloud_function
