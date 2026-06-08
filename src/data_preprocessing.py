import pandas as pd
from sklearn.model_selection import train_test_split


def initiate_data_preprocessing(data_path="data/bioreactor_data.csv"):
    print(" [Preprocessing] Loading and splitting biological matrices...")

    df = pd.read_csv(data_path)

    # FIX: Added 'Time_Hours' to features because Yield is heavily dependent on time!
    feature_cols = [
        "Time_Hours",
        "Temperature",
        "pH",
        "Dissolved_Oxygen",
        "Glucose_Feed_Rate",
    ]
    X = df[feature_cols]
    y = df["Biomass_Yield"]

    # Simple clean split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("✓ [Preprocessing] Split completed successfully.")
    return X_train, X_test, y_train, y_test