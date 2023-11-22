# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 11/22/2023

import pandas as pd
from typing import List
from search_params import FILTERED_PATH

# Field used to fetch jobs
FETCH_KEY = "title"

def get_jobs(location: str, positions_to_include: List[str], positions_to_exclude: List[str]):
    include_criteria = "|".join([position.lower() for position in positions_to_include])
    exclude_criteria = "|".join([position.lower() for position in positions_to_exclude])

    jobs = pd.read_csv(FILTERED_PATH[location], index_col=[0])

    jobs_with_included_positions = jobs[jobs[FETCH_KEY].str.lower().str.contains(include_criteria)]

    # Exclude jobs that contain positions to exclude
    if positions_to_exclude:
        jobs_with_included_positions = jobs_with_included_positions[~jobs_with_included_positions[FETCH_KEY].str.lower().str.contains(exclude_criteria)]

    return jobs_with_included_positions.to_dict(orient='records')