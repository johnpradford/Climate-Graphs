import pandas as pd


MONTH_ORDER = [
    1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12
]


MONTH_LABELS = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}


def rotate_months(df: pd.DataFrame, survey_month: int):
    """Rotate climate year so survey month becomes final month."""

    order = MONTH_ORDER[survey_month:] + MONTH_ORDER[:survey_month]

    month_rank = {
        month: index
        for index, month in enumerate(order)
    }

    rotated = df.copy()

    rotated['month_order'] = rotated['month'].map(month_rank)

    return rotated.sort_values('month_order')
