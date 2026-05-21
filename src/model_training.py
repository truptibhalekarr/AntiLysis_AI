from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from src.evaluation import evaluate_model_performance
from src.utils import save_object


def initiate_model_training(X_train, X_test, y_train, y_test):
    print("🌲 [Modeling] Fusing Scaler and Random Forest into an ML Pipeline...")

    # Creating the strict sequence pipeline object
    # Step 1: Scale the data, Step 2: Pass directly to Random Forest
    antilysis_pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("rf_regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
        ]
    )

    print("⚡ Fitting data features through the pipeline layers...")
    antilysis_pipeline.fit(X_train, y_train)

    # Predict directly using raw X_test (Pipeline internal scale apne aap handle karega)
    test_predictions = antilysis_pipeline.predict(X_test)

    # Evaluate using evaluation module
    evaluate_model_performance(y_true=y_test, y_pred=test_predictions)

    # Save the single fused pipeline object (Includes both Scaler AND Model!)
    model_path = "artifacts/model.pkl"
    save_object(file_path=model_path, obj=antilysis_pipeline)

    print(
        "✓ [Modeling] Entire integrated pipeline saved successfully as model.pkl."
    )
    return model_path