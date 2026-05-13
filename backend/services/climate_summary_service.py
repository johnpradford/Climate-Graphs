from backend.acquisition.mock_climate_data import generate_mock_dataset
from backend.acquisition.station_metadata import get_station_metadata
from backend.exports.png_export import PNGExporter
from backend.logging.logger import get_logger
from backend.plotting.rainfall_temperature_plot import RainfallTemperaturePlot


logger = get_logger()


class ClimateSummaryService:
    def generate(self, station: str, survey_year: int):
        logger.info(f'Generating climate summary for {station}')

        station_metadata = get_station_metadata(station)

        dataset = generate_mock_dataset(station, survey_year)

        plotter = RainfallTemperaturePlot()
        figure = plotter.generate(dataset)

        exporter = PNGExporter()

        output_path = exporter.export(
            figure,
            f'{station.lower().replace(" ", "_")}_summary.png'
        )

        logger.info(f'Climate summary exported to {output_path}')

        return {
            'station': station,
            'station_metadata': (
                station_metadata.__dict__
                if station_metadata
                else None
            ),
            'survey_year': survey_year,
            'output_path': str(output_path),
            'record_count': len(dataset.records)
        }
