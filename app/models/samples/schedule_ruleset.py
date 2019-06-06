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
    'default_day_schedule': [
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 59,
            'value_until_time': 20
        }
    ],
    'summer_designday_schedule': [
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 59,
            'value_until_time': 20
        }
    ],
    'winter_designday_schedule': [
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 59,
            'value_until_time': 20
        }
    ],
    'schedule_rule': [
        {
            'type': 'ScheduleRule',
            'schedule_day': [
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 23,
                    'minute': 59,
                    'value_until_time': 20
                }
            ],
            'start_period': {
                'month': 1,
                'day': 1,
                'hour': 0,
                'minute': 0,
                'is_leap_year': False
            }, 
            'end_period': {
                'month': 12,
                'day': 31, 
                'hour': 23,
                'minute': 59,
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


schedule_ruleset_1 = {
    'type': 'ScheduleRuleset',
    'name': 'Schedule Ruleset 1',
    'schedule_type_limits': {
        'type': 'ScheduleTypeLimits',
        'numeric_type': {
            'numerictype': {
                'type': 'ScheduleContinuous'
            }
        },
        'unit_type': 'Dimensionless',
        'name': 'Numeric Type',
        'lower_limit_value': 0,
        'upper_limit_value': 1   
    },
    'default_day_schedule': [
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 7,
            'minute': 0,
            'value_until_time': 0
        },
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 19,
            'minute': 0,
            'value_until_time': 1
        },
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 59,
            'value_until_time': 0
        }
    ],
    'summer_designday_schedule': [
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 1',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 0,
            'value_until_time': 0
        }
    ], 
    'winter_designday_schedule': [    
        {
            'type': 'ScheduleDay',
            'name': 'Default Day 2',
            'interpolate_to_timestep': 'No',
            'hour': 23,
            'minute': 0,
            'value_until_time': 0
        }
    ],
    'schedule_rule': [
        {
            'type': 'ScheduleRule', 
            'schedule_day': [
                {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 180', 
                    'interpolate_to_timestep': 'No',
                    'hour': 23,
                    'minute': 0,
                    'value_until_time': 0
                }
            ],
            'start_period': {
                'month': 8,
                'day': 17,
                'hour': 0,
                'minute': 0,
                'is_leap_year': False
            }, 
            'end_period': {
                'month': 12,
                'day': 11, 
                'hour': 23,
                'minute': 59,
                'is_leap_year': False
            },
            'name': 'Schedule Rule 180',
            'apply_sunday': 'Yes',
            'apply_monday': 'No',
            'apply_tuesday': 'No',
            'apply_wednesday': 'No',
            'apply_thursday': 'No',
            'apply_friday': 'No',
            'apply_saturday': 'No',
            'apply_holiday': 'No'
        },
        {
            'type': 'ScheduleRule', 
            'schedule_day': [
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 7,
                    'minute': 0,
                    'value_until_time': 0
                },
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 16,
                    'minute': 0,
                    'value_until_time': 0.3
                },
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 23,
                    'minute': 59,
                    'value_until_time': 0
                }                                
            ],
            'start_period': {
                'month': 8,
                'day': 17,
                'hour': 0,
                'minute': 0,
                'is_leap_year': False
            }, 
            'end_period': {
                'month': 12,
                'day': 11, 
                'hour': 23,
                'minute': 59,
                'is_leap_year': False
            },
            'name': 'Schedule Rule 181',
            'apply_sunday': 'No',
            'apply_monday': 'No',
            'apply_tuesday': 'No',
            'apply_wednesday': 'No',
            'apply_thursday': 'No',
            'apply_friday': 'No',
            'apply_saturday': 'Yes',
            'apply_holiday': 'No'
        },
        {
            'type': 'ScheduleRule', 
            'schedule_day': [
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 7,
                    'minute': 0,
                    'value_until_time': 0
                },
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 19,
                    'minute': 0,
                    'value_until_time': 1
                },
                {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 1',
                    'interpolate_to_timestep': 'No',
                    'hour': 23,
                    'minute': 59,
                    'value_until_time': 0
                }
            ],
            'start_period': {
                'month': 8,
                'day': 17,
                'hour': 0,
                'minute': 0,
                'is_leap_year': False
            }, 
            'end_period': {
                'month': 12,
                'day': 11, 
                'hour': 23,
                'minute': 59,
                'is_leap_year': False
            },
            'name': 'Schedule Rule 182',
            'apply_sunday': 'No',
            'apply_monday': 'Yes',
            'apply_tuesday': 'Yes',
            'apply_wednesday': 'Yes',
            'apply_thursday': 'Yes',
            'apply_friday': 'Yes',
            'apply_saturday': 'No',
            'apply_holiday': 'No'
        }    
    ]      
}