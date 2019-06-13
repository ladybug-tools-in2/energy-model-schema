schedule_ruleset = {
    'type': 'ScheduleRuleset',
    'name': 'Schedule Ruleset',
    'schedule_type_limits': {
        'type': 'ScheduleTypeLimits',
        'numeric_type': {
            'numerictype': {
                'type': 'ScheduleContinuous'
            }
        },
        'unit_type': 'Temperature',
        'name': 'Numeric Type',
        'lower_limit_value': 0,
        'upper_limit_value': 20
    },
    'default_day_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 1',
        'interpolate_to_timestep': 'No',
        'day_values': [
                {
                    'hour': 24,
                    'minute': 60,
                    'value_until_time': 20
                }
        ],
    },
    'summer_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 2',
        'interpolate_to_timestep': 'No',
        'day_values': [
                {
                    'hour': 24,
                    'minute': 60,
                    'value_until_time': 20
                }
        ],
    },
    'winter_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 3',
        'interpolate_to_timestep': 'No',
        'day_values': [
                {
                    'hour': 24,
                    'minute': 60,
                    'value_until_time': 20
                }
        ]
    },
    'schedule_rule': [
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 4',
                    'interpolate_to_timestep': 'No',
                    'day_values': [
                        {
                            'hour': 24,
                            'minute': 60,
                            'value_until_time': 20
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 1,
                    'day': 1
                },
                'time': {
                    'hour': 0,
                    'minute': 0
                },
                'is_leap_year': False
            },
            'end_period': {
                'date': {
                    'month': 12,
                    'day': 31
                },
                'time': {
                    'hour': 24,
                    'minute': 60
                },
                'is_leap_year': False
            },
            'name': 'Schedule Rule 1',
            'apply_sunday': 'Yes',
            'apply_monday': 'Yes',
            'apply_tuesday': 'Yes',
            'apply_wednesday': 'Yes',
            'apply_thursday': 'Yes',
            'apply_friday': 'Yes',
            'apply_saturday': 'Yes',
            'apply_holiday': 'Yes'
        }
    ]
}

