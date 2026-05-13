from backend.anomaly_analysis.anomaly_classifier import AnomalyClassifier


class PatternDetection:
    @staticmethod
    def rainfall_summary(anomaly: float) -> str:
        classification = AnomalyClassifier.classify_rainfall(anomaly)

        return (
            f'Rainfall conditions during the survey period were '
            f'{classification}.'
        )

    @staticmethod
    def temperature_summary(anomaly: float) -> str:
        classification = AnomalyClassifier.classify_temperature(anomaly)

        return (
            f'Temperature conditions during the survey period were '
            f'{classification}.'
        )
