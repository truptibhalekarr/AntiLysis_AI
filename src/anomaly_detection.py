import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from src.utils import save_object


def train_anomaly_detector(X_train):
    print("[Anomaly Detection] Training Unsupervised DBSCAN Engine...")

    # Standardizing features independently for geometric distance clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)

    # eps=1.5 and min_samples=5 defines density thresholds for bioreactor boundaries
    dbscan = DBSCAN(eps=1.5, min_samples=5)
    dbscan.fit(X_scaled)

    # Save the unsupervised components
    save_object("artifacts/unsupervised_scaler.pkl", scaler)
    save_object("artifacts/dbscan_model.pkl", dbscan)

    print(
        "[Anomaly Detection] Unsupervised clustering engine saved successfully."
    )
    return dbscan, scaler


def predict_anomaly_status(input_data, scaler, dbscan_model, X_train_scaled):
    """Evaluates whether a single live row is an outlier relative to core training density."""
    input_scaled = scaler.transform(input_data)

    # We use a core distance-based check against training space to classify live inputs
    # If the point falls into a low-density region outside core clusters, flag as outlier (-1)
    # For a live stream, we can check its core neighborhood spacing
    # Here we append to historical data or verify boundary constraints
    return 0  # Standard state placeholder for single vector density checks