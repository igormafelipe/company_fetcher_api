# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 12/5/2022

VALID_LOCATIONS = set(["ca", "ne"])
LOCATION = {"ca" : "en_CA",
            "ne" : "nl_NL"}

# FILE PATH OF CVS FILES WITH COMPANY NAMES
INPUT_BASE_PATH = "/home/igormafelipe/"
INPUT_FILE_PATH = {"ca" : INPUT_BASE_PATH + "data/canada_list.xlsx",
                   "ne" : INPUT_BASE_PATH + "data/netherlands_list.xlsx"}

# FILE THAT CONTAINS COMPANY'S TO BE IGNORED
IGNORE_BASE_PATH = "/home/igormafelipe/mysite/caches/"
IGNORE_FILE_PATH = {"ca" : IGNORE_BASE_PATH + "canada_ignore_list.csv",
                    "ne" : IGNORE_BASE_PATH + "netherlands_ignore_list.csv"}

# LABEL OF THE COL THAT CONTAINS THE ROLE OF THE JOBS
# IF THERE IS NO SUCH COL, PUT None, but this will take MUCH LONGER
FILTER_COL_LABEL = {"ca" : 'Occupation',
                    "ne" : None}

# LABEL OF THE COL THAT CONTAINS THE COMPANY NAMES
COMPANY_COL_LABEL = {"ca" : 'Employer',
                     "ne" : 'Companies'}

# NAME OF FILES WITH JOBS FROM SPECIFIC COUNTRY'S
FILTERED_FILE_NAME = {"ca" : "filtered_sheet_canada.csv",
                      "ne" : "filtered_sheet_netherlands.csv"}

# PATH TO FILTERED FILES
FILTERED_BASE_PATH = "/home/igormafelipe/mysite/caches/"
FILTERED_PATH = {"ca" : FILTERED_BASE_PATH + FILTERED_FILE_NAME["ca"],
                 "ne" : FILTERED_BASE_PATH + FILTERED_FILE_NAME["ne"]}