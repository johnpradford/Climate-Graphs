from backend.models.climate_dataset import ClimateDataset, ClimateRecord


def generate_mock_dataset(station: str, survey_year: int):
    months = [
        'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'
    ]

    records = []

    for index, month in enumerate(months):
        records.append(
            ClimateRecord(
                month=month,
                rainfall=round(20 + index * 8.5, 1),
                max_temp=round(34 - index * 1.2, 1),
                min_temp=round(22 - index * 0.7, 1),
            )
        )

    return ClimateDataset(
        station=station,
        survey_year=survey_year,
        records=records,
    )
