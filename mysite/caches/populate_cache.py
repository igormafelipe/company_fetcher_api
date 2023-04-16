# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 4/14/2022
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

# Controls max range of exclusion of experience. If a position requests more than
# EXPERIENCE_EXCLUSION years of experience, it will not be filtred out regardless
# of range.
EXPERIENCE_EXCLUSION = 15

# Outputs the given pd object to excel
def output_csv(pd: object, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)
    pd.to_csv(out_file)

# Gets the desired jobs from the career jet website based on location and company
# Parameters:
#         companies: List of company names to be looked up
#         location: Which country we are looking for
# Returns:
#         all_jobs: Dictionary of company jobs found.
#         to_ignore: Set of company names that had no job listings to them.
def fetch_positions(companies: dict, location):
    all_jobs = {}
    to_ignore = set([])
    used = set()
    cja = careerjet_api_client.CareerjetAPIClient(sp.LOCATION[location]);
    ip = get('https://api.ipify.org').text
    for company in tqdm(companies):
        for company_possible_name in companies[company]:
            try:
               result_json = cja.search({
                            'keywords'    : f"{company_possible_name}",
                            'affid'       : '069f8b7ca985d7c45f58ba3cfdf773da',
                            'user_ip'     : f"{ip}",
                            'url'         : 'https://igormafelipe.pythonanywhere.com',
                            'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                        });
            except Exception as e:
                to_ignore.add(company_possible_name)
                print(f"whooops, the search failed!\n{e} {company_possible_name}\n")

            if 'jobs' not in result_json:
                to_ignore.add(company_possible_name)
                continue

            for job in result_json['jobs']:
                job_key = job['title'] + job['date'] + job['company']
                if (job_key in used or job['company'] == ""):
                    continue

                for key in FETCH_KEYS:
                    if key not in all_jobs:
                        all_jobs[key] = []
                    all_jobs[key].append(job[key])
                used.add(job_key)
    return all_jobs, to_ignore

# Gets the list of job listings for a specified country's list.
# Populates the ignore list, for companies that had no jobs listed.
# Takes about 1 hour to run.
def populate(location: str):
    try:
        possible_companies: dict = get_company_names([], location)
        jobs, to_ignore = fetch_positions(possible_companies, location)
        ignore_out_file = sp.IGNORE_FILE_PATH[location]
        companies_out_file = sp.FILTERED_FILE_NAME[location]
        output_csv(pd.DataFrame(to_ignore), ignore_out_file)
        output_csv(pd.DataFrame.from_dict(jobs), companies_out_file)
    except Exception as e:
        print(f"Whoops, something went wrong\n{e}\nAborting...")
    return []