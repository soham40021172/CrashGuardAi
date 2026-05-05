# 🚗 Vehicle Crash Injury Prediction System

A production-style **Machine Learning + Data Engineering + Analytics Platform** designed to predict injury severity from vehicle crash reports.

Built using:

* **Python**
* **Flask REST API**
* **PostgreSQL**
* **Scikit-Learn Pipeline**
* **Feature Engineering**
* **Power BI**
* **React (Planned Integration)**

---

---

## 🎥 Demo & Project Walkthrough

Watch the system in action:

### 🚀 Full Project Demo (Model + Web App)

👉 [https://www.youtube.com/your-demo-link](https://youtu.be/a0pc44KEHp0)

---

### 📊 Power BI Dashboard Walkthrough

👉 [https://www.youtube.com/your-powerbi-link](https://youtu.be/t2-qywa1io8)

---

### 🧠 Model Prediction + Explainability (SHAP)

👉 https://www.youtube.com/your-shap-demo-link

---

## 💡 What these videos show:

* End-to-end pipeline execution
* Model training and predictions
* Real-time API usage via Flask
* Frontend interaction (React UI)
* Power BI insights and analytics
* SHAP-based model explainability

---


---
## 📌 Overview

The **Vehicle Crash Injury Prediction System** is an end-to-end analytics and machine learning project that transforms raw crash data into actionable injury risk predictions.

This project demonstrates a real-world ML workflow including:

* Data ingestion and preprocessing
* Automated feature engineering
* Machine learning model training
* API deployment for predictions
* Dashboard analytics
* Production-ready project architecture

---

## 🎯 Project Objective

The goal of this project is to:

* Clean and process raw crash report data
* Build reusable feature engineering pipelines
* Predict injury severity using machine learning
* Serve predictions via a Flask API
* Store and retrieve data using PostgreSQL
* Visualize insights using Power BI
* Maintain scalable production architecture

---

## 🏗️ Project Architecture

```text
Raw Crash Data
      ↓
Database Extraction
      ↓
Data Cleaning Pipeline
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Serialization (.pkl)
      ↓
Flask Prediction API
      ↓
React Frontend / Power BI Dashboard
```

---

## 📂 Project Structure

```text
crashreport/
│
├── crash_report/
│   ├── db/
│   │   └── connection.py
│   │
│   ├── modeling/
│   │   ├── train.py
│   │   └── predict.py
│   │
│   ├── pipeline/
│   │   ├── extract.py
│   │   ├── load.py
│   │   ├── cleaning/
│   │   └── feature_engineering/
│   │       ├── feature_selector.py
│   │       └── feature_transformer.py
│   │
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   └── plots.py
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── crash_model.pkl
│   │   ├── feature_schema.pkl
│   │   └── threshold.pkl
│   │
│   ├── logs/
│   ├── requirements.txt
│   └── wsgi.py
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
│
├── models/
├── notebooks/
├── tests/
├── reports/
├── logs/
├── README.md
└── requirements.txt
```

---

## ⚙️ Tech Stack

### Backend

* Flask
* Flask Blueprint Architecture
* SQLAlchemy
* Joblib
* Pandas

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* ColumnTransformer
* Pipeline API

### Database

* PostgreSQL

### Visualization

* Power BI

### Frontend *(Planned)*

* React.js

---

## 🗄️ Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE crash_report_db;
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crash_report_db
DB_USER=postgres
DB_PASSWORD=your_password
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd crashreport
```

---

### 2️⃣ Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧹 Data Cleaning Pipeline

The cleaning pipeline:

* Extracts raw crash data
* Cleans categorical columns
* Cleans numerical columns
* Generates cleaned SQL tables

Run:

```bash
python crash_report/pipeline/load.py
```

Creates:

```text
crash_reports_analysis_clean
```

inside PostgreSQL.

---

## 🤖 Model Training

Training pipeline includes:

* Feature selection
* Feature engineering
* Encoding
* Random Forest training
* Model persistence

Run:

```bash
python crash_report/modeling/train.py
```

Generated model artifacts:

```text
models/
├── crash_model.pkl
├── feature_schema.pkl
└── threshold.pkl
```

---

## 🔍 Prediction Script

Run prediction locally:

```bash
python crash_report/modeling/predict.py
```

Example output:

```text
Injury Probability: 0.73
Predicted Injury: 1
```

---

## 🌐 Running Flask Backend

Navigate to backend:

```bash
cd backend
```

Run:

```bash
python wsgi.py
```

Server runs at:

```text
http://localhost:8000
```

---

## 🧠 Feature Engineering Pipeline

### FeatureSelector

Responsible for:

* Removing leakage columns
* Dropping noisy features
* Removing redundant raw columns

### FeatureTransformer

Responsible for:

* Category consolidation
* Binary feature creation
* Numerical binning
* Data transformation

---

## 📈 Machine Learning Model

### Algorithm

* Random Forest Classifier

### Parameters

```python
RandomForestClassifier(
    n_estimators=400,
    max_depth=12,
    min_samples_leaf=10,
    min_samples_split=20,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)
```
## 🔍 Model Explainability (SHAP)

The system includes **SHAP (SHapley Additive exPlanations)** to interpret model predictions.

### What it provides:

* Shows **which features increased injury risk**
* Shows **which features decreased injury risk**
* Displays **impact contribution (%) per feature**
* Helps make the model **transparent and explainable**

This makes the model suitable for **real-world decision support systems**.

---

## ✅ Testing

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_training.py
pytest tests/test_feature_engineering.py
```

---

## 📊 Power BI Dashboard

Dashboard includes:

1. Executive Summary
2. Crash Time Analysis
3. Environmental Conditions
4. Driver & Vehicle Analysis
5. Geographic Heatmaps
6. Injury Prediction Insights

---

## 📂 Dataset Access

Due to GitHub file size limitations, the dataset is hosted externally.

👉 Download the raw dataset from Google Drive:
https://drive.google.com/file/d/1pRww1svVeVpW0KagA2gEzeUgJnztQv7R/view?usp=drive_link

---

## 📥 How to Use the Dataset

After downloading, you have **two options depending on your workflow**:

---

### 🔹 Option 1: For Notebook / Local Analysis

1. Download the dataset
2. Place it inside:

```text
data/raw/
```

3. Rename file (recommended):

```text
Crash_Reporting_-_Drivers_Data.csv
```

4. Run notebooks or scripts normally

---

### 🔹 Option 2: For Full Pipeline (Recommended)

This project is designed using a **production-style database workflow**.

#### Step 1 — Create PostgreSQL Database

```sql
CREATE DATABASE crash_report_db;
```

---

#### Step 2 — Import CSV into PostgreSQL

You can use:

* pgAdmin (GUI)
* OR SQL command:

```sql
COPY crash_reports
FROM '/path/to/Crash_Reporting_-_Drivers_Data.csv'
DELIMITER ','
CSV HEADER;
```

---

#### Step 3 — Run Cleaning Pipeline

```bash
python crash_report/pipeline/load.py
```

This will create:

```text
crash_reports_analysis_clean
```

---

#### Step 4 — Train Model

```bash
python crash_report/modeling/train.py
```

---

## ⚠️ Important Note

* The ML pipeline **does NOT directly read CSV files**
* It **expects data from PostgreSQL**
* This mimics **real-world production systems**

---

## 💡 Pro Tip

If you want a simpler setup, you can:

* Modify `extract.py` to read CSV directly
* OR create a helper script (`setup_db.py`) to automate DB loading

(Advanced users can extend this easily)


---
## 👨‍💻 Author

Developed as a complete **Machine Learning + Data Engineering + Analytics Project** for production-grade workflow demonstration.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Contribute improvements
* Share feedback

---
