from typing import List


MONTHS = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]


def rotate_months(survey_month: str) -> List[str]:
    if survey_month not in MONTHS:
        raise ValueError(f'Invalid month: {survey_month}')

    index = MONTHS.index(survey_month)

    return MONTHS[index + 1:] + MONTHS[:index + 1]
