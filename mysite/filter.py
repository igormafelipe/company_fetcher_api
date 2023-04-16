# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 4/14/2022
# Purpose: Filters the jobs from a certain location based on position.
#          Can exlude jobs with certain keywords on their title, like Senior, etc.
#          Can get jobs with ONLY certain keywords on their title
import sys
sys.path.append('../')
sys.path.append('./')

import pandas as pd
import search_params as sp

# information to be fetched from each job post
FETCH_KEY = "title"

# Fetches jobs that contain position_include in their title and do not contain
# position_exclude. Location determines which country is fetched.
def get_jobs(location: str, position_include: list[str], position_exclude: list[str]):
    pos_include = "|".join([x.lower() for x in position_include])
    pos_exclude = "|".join([x.lower() for x in position_exclude])

    jobs = pd.read_csv(sp.FILTERED_PATH[location], index_col=[0])

    jobs_position = jobs[jobs[FETCH_KEY].str.lower().str.contains(pos_include)]
    if len(position_exclude) > 0:
        jobs_position = jobs_position[~jobs_position[FETCH_KEY].str.lower().str.contains(pos_exclude)]

    return jobs_position.to_dict(orient='records')

#without senior it does not work, look at it!
print(get_jobs("ca", ["Software Engineer"], []))