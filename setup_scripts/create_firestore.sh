#!/bin/bash
# Enable Firestore API
gcloud services enable firestore.googleapis.com

# Create Firestore in Native Mode
gcloud firestore databases create --region=us-central1
