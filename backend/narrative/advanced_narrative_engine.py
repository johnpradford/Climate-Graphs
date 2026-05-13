from backend.anomaly_analysis.anomaly_classifier import AnomalyClassifier


class AdvancedNarrativeEngine:
    def rainfall_narrative(self, anomaly: float):
        classification = AnomalyClassifier.classify_rainfall(anomaly)

        if classification == 'near average':
            return 'Rainfall conditions remained close to long-term averages.'

        return (
            f'Rainfall conditions were {classification} '
            f'relative to long-term averages.'
        )

    def temperature_narrative(self, anomaly: float):
        classification = AnomalyClassifier.classify_temperature(anomaly)

        return (
            f'Temperature conditions were {classification} '
            f'relative to long-term averages.'
        )
