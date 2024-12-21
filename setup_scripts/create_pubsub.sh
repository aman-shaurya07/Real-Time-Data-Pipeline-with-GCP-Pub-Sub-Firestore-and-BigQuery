#!/bin/bash
# Create Pub/Sub topic
gcloud pubsub topics create pubsub-first-topic

# Create Pub/Sub subscription
gcloud pubsub subscriptions create pubsub-first-subscription \
    --topic=pubsub-first-topic
