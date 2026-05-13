import pandas as pd


class BOMSchemaHandler:
    REQUIRED_COLUMNS = {
        'Month',
        'Rainfall',
    }

    def normalise_columns(self, dataframe: pd.DataFrame):
        dataframe.columns = [
            str(column).strip().replace('\n', ' ')
            for column in dataframe.columns
        ]

        return dataframe

    def validate_required_columns(self, dataframe: pd.DataFrame):
        missing = self.REQUIRED_COLUMNS.difference(dataframe.columns)

        if missing:
            raise ValueError(
                f'Missing required BOM columns: {sorted(missing)}'
            )

        return True
