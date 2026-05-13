class BOMUrlBuilder:
    """Construct BOM climate data endpoints."""

    BASE_CLIMATOLOGY_URL = (
        'http://www.bom.gov.au/climate/averages/tables/'
    )

    @classmethod
    def monthly_climatology_url(cls, station_id: str):
        """Build BOM monthly climatology URL."""

        return (
            f'{cls.BASE_CLIMATOLOGY_URL}'
            f'cw_{station_id}.shtml'
        )
