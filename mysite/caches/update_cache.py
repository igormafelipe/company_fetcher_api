# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 4/14/2022
# Purpose: A script that is run once every 3 days, updating the current job listing.

import sys
sys.path.append('../')
sys.path.append('./')

import pandas as pd
import os
from tqdm import tqdm
import careerjet_api_client
import search_params as sp
from get_company_names import get_company_names
from requests import get

# information to be fetched from each job post
# >> DO NOT CHANGE <<
FETCH_KEYS = ["locations", "date", "title", "company", "url"]

# Excludes jobs that require more than EXPERIENCE_EXCLUSION years of experience
EXPERIENCE_EXCLUSION = 15

def output_csv(pd: object, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)
    pd.to_csv(out_file)

# Ignored companies are skipped when fetching jobs, as they have no jobs listed.
# These are updated every week based on populate_cache.
def get_ignored_companies(location):
    to_ignore = pd.read_csv(sp.IGNORE_FILE_PATH[location]).values.tolist()
    to_ignore = [company for num, company in to_ignore]
    return to_ignore

def update_cache(companies: dict, location: str):
    all_jobs = {}
    ignored_companies = set(get_ignored_companies(location))
    used = set()
    career_jet_api = careerjet_api_client.CareerjetAPIClient(sp.LOCATION[location]);
    ip = get('https://api.ipify.org').text
    for company in companies:
        for company_possible_name in companies[company]:
            if company_possible_name in ignored_companies:
                continue

            try:
               result_json = career_jet_api.search({
                            'keywords'    : f"{company_possible_name}",
                            'affid'       : sp.AFF_KEY,
                            'user_ip'     : f"{ip}",
                            'url'         : 'https://igormafelipe.pythonanywhere.com',
                            'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                        }).json()
            except Exception as e:
                print(f"The search failed!\n{e} {company_possible_name}\n")

            if 'jobs' not in result_json:
                print(f"Nothing found for {company_possible_name}\n")
                continue
            
            # Process found jobs
            for job in result_json['jobs']:
                job_key = job['title'] + job['date'] + job['company']
                
                if (job_key in used or job['company'] == ""):
                    continue

                # Extract job details using FETCH_KEYS
                for key in FETCH_KEYS:
                    if key not in all_jobs:
                        all_jobs[key] = []
                    all_jobs[key].append(job[key])
                used.add(job_key)
                
    return all_jobs

# Updates the cvs file with the information of the companies and jobs
def update(location: str):
    try:
        possible_companies: dict = get_company_names([], location)
        jobs = update_cache(possible_companies, location)
        
        companies_out_file = sp.FILTERED_FILE_NAME[location]
        output_csv(pd.DataFrame.from_dict(jobs), companies_out_file)
    except Exception as e:
        print(f"Something went wrong\n{e}\nAborting...")
    return []
