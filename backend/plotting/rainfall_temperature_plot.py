import matplotlib.pyplot as plt

from backend.models.climate_dataset import ClimateDataset


class RainfallTemperaturePlot:
    def generate(self, dataset: ClimateDataset):
        months = [record.month for record in dataset.records]
        rainfall = [record.rainfall for record in dataset.records]
        max_temp = [record.max_temp for record in dataset.records]
        min_temp = [record.min_temp for record in dataset.records]

        figure, rainfall_axis = plt.subplots(figsize=(14, 8))

        rainfall_axis.bar(
            months,
            rainfall,
            color='#577A7A',
            alpha=0.75,
            width=0.7,
            label='Rainfall'
        )

        rainfall_axis.set_ylabel(
            'Rainfall (mm)',
            fontsize=16,
            fontweight='bold'
        )

        rainfall_axis.tick_params(labelsize=14)

        temperature_axis = rainfall_axis.twinx()

        temperature_axis.plot(
            months,
            max_temp,
            color='#2E5D5D',
            linewidth=2.5,
            marker='o',
            markersize=6,
            label='Max Temp'
        )

        temperature_axis.plot(
            months,
            min_temp,
            color='#B8A63A',
            linewidth=2.5,
            marker='o',
            linestyle='--',
            markersize=6,
            label='Min Temp'
        )

        temperature_axis.set_ylabel(
            'Temperature (°C)',
            fontsize=16,
            fontweight='bold'
        )

        temperature_axis.tick_params(labelsize=14)

        rainfall_axis.set_facecolor('#ECECEC')
        figure.patch.set_facecolor('#ECECEC')

        rainfall_axis.grid(
            linestyle='--',
            linewidth=0.5,
            alpha=0.35
        )

        rainfall_axis.axvspan(
            len(months) - 1.5,
            len(months) - 0.5,
            color='#D8E8B5',
            alpha=0.5,
        )

        figure.suptitle(
            f'{dataset.station} Climate Summary',
            fontsize=18,
            fontweight='bold'
        )

        figure.tight_layout()

        return figure
