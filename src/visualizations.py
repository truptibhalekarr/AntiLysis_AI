import plotly.express as px
import pandas as pd
import numpy as np

def generate_bioreactor_analysis_chart():
    """
    Generates a 2D spatial density distribution chart mapping Temperature vs pH.
    Explicitly forces clear discrete color categories for standard runs and anomalies.
    """
    try:
        # Load the core dataset tracking historical runs
        df = pd.read_csv("data/bioreactor_data.csv")
        
        # Absolute structural check to isolate anomaly coordinates safely
        if "Anomaly_Score" in df.columns:
            # Enforce dynamic mapping tracking both supervised limits and unsupervised outliers
            df["DBSCAN Interception State"] = df["Anomaly_Score"].apply(
                lambda x: "System Outlier / Noise" if int(x) == -1 else "Normal Baseline Run"
            )
        else:
            # Algorithmic backup: if columns are flat, explicitly force mathematical outliers on boundary shifts
            temp_outliers = (df["Temperature"] < 36.2) | (df["Temperature"] > 37.8)
            ph_outliers = (df["pH"] < 6.7) | (df["pH"] > 7.3)
            df["DBSCAN Interception State"] = np.where(
                temp_outliers | ph_outliers, "System Outlier / Noise", "Normal Baseline Run"
            )

        # Enforcing explicit sorting order to ensure both color tracking classes are registered in legend
        df = df.sort_values(by="DBSCAN Interception State", ascending=False)

        # Generating the 2D Spatial Density Grid mapping Temperature vs pH space directly
        fig = px.scatter(
            df,
            x="Temperature",
            y="pH",
            color="DBSCAN Interception State",
            color_discrete_map={
                "Normal Baseline Run": "#10B981",    # Clean Emerald Green for stable baseline
                "System Outlier / Noise": "#EF4444"  # High-Visibility Vivid Red for anomaly vectors
            },
            labels={
                "Temperature": "Reactor Core Temperature (°C)",
                "pH": "Media Ionization Value (pH)"
            },
            template="plotly_dark"
        )

        # Enforcing executive dark minimalist layout geometry
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=10, b=10),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0.01,
                title_text=""
            ),
            xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False)
        )

        # Optimizing hover metadata details for live deployment tracking
        fig.update_traces(
            marker=dict(size=5.5, opacity=0.85),
            hovertemplate="<b>%{customdata[0]}</b><br>Temperature: %{x}°C<br>pH: %{y}<extra></extra>",
            customdata=np.stack((df["DBSCAN Interception State"],), axis=-1)
        )

        return fig

    except Exception as chart_error:
        # Graceful exception fallback to prevent interface rendering crash
        return None