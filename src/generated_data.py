import os
import numpy as np
import pandas as pd


def generate_bioreactor_data(output_path="data/bioreactor_data.csv", rows=1200):
    np.random.seed(42)
    time = np.linspace(0, 168, rows)

    temperature = np.random.normal(37.0, 0.3, rows)
    ph = np.random.normal(7.0, 0.08, rows)
    dissolved_oxygen = np.random.normal(50.0, 4.0, rows)
    glucose_feed = np.random.normal(3.0, 0.25, rows)

    base_yield = 12.0 + (time * 0.38) + (glucose_feed * 3.5)

    temp_penalty = np.where(temperature > 38.0, (temperature - 38.0) * 14.5, 0)
    ph_penalty = np.where(ph < 6.5, (6.5 - ph) * 22.0, 0)
    do_penalty = np.where(dissolved_oxygen < 22, (22 - dissolved_oxygen) * 1.5, 0)

    biomass_yield = base_yield - temp_penalty - ph_penalty - do_penalty
    biomass_yield = np.clip(biomass_yield, 1.5, 99.0)

    df = pd.DataFrame(
        {
            "Time_Hours": np.round(time, 2),
            "Temperature": np.round(temperature, 2),
            "pH": np.round(ph, 2),
            "Dissolved_Oxygen": np.round(dissolved_oxygen, 2),
            "Glucose_Feed_Rate": np.round(glucose_feed, 2),
            "Biomass_Yield": np.round(biomass_yield, 2),
        }
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✓ [AntiLysis AI] Dataset generated successfully at: {output_path}")


if __name__ == "__main__":
    generate_bioreactor_data()