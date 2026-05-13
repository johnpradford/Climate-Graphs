import pandas as pd

from backend.transformations.bom_row_classifier import (
    BOMRowClassifier,
)


class ClimatologyTransformer:
    """Transform raw BOM climatology tables into canonical schema."""

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

        for _, row in table.iterrows():

            statistics_label = row.get('Statistics')

            variable_name = (
                BOMRowClassifier
                .classify_row(statistics_label)
            )

            if variable_name is None:
                continue

            values = []

            for month in cls.MONTH_COLUMNS:

                value = row.get(month)

                values.append(value)

            canonical[variable_name] = values

        return canonical
