import pandas as pd


class ClimateBaselineValidator:
    @staticmethod
    def validate_monthly_coverage(dataframe: pd.DataFrame):
        if len(dataframe) < 12:
            raise ValueError('Incomplete long-term climatology coverage')

    @staticmethod
    def validate_missing_values(dataframe: pd.DataFrame):
        if dataframe.isnull().sum().sum() > 0:
            raise ValueError('Missing climatology values detected')
