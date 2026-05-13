from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ClimateRecord(BaseModel):
    """Canonical internal climate record schema."""

    station_id: str
    station_name: str
    variable: str
    year: int
    month: int
    value: float
    dataset_type: str
    quality_flag: Optional[str] = None
    source: Optional[str] = None
    retrieved_at: Optional[datetime] = None
