from backend.acquisition.bom_url_builder import BOMUrlBuilder


def test_monthly_climatology_url():

    url = BOMUrlBuilder.monthly_climatology_url(
        '009021'
    )

    assert '009021' in url
    assert url.endswith('.shtml')
