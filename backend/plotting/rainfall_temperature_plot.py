import matplotlib.pyplot as plt

from backend.models.climate_dataset import ClimateDataset


class RainfallTemperaturePlot:
    def generate(self, dataset: ClimateDataset):
        months = [record.month for record in dataset.records]
        rainfall = [record.rainfall for record in dataset.records]
        max_temp = [record.max_temp for record in dataset.records]
        min_temp = [record.min_temp for record in dataset.records]

        figure, rainfall_axis = plt.subplots(figsize=(12, 7))

        rainfall_axis.bar(
            months,
            rainfall,
            color='#577A7A',
            alpha=0.8,
            label='Rainfall'
        )

        rainfall_axis.set_ylabel('Rainfall (mm)')

        temperature_axis = rainfall_axis.twinx()

        temperature_axis.plot(
            months,
            max_temp,
            color='#2E5D5D',
            linewidth=2,
            marker='o',
            label='Max Temp'
        )

        temperature_axis.plot(
            months,
            min_temp,
            color='#B8A63A',
            linewidth=2,
            marker='o',
            label='Min Temp'
        )

        temperature_axis.set_ylabel('Temperature (°C)')

        rainfall_axis.set_facecolor('#ECECEC')
        figure.patch.set_facecolor('#ECECEC')

        rainfall_axis.grid(
            linestyle='--',
            linewidth=0.5,
            alpha=0.4
        )

        figure.tight_layout()

        return figure
