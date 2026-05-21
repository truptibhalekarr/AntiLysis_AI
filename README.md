# 🧬 AntiLysis AI
> **Advanced Bioprocess Analytics & High-Fidelity Anomaly Interception System**

AntiLysis AI is an end-to-end machine learning system engineered as a high-fidelity predictive digital twin for industrial biochemical reactors. The platform leverages a production-grade modular pipeline structure to predict continuous microbial biomass yield density ($g/L$) in real-time, while automatically tracking physical thresholds to flag cell-stress and prevent batch destruction caused by **Cell Lysis** (cellular rupture).

---

## 📁 Repository & Core Architecture

The codebase follows a strict industry-standard modular software pattern, completely decoupled into separate pipelines for preprocessing, evaluation, modeling, and deployment serving layouts:

```text
📁 AntiLysis_AI/
│
├── 📁 artifacts/             # Serialized production pipeline weights (model.pkl)
├── 📁 data/                  # Simulated bioreactor continuous sensor logs
│
├── 📁 src/                   # Core Modular ML Pipeline Scripts
│   ├── 📄 data_preprocessing.py   # Feature selection and train-test splitting
│   ├── 📄 evaluation.py           # Evaluation metrics engine (R² Score & MAE calculation)
│   ├── 📄 generated_data.py       # Bio-constrained raw dataset simulator engine
│   ├── 📄 model_training.py       # Unified Pipeline wrapper training script
│   ├── 📄 pipeline.py             # System orchestrator connecting ingestion to modeling
│   └── 📄 utils.py                # Global binary object serialization helper functions
│
├── 📄 app.py                 # Streamlit high-performance interactive UI
├── 📄 main.py                # Primary ignition switch triggering the training loop
└── 📄 requirements.txt       # Production dependency configuration log

🔬 Deployed Telemetry Parameters
The predictive engine processes 5 continuous independent inputs to evaluate cellular lifecycle tracking profiles:

Timeline Duration (Time_Hours): 0 to 168 hours (Standard industrial 1-week batch lifecycle sequence).

Reactor Temperature (Temperature): Normal baseline operations around 37.0°C (Overheating stress triggers cell apoptosis at >38.0°C).

Media Acidity (pH): Maintained around 7.0 homeostasis bounds (Acidic fluid shock penalties active below <6.5 pH).

Dissolved Oxygen (Dissolved_Oxygen): Target baseline fluid saturation at 50% oxygenation loops.

Nutrient Feed Rate (Glucose_Feed_Rate): Continuous carbon source supply inflow rate tracking.

📊 Core Performance Metrics
The underlying machine learning architecture uses a scikit-learn integrated Pipeline encapsulating feature scaling and a RandomForestRegressor matrix (100 independent decision estimators). Upon model execution, the pipeline reports the following performance metrics on holdout verification data:

R² Score (Coefficient of Determination): 0.9993 (Indicates 99.93% variance accuracy)

Mean Absolute Error (MAE): 0.35 g/L (Average prediction deviation margin)

🚀 Local Installation & Deployment Guide
Follow these steps to spin up the entire application platform locally in your machine:

1. Clone the repository to your local path
git clone [https://github.com/truptibhalekarr/AntiLysis_AI.git](https://github.com/truptibhalekarr/AntiLysis_AI.git)
cd AntiLysis_AI

2. Configure a virtual isolation workspace environment
# Windows Command Prompt / PowerShell
python -m venv .venv
.venv\Scripts\activate

3. Deploy environment runtime libraries dependencies
pip install -r requirements.txt

4. Run the end-to-end production pipeline training script
python main.py

5. Launch the high-fidelity web serving dashboard interface
streamlit run app.py

🛡️ Future Implementations
Phase 2 — Unsupervised Alignment: Integrating DBSCAN Clustering Algorithms within the modular pipeline architecture to identify and isolate multi-variable system outliers natively.

Plotly Visuals Integration: Hooking real-time flashing anomaly maps directly onto the web interface rendering layer.

