
# 🧬 AntiLysis AI
> **Predictive Bioprocess Analytics & High-Fidelity Anomaly Interception System**

<div align="left">
    <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
    <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/R2%20Score-99.93%25-10B981?style=for-the-badge" alt="Accuracy">
</div>

---

## 📌 Project Overview

**AntiLysis AI** functions as a high-performance predictive **digital twin** engineered for industrial-scale biochemical fermentation reactors. Deployed on a decoupled production pipeline, the system tracks continuous cellular replication patterns to accurately forecast **Biomass Yield** ($g/L$). 

Simultaneously, the engine serves as a real-time safety interceptor—monitoring continuous telemetry inputs to trigger defensive flags against **Cell Lysis** (lethal cellular rupture caused by adverse thermal or acidic environment shifts) before batch destruction occurs.

---

## 📁 Repository Architecture & Modular Design

The software workspace strictly rejects monolithic scripts, completely decoupling operations into independent pipeline layers to maximize scannability and production deployment standards:

```text
📁 AntiLysis_AI/
│
├── 📁 artifacts/          # Serialized pipeline binaries (model.pkl, dbscan_model.pkl)
├── 📁 data/               # Simulated bioreactor continuous sensor logs (bioreactor_data.csv)
│
├── 📁 src/                # Core Modular Pipeline Architecture
│   ├── 📄 anomaly_detection.py    # Unsupervised anomaly clustering pipeline
│   ├── 📄 data_preprocessing.py   # Automated feature scaling & train-test splitting
│   ├── 📄 evaluation.py           # Evaluation metrics engineering console
│   ├── 📄 generated_data.py       # Bio-constrained raw database simulator engine
│   ├── 📄 model_training.py       # Supervised estimator training engine
│   ├── 📄 pipeline.py             # System orchestrator connecting ingestion layers
│   ├── 📄 utils.py                # Global object serialization helpers (Pickle)
│   └── 📄 visualizations.py       # Plotly dynamic multi-dimensional cluster graphs
│
├── 📄 app.py              # Streamlit premium responsive executive control panel UI
├── 📄 main.py             # Primary ignition switch triggering training pipelines
└── 📄 requirements.txt    # Global production environment configurations

```

---

## 🔬 Deployed Telemetry Parameters

The core machine learning models process 5 continuous inputs to compute active culture density tracks:

| Parameter Name | Metric Units | Operational Boundaries & Safety Constraints |
| --- | --- | --- |
| **Time_Hours** | Hours (`0.0 - 168.0`) | Maps a standard industrial 7-day batch fermentation lifecycle. |
| **Temperature** | Celsius (`°C`) | Optimal at ~37°C. Overheating past `>38.0°C` triggers thermal cell death arrays. |
| **pH** | Log Scale (`5.0 - 9.0`) | Maintained at ~7.0 homeostasis. Drops `<6.5` flag acidic fluid shock loops. |
| **Dissolved_Oxygen** | Saturation (`%`) | Target baseline fluid oxygenation loops locked at a standard `50.0%`. |
| **Glucose_Feed_Rate** | Inflow (`g/L/h`) | Continuous carbohydrate nutrition input channel tracking. |

---

## 📊 Performance Benchmark Analytics

The dashboard features a dual-engine machine learning grid evaluating data streams through separate processing tracks to eliminate multi-collinearity and capture operational deviations:

### 1. Supervised Predictive Layer (Regression)

* **Algorithm:** Random Forest Regressor (Ensemble model utilizing 100 independent decision estimators)
* **$R^2$ Score (Coefficient of Determination):** `0.9993` *(99.93% variance fit accuracy)*
* **Root Mean Squared Error (RMSE):** `0.48 g/L` *(Extremely stable deviation margin)*

### 2. Unsupervised Anomaly Interception Layer (Clustering)

* **Algorithm:** Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
* **Hyperparameters Configuration:** `Epsilon: 0.40` | `Min Samples: 4`
* **Operational Purpose:** Maps live multi-variable data coordinates natively to catch sensor glitches, hardware noise, or mechanical drift without predefined training tags.

---

## 🚀 Quick Local Deployment Guide

Follow this sequence to setup and run the entire interactive platform locally on your machine:

### 1. Clone the project workspace

```bash
git clone [https://github.com/truptibhalekarr/AntiLysis_AI.git](https://github.com/truptibhalekarr/AntiLysis_AI.git)
cd AntiLysis_AI

```

### 2. Configure environment isolation boundaries

```bash
python -m venv .venv
.venv\Scripts\activate

```

### 3. Inject runtime dependency libraries

```bash
pip install -r requirements.txt

```

### 4. Fire the ignition switch to compile backend pipeline weights

```bash
python main.py

```

### 5. Stream up the executive control center dashboard interface

```bash
streamlit run app.py

```
