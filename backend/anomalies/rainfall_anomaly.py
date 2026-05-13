import pandas as pd


class RainfallAnomalyCalculator:
    """Calculate rainfall anomalies from climatology datasets."""

    @staticmethod
    def rolling_rainfall(
        df: pd.DataFrame,
        window: int = 3,
    ) -> pd.DataFrame:

        anomaly_df = df.copy()

        anomaly_df['rolling_rainfall_mm'] = (
            anomaly_df['rainfall_mm']
            .rolling(window=window, min_periods=1)
            .sum()
        )

        climatology_mean = (
            anomaly_df['rolling_rainfall_mm']
            .mean()
        )

        anomaly_df['rainfall_anomaly_mm'] = (
            anomaly_df['rolling_rainfall_mm']
            - climatology_mean
        )

        return anomaly_df
