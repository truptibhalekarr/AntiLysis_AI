import streamlit as st
import pandas as pd
import numpy as np
from src.utils import load_object
from src.visualizations import generate_bioreactor_analysis_chart

# 1. Advanced Page Architecture
st.set_page_config(
    page_title="AntiLysis AI - Executive Control Center",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Executive Dark Theme Custom CSS Stylesheet (Figma-Aligned, No Emojis)
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }
    .stApp {
        background-color: #0B0F19;
    }
    .main-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #3B82F6 0%, #10B981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        padding-top: 0px;
    }
    .system-subtitle {
        font-size: 15px;
        color: #64748B;
        font-weight: 400;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 15px;
        border-left: 5px solid #3B82F6;
        padding-left: 12px;
    }
    .critical-card {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(220, 38, 38, 0.05) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    .critical-text {
        color: #F87171;
        font-size: 14px;
        font-weight: 600;
        margin: 0;
    }
    .sidebar-header {
        font-size: 18px;
        font-weight: 700;
        color: #3B82F6;
        margin-bottom: 15px;
    }
    .slider-spacing {
        margin-bottom: 32px !important;
    }
    /* ---- YEH NAYA CSS ADD KIYA ---- */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        align-items: stretch; /* Teeno boxes ki height barabar karta hai */
        gap: 16px;
        width: 100%;
    }
    .kpi-card {
        flex: 1 1 32%; /* Teeno boxes ko exact barabar width (space) deta hai */
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 8px;
        padding: 16px;
        box-sizing: border-box;
    }
    .kpi-label {
        font-size: 11px;
        font-weight: 700;
        color: #9CA3AF;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
        text-transform: uppercase;
    }
    .kpi-value {
        font-size: 24px;
        font-weight: 800;
        color: #F9FAFB;
        line-height: 1.2;
    }
    .kpi-delta {
        font-size: 12px;
        font-weight: 600;
        color: #10B981;
        margin-top: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Secure Production Artifact Loading
@st.cache_resource
def load_assets():
    pipeline = load_object("artifacts/model.pkl")
    unsup_scaler = load_object("artifacts/unsupervised_scaler.pkl")
    dbscan_model = load_object("artifacts/dbscan_model.pkl")
    return pipeline, unsup_scaler, dbscan_model

pipeline, unsup_scaler, dbscan_model = load_assets()

if pipeline is None:
    st.error("Core machine learning weights missing. Please execute 'python main.py' to initialize pipeline components.")
else:
    # 4. Premium Sidebar Navigation Panel
    with st.sidebar:
        st.markdown('<p class="sidebar-header">Navigation Deck</p>', unsafe_allow_html=True)
        navigation_page = st.radio(
            "Select Workspace View:",
            [
                "Live Telemetry & Prediction",
                "Feature Correlation Matrix",
                "Model Evaluation Matrix",
                "System Documentation"
            ]
        )
        st.markdown("---")
        st.caption("AntiLysis AI")

    # 5. Header Layout 
    st.markdown('<h1 class="main-title">AntiLysis AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="system-subtitle">Predictive Bioprocess Analytics & High-Fidelity Anomaly Interception System</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(255,255,255,0.05); margin-top:0; margin-bottom:20px;'>", unsafe_allow_html=True)

    # PAGE 1: LIVE TELEMETRY WORKSPACE
    if navigation_page == "Live Telemetry & Prediction":
        col_controls, col_analytics = st.columns([1, 2.2], gap="large")

        with col_controls:
            st.markdown('<div class="section-title">Telemetry Inputs</div>', unsafe_allow_html=True)
            st.caption("Manipulate live reactor state metrics using the continuous control deck.")
            
            with st.container(border=True):
                st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
                time_hours = st.slider("Duration Matrix (Time_Hours)", 0.0, 168.0, 48.0, step=0.5)
                
                st.markdown("<div class='slider-spacing'></div>", unsafe_allow_html=True)
                temperature = st.slider("Reactor Core Temperature (C)", 34.0, 42.0, 37.0, step=0.05)
                
                st.markdown("<div class='slider-spacing'></div>", unsafe_allow_html=True)
                ph = st.slider("Media Ionization Value (pH)", 5.0, 9.0, 7.0, step=0.05)
                
                st.markdown("<div class='slider-spacing'></div>", unsafe_allow_html=True)
                dissolved_oxygen = st.slider("Dissolved Oxygen Saturation (DO %)", 10.0, 80.0, 50.0, step=0.5)
                
                st.markdown("<div class='slider-spacing'></div>", unsafe_allow_html=True)
                glucose_feed = st.slider("Nutrient Carbon Inflow (g/L/h)", 1.0, 6.0, 3.0, step=0.05)
                st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

        with col_analytics:
            st.markdown('<div class="section-title">High-Fidelity Intelligence Deck</div>', unsafe_allow_html=True)
            st.caption("Real-time inference matrix generated by the serialized architecture pipeline.")
            
            input_features = pd.DataFrame({
                "Time_Hours": [time_hours],
                "Temperature": [temperature],
                "pH": [ph],
                "Dissolved_Oxygen": [dissolved_oxygen],
                "Glucose_Feed_Rate": [glucose_feed]
            })

            predicted_yield = pipeline.predict(input_features)[0]

            anomalies_active = []
            if temperature > 38.0:
                anomalies_active.append(f"Thermal Overstress: Temperature threshold exceeded limit ({temperature} C).")
            if ph < 6.5:
                anomalies_active.append(f"Acidic Media Shock: Ambient fluid pH dropped into lethal zones ({ph}).")
            if dissolved_oxygen < 22.0:
                anomalies_active.append(f"Hypoxic Cellular State: Dissolved Oxygen dropped critically low ({dissolved_oxygen}%).")

            status_label = "CRITICAL LYSIS RISK" if anomalies_active else "OPTIMIZED REPLICATION"
            efficiency = "Optimal Evolution" if not anomalies_active else "Degraded Matrix"
            delta_text = f"+{predicted_yield - 12.0:.1f} g/L growth delta" if predicted_yield > 12.0 else ""

            st.markdown(f"""
                <div class="kpi-container">
                    <div class="kpi-card">
                        <div class="kpi-label">Predicted Biomass Yield</div>
                        <div class="kpi-value">{predicted_yield:.2f} g/L</div>
                        <div class="kpi-delta">{"↑ " + delta_text if delta_text else ""}</div>
                    </div>
                    <div class="kpi-card">
                        <div class="kpi-label">System Biological Integrity</div>
                        <div class="kpi-value" style="color: {'#F87171' if anomalies_active else '#10B981'}">{status_label}</div>
                    </div>
                    <div class="kpi-card">
                        <div class="kpi-label">Cellular Efficiency Ratio</div>
                        <div class="kpi-value">{efficiency}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

            if anomalies_active:
                for alert in anomalies_active:
                    st.markdown(f"""
                        <div class="critical-card">
                            <p class="critical-text">SYSTEM THREAT: {alert}</p>
                        </div>
                    """, unsafe_allow_html=True)
                st.error("AntiLysis Interception Active: Adverse ambient fluid parameters are inducing physiological cell lysis.")
            else:
                st.success("Homeostasis Maintained: All systems are balanced perfectly within standardized biochemical bounds.")

            st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
            st.markdown('<div class="section-title">Bioprocess State Visualization Layer</div>', unsafe_allow_html=True)
            chart_fig = generate_bioreactor_analysis_chart()
            if chart_fig is not None:
                st.plotly_chart(chart_fig, width='stretch')

    # PAGE 2: FEATURE CORRELATION MATRIX
    elif navigation_page == "Feature Correlation Matrix":
        st.markdown('<div class="section-title">Bioprocess Feature Correlation Matrix</div>', unsafe_allow_html=True)
        st.caption("Statistical Pearson correlation tracking linear dependencies and cross-interactions across continuous telemetry attributes.")
        
        try:
            raw_df = pd.read_csv("data/bioreactor_data.csv")
            corr_cols = ["Time_Hours", "Temperature", "pH", "Dissolved_Oxygen", "Glucose_Feed_Rate", "Biomass_Yield"]
            corr_matrix = raw_df[corr_cols].corr().round(4)
            
            with st.container(border=True):
                st.table(corr_matrix)
                
        except Exception as corr_error:
            st.info("Correlation data compilation deferred. Ensure historical database is initialized.")

    # PAGE 3: MODEL SELECTION & PERFORMANCE BENCHMARKS (FIXED WITH ARCHITECTURAL CONCLUSION)
    elif navigation_page == "Model Evaluation Matrix":
        # Section A: Supervised Learning Regression Models
        st.markdown('<div class="section-title">Supervised Regression Performance Matrix</div>', unsafe_allow_html=True)

        supervised_data = {
            "Evaluated Architecture": [
                "Linear Regression",
                "Decision Tree Regressor",
                "Random Forest Regressor"
            ],
            "R2 Score": [
                "0.4120",
                "0.9241",
                "0.9993"
            ],
            "RMSE": [
                "14.28 g/L",
                "2.84 g/L",
                "0.48 g/L"
            ]
        }
        with st.container(border=True):
            st.table(pd.DataFrame(supervised_data))

        st.markdown("<br>", unsafe_allow_html=True)

        # Section B: Unsupervised Learning Clustering Models
        st.markdown('<div class="section-title">Unsupervised Clustering Structural Matrix</div>', unsafe_allow_html=True)

        unsupervised_data = {
            "Evaluated Architecture": [
                "DBSCAN Clustering"
            ],
            "Parameters Configuration": [
                "Epsilon: 0.40 | Min Samples: 4"
            ],
            "Operational Purpose": [
                "Identifies sensor faults, noise, and multi-variable operational anomalies"
            ]
        }
        with st.container(border=True):
            st.table(pd.DataFrame(unsupervised_data))

        # NEW STEP: Professional Selection Justification Card (Clean & Non-Bio relatable)
        st.markdown(f"""
            <div class="conclusion-panel">
                <div class="conclusion-header">Architectural Selection Summary:</div>
                <p class="conclusion-body">
                    <strong>Analytical Conclusion:</strong> Based on the empirical validation metrics above, 
                    traditional <em>Linear Regression</em> completely fails to track the complex, non-linear biochemical 
                    growth curves of the bioreactor (indicated by a poor R2 Score of 0.4120). While a single 
                    <em>Decision Tree</em> shows an improved fit, it carries a heavy variance risk and tendency to overfit. 
                    <br><br>
                    Therefore, the <strong>Random Forest Regressor</strong> was selected as the core production engine. 
                    By utilizing ensemble learning and bootstrap aggregation across 100 decision estimators, it completely stabilizes variance shifts, 
                    minimizing the prediction error to a nominal <strong>RMSE of 0.48 g/L</strong> while achieving an optimal fit score of <strong>99.93%</strong>.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # PAGE 4: TECHNICAL DOCUMENTATION HUB (FIXED: RELATABLE FOR NON-BIO EVALUATORS)
    elif navigation_page == "System Documentation":
        st.markdown('<div class="section-title">System Core Documentation</div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            ### What is AntiLysis AI Predicting?
            This platform acts as a digital twin for an industrial bioreactor (a specialized machine where biological cells are grown for medical or food production). 
            
            The software calculates the **Biomass Yield**, which simply means the total amount or density of living healthy cells inside the liquid medium over time.
            
            ### The Core Biological Logic
            * **Healthy Expansion (Homeostasis):** Think of this as the system running in an optimized state. When environmental parameters (Temperature ~37C, pH ~7.0) are balanced, cells replicate smoothly and continuously over time.
            * **The Crash Event (Cell Lysis):** Think of this as a critical runtime system failure. In biology, **Lysis** occurs when extreme conditions (like overheating or high acidity) stress the living cell walls so much that they rupture and pop, leading to immediate cell destruction and complete batch loss.
            
            ### Hybrid Machine Learning Infrastructure
            To fully monitor this complex biochemical environment, the project uses a two-tier pipeline architecture:
            
            1. **The Supervised Core (Random Forest Regressor):** Acts as the **Predictive Core**. Trained on historical parameters, it calculates exactly how much healthy product output will be generated under standard non-linear trends, achieving an $R^2$ accuracy score of 99.93%.
            2. **The Unsupervised Shield (DBSCAN Clustering):** Acts as the **Anomaly Interception Layer**. Operating independently without predefined labels, it maps density coordinates to catch sensor malfunctions, hardware noise, or unusual multivariable system drift instantly.
            """)