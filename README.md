# Real-Time Data Pipeline with GCP Pub/Sub, Firestore and BigQuery

This project demonstrates a real-time sales data pipeline using Google Cloud Platform (GCP) services with a **Pub/Sub-first architecture**. The pipeline processes and transforms sales data and stores it in Firestore and Cloud Storage for analysis via BigQuery.

---

## **Architecture Overview**

1. **Mock Data Generator**: Generates simulated sales data and publishes it to a Pub/Sub topic.
2. **Pub/Sub Topic**: Handles real-time ingestion of sales data messages.
3. **Cloud Function**: Processes and transforms data, storing the results in Firestore and Cloud Storage.
4. **Firestore**: Stores structured sales data for downstream use.
5. **Cloud Storage**: Stores transformed JSON files for batch analytics.
6. **BigQuery**: Performs SQL-based analysis on the transformed data stored in Cloud Storage.

---

### **Architecture Flow**

```plaintext
          +---------------------------+
          |    Mock Data Generator    |
          | (Python Script with Pub/Sub)| 
          +---------------------------+
                     |
                     v
          +---------------------------+
          |        Pub/Sub Topic       |
          | (Event streaming)          |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |       Cloud Function       |
          | (Transforms the data)      |
          +---------------------------+
            /                 \
           v                   v
+-------------------+    +----------------------+
|    Firestore DB   |    |   Cloud Storage      |
| (Stores structured|    | (Stores JSON files)  |
|  transformed data)|    +----------------------+
           \                    |
            \                   v
             \      +---------------------------+
              \     |        BigQuery            |
               \----> (Queries JSON data)        |
                    +---------------------------+
```



## Setup Instructions

### Prerequisites
1. Google Cloud SDK installed and authenticated.
2. Python 3.9 or later installed.
3. Enabled the following GCP APIs:
    - Cloud Functions
    - Pub/Sub
    - Firestore
    - Cloud Storage
    - BigQuery



### Deployment Steps
#### Step 1: Set Up Firestore
```bash
bash setup_scripts/create_firestore.sh
```

#### Step 2: Set Up Pub/Sub
```bash
bash setup_scripts/create_pubsub.sh
```

#### Step 3: Set Up Cloud Storage
```bash
bash setup_scripts/create_storage.sh
```

#### Step 4: Deploy the Cloud Function
```bash
bash setup_scripts/deploy_cloud_function.sh
```

#### Step 5: Set Up BigQuery
```bash
bash setup_scripts/create_bigquery_table.sh
```

#### Step 6: Generate Mock Data
```bash
python3 mock_data_generator/mock_data_generator.py
```
