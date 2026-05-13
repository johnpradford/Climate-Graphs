import pandas as pd


class ClimatologyTransformer:
    """Transform raw BOM climatology tables into canonical schema."""

    VARIABLE_LOOKUP = {
        1: 'tmax_c',
        2: 'tmin_c',
        4: 'rainfall_mm',
        6: 'rain_days',
    }

    MONTH_COLUMNS = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec',
    ]

    @classmethod
    def extract_canonical_monthly_data(
        cls,
        table: pd.DataFrame,
    ) -> pd.DataFrame:

        canonical = pd.DataFrame({
            'month': list(range(1, 13)),
        })

        for row_index, variable_name in cls.VARIABLE_LOOKUP.items():

            if row_index >= len(table):
                continue

            row = table.iloc[row_index]

            values = []

            for month in cls.MONTH_COLUMNS:

                value = row.get(month)

                values.append(value)

            canonical[variable_name] = values

        return canonical
