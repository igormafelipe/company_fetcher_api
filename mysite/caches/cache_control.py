# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 4/16/2022
# Purpose: A script run daily. Controls which scrips will be run to maintain
#          the jobs cache.

import datetime
today = datetime.date.today()
weekday = today.weekday()

if weekday == 0:
    from populate_cache import populate
    try:
        populate("ca")
        populate("ne")
    except Exception as e:
        # todo: add a log file
        print(e)
elif weekday % 2 == 0:
    from update_cache import update
    try:
        update("ca")
        update("ne")
    except Exception as e:
        # todo: add a log file
        print(e)