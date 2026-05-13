from pathlib import Path


class PNGExporter:
    def __init__(self, output_dir: str = 'outputs'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export(self, figure, filename: str):
        output_path = self.output_dir / filename

        figure.savefig(
            output_path,
            dpi=400,
            bbox_inches='tight'
        )

        return output_path
