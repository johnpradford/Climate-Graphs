class AnomalyClassifier:
    @staticmethod
    def classify_rainfall(anomaly: float) -> str:
        if anomaly >= 100:
            return 'substantially above average'

        if anomaly >= 25:
            return 'above average'

        if anomaly <= -100:
            return 'substantially below average'

        if anomaly <= -25:
            return 'below average'

        return 'near average'

    @staticmethod
    def classify_temperature(anomaly: float) -> str:
        if anomaly >= 2:
            return 'well above average'

        if anomaly >= 0.5:
            return 'above average'

        if anomaly <= -2:
            return 'well below average'

        if anomaly <= -0.5:
            return 'below average'

        return 'near average'
