from sklearn.metrics import root_mean_squared_error, r2_score


def evaluate_model_performance(y_true, y_pred):
    """Calculates regression metrics to verify algorithm safety."""
    r2 = r2_score(y_true, y_pred)

    rmse = root_mean_squared_error(y_true, y_pred)

    print("\n --- ANTI-LYSIS AI SYSTEM PERFORMANCE ---")
    print(f"✓ R² Score (Accuracy Metric) : {r2:.4f}")
    print(f"✓ Root Mean Squared Error (RMSE)  : {rmse:.2f} g/L")
    print("-------------------------------------------\n")

    return r2, rmse