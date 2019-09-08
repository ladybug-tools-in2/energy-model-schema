"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.schedulebase import ScheduleType
from app.models.common.datetime import Date, Time


class ScheduleDay(BaseModel):
    """Used to describe the daily schedule for a single simulation day."""
    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    values: List[float]

    times: List[List[float]]

    @validator('times', whole=True)
    def check_len_times(cls, v):
        for i in v:
            if len(i) != 2:
                raise ValueError(
                    'Incorrect number of values.'
                )

    interpolate: bool = Schema(
        False
    )


class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleRule', {'type': 'ScheduleRule'})

    schedule_day: ScheduleDay

    apply_sunday: bool = Schema(
        False
    )

    apply_monday: bool = Schema(
        False
    )

    apply_tuesday: bool = Schema(
        False
    )

    apply_wednesday: bool = Schema(
        False
    )

    apply_thursday: bool = Schema(
        False
    )

    apply_friday: bool = Schema(
        False
    )

    apply_saturday: bool = Schema(
        False
    )

    apply_holiday: bool = Schema(
        False
    )

    start_date: List[float]

    @validator('start_date', whole=True)
    def check_len_start_date(cls, v):
        if len(v) != 2:
            raise ValueError(
                'Incorrect number of values.'
            )

    end_date: List[float]

    @validator('end_date', whole=True)
    def check_len_end_date(cls, v):
        if len(v) != 2:
            raise ValueError(
                'Incorrect number of values.'
            )


class ScheduleRulesetAbridged(BaseModel):
    """Used to define a schedule for a default day, further described by ScheduleRule."""

    type: Enum('ScheduleRulesetAbridged', {'type': 'ScheduleRulesetAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_type: ScheduleType = Schema(
        default=None
    )

    default_day_schedule: ScheduleDay

    schedule_rules: List[ScheduleRule] = Schema(
        default=None
    )

    summer_designday_schedule: ScheduleDay = Schema(
        default=None
    )

    winter_designday_schedule: ScheduleDay = Schema(
        default=None
    )


if __name__ == '__main__':
    print(ScheduleRulesetAbridged.schema_json(indent=2))
