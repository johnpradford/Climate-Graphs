import pandas as pd


class RainfallAnomalyCalculator:
    """Calculate rolling rainfall anomalies."""

    @staticmethod
    def rolling_total(df: pd.DataFrame, window: int):

        ordered = df.sort_values(['year', 'month'])

        return (
            ordered['value']
            .rolling(window=window)
            .sum()
        )

    @staticmethod
    def anomaly(observed: float, climatology: float):
        return observed - climatology
