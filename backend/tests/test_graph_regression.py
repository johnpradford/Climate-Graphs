from backend.acquisition.mock_climate_data import generate_mock_dataset
from backend.plotting.rainfall_temperature_plot import RainfallTemperaturePlot


def test_graph_generation():
    dataset = generate_mock_dataset('Perth Metro', 2025)

    plotter = RainfallTemperaturePlot()

    figure = plotter.generate(dataset)

    assert figure is not None
