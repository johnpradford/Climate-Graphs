import matplotlib.pyplot as plt


class ClimateSummaryFigure:
    def __init__(self):
        self.figure, self.axis = plt.subplots(figsize=(12, 7))

    def apply_theme(self):
        self.figure.patch.set_facecolor('#ECECEC')
        self.axis.set_facecolor('#ECECEC')

        self.axis.grid(
            linestyle='--',
            linewidth=0.5,
            alpha=0.4
        )

    def save(self, output_path: str):
        self.figure.savefig(
            output_path,
            dpi=400,
            bbox_inches='tight'
        )
