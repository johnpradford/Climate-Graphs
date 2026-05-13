import pandas as pd


class ClimatologyEngine:
    def monthly_average(self, dataframe: pd.DataFrame, column: str):
        values = pd.to_numeric(dataframe[column], errors='coerce')

        return round(values.mean(), 2)

    def annual_rainfall(self, dataframe: pd.DataFrame, column: str):
        values = pd.to_numeric(dataframe[column], errors='coerce')

        return round(values.sum(), 2)
