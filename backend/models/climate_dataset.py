from pydantic import BaseModel


class ClimateRecord(BaseModel):
    month: str
    rainfall: float
    max_temp: float
    min_temp: float


class ClimateDataset(BaseModel):
    station: str
    survey_year: int
    records: list[ClimateRecord]
