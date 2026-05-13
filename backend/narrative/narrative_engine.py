from backend.anomaly_analysis.summary_metrics import ClimateMetric


class NarrativeEngine:
    def summarise_rainfall(self, metric: ClimateMetric) -> str:
        if metric.anomaly > 0:
            return (
                f'{metric.name} rainfall was above the long-term average '
                f'by {metric.anomaly} mm.'
            )

        if metric.anomaly < 0:
            return (
                f'{metric.name} rainfall was below the long-term average '
                f'by {abs(metric.anomaly)} mm.'
            )

        return f'{metric.name} rainfall was near average.'
