#!/bin/bash
# Create Cloud Storage bucket
gcloud storage buckets create gs://pubsub-first-bucket \
    --location=us-central1

# Enable versioning (optional)
gcloud storage buckets update gs://pubsub-first-bucket --versioning
