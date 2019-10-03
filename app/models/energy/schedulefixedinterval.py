"""Schedule Fixed Interval Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import datetime
from app.models.energy.schedulebase import ScheduleTypeLimit
from app.models.common.datetime import Date


class ScheduleFixedIntervalAbridged(BaseModel):
    """Used to specify a start date and a list of values for a period of analysis."""

    type: Enum('ScheduleFixedIntervalAbridged', {
               'type': 'ScheduleFixedIntervalAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    schedule_type_limit: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    timestep: float = Schema(
        1
    )

    interpolate: bool = Schema(
        False
    )


    start_date: Date

    is_leap_year: bool = Schema(
        False
    )

    values: List[float] = Schema(
        ...,
        minItems=24,
        maxItems=8784,
        description='A list of hourly values for the simulation.'
    )

    @validator('values', whole=True)
    def check_range(cls, v, values):
        "Ensure correct number of values."
        if not 'is_leap_year' in values: 
            return v
        if values['is_leap_year'] == False and len(v) < 24 or len(v) > 8760:
            raise ValueError(
        'Number of values can not be lesser than 24 or greater than 8760 for non-leap year')
        elif values['is_leap_year'] == True and len(v) < 24 or len(v) > 8784: 
            raise ValueError(
        'Number of values can not be lesser than 24 or greater than 8784 for leap year')

    placeholder_value = float

if __name__ == '__main__':
    print(ScheduleFixedIntervalAbridged.schema_json(indent=2))
 