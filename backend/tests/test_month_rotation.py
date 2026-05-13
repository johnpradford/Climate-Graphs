from backend.transformations.month_rotation import rotate_months


def test_october_rotation():
    months = rotate_months('Oct')

    assert months[-1] == 'Oct'
    assert months[0] == 'Nov'
