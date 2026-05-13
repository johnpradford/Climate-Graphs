class BOMUrls:
    @staticmethod
    def climate_statistics(station_id: str) -> str:
        return (
            'http://www.bom.gov.au/climate/averages/tables/'
            f'cw_{station_id}.shtml'
        )
