import matplotlib.pyplot as plt

from plotting.theme import THEME, COLOURS


class CombinedClimatePlot:
    """Render combined rainfall and temperature climate graph."""

    def render(self, rainfall_df, temperature_df, output_path):

        fig, ax1 = plt.subplots(
            figsize=(THEME['width_inches'], THEME['height_inches']),
            dpi=THEME['dpi']
        )

        ax1.bar(
            rainfall_df['label'],
            rainfall_df['value'],
            color=COLOURS['rainfall_bar']
        )

        ax1.set_ylabel('Rainfall (mm)')

        ax2 = ax1.twinx()

        ax2.plot(
            temperature_df['label'],
            temperature_df['tmax'],
            color=COLOURS['tmax_line'],
            linewidth=2
        )

        ax2.plot(
            temperature_df['label'],
            temperature_df['tmin'],
            color=COLOURS['tmin_line'],
            linewidth=2
        )

        ax2.set_ylabel('Temperature (°C)')

        fig.savefig(
            output_path,
            bbox_inches='tight'
        )
