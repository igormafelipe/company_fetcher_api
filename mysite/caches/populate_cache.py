# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 11/22/2023

# Purpose: A script that is run once every 10 days, updating the list of companies to
#          be ignored when fetching information and updating the current job listing.
#          A company is to be ignored if it has no jobs listed.

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

def fetch_positions(companies: dict, location):
    all_jobs = {}
    search_fails = set([])
    used = set()
    career_jet_api = careerjet_api_client.CareerjetAPIClient(sp.LOCATION[location]);
    ip = get('https://api.ipify.org').text
    for company in companies:
        for company_possible_name in companies[company]:
            try:
               career_jet_jobs = career_jet_api.search({
                                'keywords'    : f"{company_possible_name}",
                                'affid'       : sp.AFF_KEY,
                                'user_ip'     : f"{ip}",
                                'url'         : 'https://igormafelipe.pythonanywhere.com',
                                'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                            }).json()
               
            except Exception as e:
                search_fails.add(company_possible_name)
                print(f"The search failed!\n{e} {company_possible_name}\n")

            if 'jobs' not in career_jet_jobs:
                search_fails.add(company_possible_name)
                continue

            # Process found jobs
            for job in career_jet_jobs['jobs']:
                job_key = job['title'] + job['date'] + job['company']
                
                if (job_key in used or job['company'] == ""):
                    continue
                
                # Extract job details using FETCH_KEYS
                for key in FETCH_KEYS:
                    if key not in all_jobs:
                        all_jobs[key] = []
                    all_jobs[key].append(job[key])
                
                used.add(job_key)
                
    return all_jobs, search_fails

# Populates the cvs files with the information of the companies and jobs
# Populates ignore_out_file with the companies that have no jobs listed
def populate(location: str):
    try:
        possible_companies: dict = get_company_names([], location)
        jobs, to_ignore = fetch_positions(possible_companies, location)
        
        ignore_out_file = sp.IGNORE_FILE_PATH[location]
        companies_out_file = sp.FILTERED_FILE_NAME[location]
        
        output_csv(pd.DataFrame(to_ignore), ignore_out_file)
        output_csv(pd.DataFrame.from_dict(jobs), companies_out_file)
    except Exception as e:
        print(f"Something went wrong\n{e}\nAborting...")
    return []
