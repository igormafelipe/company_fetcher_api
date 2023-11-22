# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 11/22/2023

# Purpose: A script run daily. Controls which scrips will be run to maintain
#          the jobs cache.

import datetime
import sys
sys.path.append('../')
sys.path.append('./')

FULL_FETCH_DAY = 0 #Monday
UPDATE_DAYS = [1, 2, 4, 6] #Tuesday, Wednesday, Friday, Sunday

today = datetime.date.today()
weekday = today.weekday()

if weekday == FULL_FETCH_DAY:
    from populate_cache import populate
    try:
        populate("ca")
        populate("ne")
    except Exception as e:
        # todo: add a log file
        print(e)
elif weekday in UPDATE_DAYS:
    from update_cache import update
    try:
        update("ca")
        update("ne")
    except Exception as e:
        # todo: add a log file
        print(e)