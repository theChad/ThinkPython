# Problem 5.1

import time

def print_time():
    cur_time = time.time()
    seconds_in_day = 24 * 60 * 60
    time_in_days = cur_time/seconds_in_day
    days = int(time_in_days)
    partial_day_in_hours = (time_in_days % 1) * 24
    hours = int(partial_day_in_hours)
    partial_hour_in_minutes = (partial_day_in_hours % 1) * 60
    minutes = int(partial_hour_in_minutes)
    seconds = (partial_hour_in_minutes % 1) * 60
    print('It has been', days, 'days,', hours, 'hours,', minutes, 'minutes and', seconds, 'seconds since the epoch.')

print_time()
