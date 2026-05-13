import pandas as pd


class RollingStatistics:
    @staticmethod
    def rolling_rainfall(series: pd.Series, window: int) -> float:
        return round(series.tail(window).sum(), 2)

    @staticmethod
    def rolling_mean_temperature(series: pd.Series, window: int) -> float:
        return round(series.tail(window).mean(), 2)
