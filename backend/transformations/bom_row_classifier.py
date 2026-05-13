class BOMRowClassifier:
    """Classify BOM climatology rows semantically."""

    VARIABLE_PATTERNS = {
        'tmax_c': [
            'mean maximum temperature',
            'maximum temperature',
        ],
        'tmin_c': [
            'mean minimum temperature',
            'minimum temperature',
        ],
        'rainfall_mm': [
            'mean rainfall',
            'rainfall',
        ],
        'rain_days': [
            'mean number of rain days',
            'rain days',
        ],
    }

    @classmethod
    def classify_row(cls, label: str):

        if label is None:
            return None

        cleaned_label = str(label).lower()

        for variable, patterns in cls.VARIABLE_PATTERNS.items():

            for pattern in patterns:

                if pattern in cleaned_label:
                    return variable

        return None
