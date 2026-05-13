import pandas as pd


class LiveAnomalyEngine:
    @staticmethod
    def rainfall_anomaly(observed: pd.Series, climatology: pd.Series):
        return round(observed.sum() - climatology.sum(), 2)

    @staticmethod
    def temperature_anomaly(observed: pd.Series, climatology: pd.Series):
        return round(observed.mean() - climatology.mean(), 2)
