import pandas as pd


REQUIRED_MONTHS = set(range(1, 13))


class ClimateValidator:
    """Validation checks for climate datasets."""

    @staticmethod
    def validate_month_completeness(df: pd.DataFrame):

        months = set(df['month'].unique())

        missing = REQUIRED_MONTHS - months

        if missing:
            raise ValueError(f'Missing months: {missing}')

    @staticmethod
    def validate_duplicates(df: pd.DataFrame):

        duplicates = df.duplicated(
            subset=['station_id', 'variable', 'year', 'month']
        )

        if duplicates.any():
            raise ValueError('Duplicate climate records detected')
