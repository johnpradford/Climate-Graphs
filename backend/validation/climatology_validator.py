import pandas as pd


class ClimatologyValidator:
    """Validate canonical climatology datasets."""

    REQUIRED_COLUMNS = [
        'month',
        'tmax_c',
        'tmin_c',
        'rainfall_mm',
    ]

    @classmethod
    def validate(cls, df: pd.DataFrame):

        validation_results = {
            'valid': True,
            'errors': [],
            'warnings': [],
        }

        missing_columns = [
            column
            for column in cls.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:

            validation_results['valid'] = False

            validation_results['errors'].append(
                f'Missing columns: {missing_columns}'
            )

        if len(df) != 12:

            validation_results['warnings'].append(
                'Climatology does not contain 12 months'
            )

        if 'tmax_c' in df.columns and 'tmin_c' in df.columns:

            invalid_temperature_rows = df[
                df['tmin_c'] > df['tmax_c']
            ]

            if not invalid_temperature_rows.empty:

                validation_results['valid'] = False

                validation_results['errors'].append(
                    'Minimum temperature exceeds maximum temperature'
                )

        if 'rainfall_mm' in df.columns:

            negative_rainfall = df[
                df['rainfall_mm'] < 0
            ]

            if not negative_rainfall.empty:

                validation_results['valid'] = False

                validation_results['errors'].append(
                    'Negative rainfall values detected'
                )

        return validation_results
