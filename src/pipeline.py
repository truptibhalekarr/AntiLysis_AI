from src.data_preprocessing import initiate_data_preprocessing
from src.model_training import initiate_model_training


class TrainingPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):
        print("🚀 [Pipeline] Triggering end-to-end training architecture...")

        # Step 1: Preprocessing & Splitting
        X_train, X_test, y_train, y_test = initiate_data_preprocessing(
            data_path="data/bioreactor_data.csv"
        )

        # Step 2: Training the unified pipeline
        model_path = initiate_model_training(X_train, X_test, y_train, y_test)

        print(f"🏁 [Pipeline] Execution complete. Weights at: {model_path}")