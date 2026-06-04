from src.data_preprocessing import initiate_data_preprocessing
from src.model_training import initiate_model_training
from src.anomaly_detection import train_anomaly_detector


class TrainingPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):
        print("[Pipeline] Triggering end-to-end training architecture...")

        # Step 1: Preprocessing & Splitting
        X_train, X_test, y_train, y_test = initiate_data_preprocessing(
            data_path="data/bioreactor_data.csv"
        )

        # Step 2: Training the unified Supervised Pipeline
        model_path = initiate_model_training(X_train, X_test, y_train, y_test)

        # Step 3: Training the Unsupervised DBSCAN Engine
        train_anomaly_detector(X_train)

        print(f"Execution complete. Training matrices saved successfully.")