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

**AntiLysis AI** functions as a high-fidelity predictive **digital twin** designed for industrial-scale biochemical fermentation reactors. Deployed on an industry-grade production pipeline, the system tracks continuous cellular replication patterns to accurately predict **Biomass Yield** ($g/L$). 

Simultaneously, the engine serves as a real-time safety interceptor—monitoring continuous telemetry inputs to trigger defensive flags against **Cell Lysis** (lethal cellular rupture caused by adverse thermal or acidic environment shifts) before batch destruction occurs.

---

## 📁 Repository Architecture & Modular Design

The software workspace strictly rejects monolithic scripts, completely decoupling operations into independent pipeline layers to maximize scannability and production deployment standards:

```text
📁 AntiLysis_AI/
│
├── 📁 artifacts/             # Serialized pipeline binaries (model.pkl)
├── 📁 data/                  # Simulated bioreactor continuous sensor logs
│
├── 📁 src/                   # Core Modular Pipeline Core
│   ├── 📄 data_preprocessing.py   # Automated feature slicing & train-test splitting
│   ├── 📄 evaluation.py           # Evaluation metrics engineering console
│   ├── 📄 generated_data.py       # Bio-constrained raw database simulator engine
│   ├── 📄 model_training.py       # Unified Pipeline wrapper training engine
│   ├── 📄 pipeline.py             # System orchestrator connecting ingestion layers
│   └── 📄 utils.py                # Global object serialization helpers (Pickle)
│
├── 📄 app.py                 # Streamlit high-performance interactive dashboard UI
├── 📄 main.py                # Primary ignition switch triggering training pipelines
└── 📄 requirements.txt       # Global production environment configurations

```

---

## 🔬 Deployed Telemetry Parameters

The core machine learning models process 5 continuous inputs to compute active culture density tracks:

| Parameter Name | Metric Units | Operational Boundaries & Safety Constraints |
| --- | --- | --- |
| **Time_Hours** | Hours (`0 - 168`) | Maps a standard industrial 7-day batch fermentation lifecycle. |
| **Temperature** | Celsius (`°C`) | Optimal at ~37°C. Overheating past `>38.0°C` triggers cell death arrays. |
| **pH** | Log Scale (`0 - 14`) | Maintained at ~7.0 homeostasis. Drops `<6.5` flag acidic fluid shock. |
| **Dissolved_Oxygen** | Saturation (`%`) | Target baseline fluid oxygenation loops set at `50%`. |
| **Glucose_Feed_Rate** | Inflow (`g/L/h`) | Continuous carbohydrate nutrition channel tracking profiles. |

---

## 📊 Performance Benchmark Analytics

The predictive back-end engine features a scikit-learn integrated `Pipeline` encapsulating multi-variable `StandardScaler` mechanisms mapped natively directly into a **Random Forest Regressor** matrix (100 independent tree estimators).

Upon compilation, the production pipeline logs the following verification benchmarks:

* **R² Score (Coefficient of Determination):** `0.9993` *(99.93% variance fit accuracy)*
* **Mean Absolute Error (MAE):** `0.35 g/L` *(Extremely tight 0.35 deviation margin)*

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

### 3. Inject runtime dependencies libraries

```bash
pip install -r requirements.txt

```

### 4. Fire the ignition switch to compile backend pipeline weights

```bash
python main.py

```

### 5. Stream up the luxury control center dashboard interface

```bash
streamlit run app.py

```

---

## 🛡️ Future Engineering Roadmap

* **Phase 2 — Unsupervised Alignment:** Integrating **DBSCAN Clustering Algorithms** inside the operational scripts to automatically capture and isolate multi-variable system outlier vectors natively.
* **Plotly Visuals Integration:** Hooking dynamic multi-dimensional cluster graphs directly onto the user frontend panel.
