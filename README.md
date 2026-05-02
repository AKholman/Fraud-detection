## 🚀 Live Demo
👉 https://fraud-detection-82yj5vkxtevasdsitmgjsm.streamlit.app/

## ⚙️ How It Works
UI (Streamlit) → API Gateway → AWS Lambda → XGBoost Model (S3)

- The ML model is already trained and deployed on AWS
- Streamlit UI only sends transaction data to the API
- Lambda loads the model from S3 and returns real-time predictions
- No setup or cloud access is required to use the app

--------------------------------------------------------------------------------

💳 Real-Time Credit Card Fraud Detection (End-to-End ML System)
Overview

This project implements a production-style, end-to-end fraud detection system using classical machine learning (XGBoost) and AWS cloud services, fully deployed with CPU-only, low-cost infrastructure.

The pipeline covers data preprocessing → model training → cloud storage → real-time inference API → UI, closely mirroring real-world ML engineering workflows.

🧩 Problem Statement

Credit card fraud detection is a highly imbalanced binary classification problem, where fraudulent transactions are rare but extremely costly if missed.

Dataset (Kaggle – Credit Card Fraud Detection):

Total rows: 284,807
Features: Time, V1–V28 (PCA-transformed), Amount
Target: Class (1 = Fraud, 0 = Legit)

Class Distribution
+-------+--------+
| Class | Count  |
+-------+--------+
|   1   |   473  |
|   0   | 283253 |
+-------+--------+
⚠️ Fraud cases represent ~0.17% of all transactions, requiring careful handling of class imbalance.

------------------------------------------------------

🧹 Data Preprocessing & Feature Engineering

Platform: Databricks Community Edition (Free)

Tools: Spark + SQL

Steps:

Loaded raw Kaggle CSV into Databricks
Data validation and cleanup
Feature selection (Time, V1–V28, Amount)
No target leakage (Class excluded from features)
Final dataset exported as CSV
Uploaded to AWS S3 for downstream training

----------------------------------------------
🧠 Model Training (AWS EC2 – CPU Only)

Instance: EC2 t2.micro / t3.micro (Free Tier)
Framework: XGBoost (CPU mode)

Key Techniques:

scale_pos_weight to handle extreme class imbalance
Stratified 5-fold cross-validation
Probability threshold tuning (optimized for recall)
Standard scaling applied consistently for training & inference

Training Metrics

| Metric          | Value      |
| --------------- | ---------- |
| Mean CV ROC-AUC | **0.9771** |
| ROC-AUC (final) | **0.9973** |
| Precision       | **0.8878** |
| Recall          | **0.9704** |

----------------------------------------------------

📦 Model Artifacts & Storage (AWS S3)

All artifacts are versioned and stored in S3:

s3://fraud-project/models/xgb/
├── model.pkl
├── scaler.pkl
└── feature_list.json

S3 acts as a central artifact store, decoupling training from inference.

---------------------------------------------

⚡ Real-Time Inference (AWS Lambda)

Deployment: Lambda Container Image (CPU)
Cold-start behavior:

Model + preprocessing artifacts loaded from S3 once
Cached in /tmp for reuse

Inference Logic:

Accepts JSON transaction input
Applies feature ordering + scaling
Returns fraud probability + classification label

Output Example

{
  "fraud_probability": 0.87,
  "fraud_label": 1
}

---------------------------------------

🌐 API Layer (AWS API Gateway)

Type: HTTP API
Endpoint:
POST /predict

Flow:
Client → API Gateway → Lambda → XGBoost Model → Prediction

Fully serverless
Auto-scaling
Public REST endpoint
CORS enabled for UI access

-------------------------------------------

🖥️ User Interface (Streamlit)

Deployment: Streamlit Community Cloud

Features:

Transaction input form (Time, V1–V28, Amount)
Real-time API calls
Fraud probability display
Risk label (Fraud / Legit)
Prediction history chart
Feature importance visualization

🔗 Recruiter-friendly public demo link

----------------------------------------------

🛠️ Tech Stack

ML: XGBoost (CPU)
Data Processing: Databricks, Spark, SQL
Training: AWS EC2 (Free Tier)
Storage: AWS S3
Inference: AWS Lambda (Container Image)
API: AWS API Gateway
UI: Streamlit
Cost: ~$0 (Free Tier)

---------------------------------------------

🏁 Key Takeaways
Designed for real-world ML deployment, not just notebooks
Handles severe class imbalance
Fully serverless inference
Clean separation between training and serving
Resume-ready, production-style architecture

-----------------------------------------------

📌 Future Improvements
Model versioning & A/B testing
Monitoring & drift detection
Batch inference pipeline
Feature store integration

-----------------------------------------------

One-paragraph bullet — Fraud Detection Project:

Real-time credit card fraud detection system.
Built an end-to-end, production-style ML pipeline using XGBoost (CPU) to handle extreme class imbalance (~0.17% fraud). Performed Spark/SQL preprocessing in Databricks, trained and validated models on AWS EC2 (free tier), and stored versioned artifacts in S3. Deployed a serverless, low-latency inference service using AWS Lambda (container image) and API Gateway, and exposed a Streamlit UI for real-time predictions and monitoring. Achieved ROC-AUC 0.997, precision 0.89, recall 0.97 on held-out data. | GitHub | Live Demo |

-----------------------------------------------
Author: Iskandar Kholmanov
Role Target: Machine Learning Engineer / Applied Scientist / Senior Data Scientist

