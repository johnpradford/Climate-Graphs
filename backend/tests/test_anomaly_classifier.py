from backend.anomaly_analysis.anomaly_classifier import AnomalyClassifier


def test_rainfall_above_average():
    classification = AnomalyClassifier.classify_rainfall(150)

    assert classification == 'substantially above average'


def test_temperature_near_average():
    classification = AnomalyClassifier.classify_temperature(0.2)

    assert classification == 'near average'
