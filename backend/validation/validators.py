from typing import Iterable


class ClimateValidationError(Exception):
    pass


class ClimateValidator:
    @staticmethod
    def validate_month_count(months: Iterable) -> None:
        months = list(months)

        if len(months) != 12:
            raise ClimateValidationError(
                f'Expected 12 months but received {len(months)}'
            )

    @staticmethod
    def validate_rainfall(value: float) -> None:
        if value < 0:
            raise ClimateValidationError(
                'Rainfall values cannot be negative'
            )

    @staticmethod
    def validate_temperature(value: float) -> None:
        if value < -20 or value > 60:
            raise ClimateValidationError(
                f'Temperature value outside expected range: {value}'
            )
