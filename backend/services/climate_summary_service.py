from backend.acquisition.mock_climate_data import generate_mock_dataset
from backend.plotting.rainfall_temperature_plot import RainfallTemperaturePlot
from backend.exports.png_export import PNGExporter


class ClimateSummaryService:
    def generate(self, station: str, survey_year: int):
        dataset = generate_mock_dataset(station, survey_year)

        plotter = RainfallTemperaturePlot()
        figure = plotter.generate(dataset)

        exporter = PNGExporter()
        output_path = exporter.export(
            figure,
            f'{station.lower().replace(" ", "_")}_summary.png'
        )

        return {
            'station': station,
            'survey_year': survey_year,
            'output_path': str(output_path),
            'record_count': len(dataset.records)
        }
