# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 11/22/2023

# Meta information
AFF_KEY = ""

# Valid locations and their corresponding codes
VALID_LOCATIONS = set(["ca", "ne"])
LOCATION = {
    "ca": "en_CA",
    "ne": "nl_NL"
}

# Paths for input and ignore files
INPUT_BASE_PATH = "/home/igormafelipe/"
INPUT_FILE_PATH = {
    "ca": INPUT_BASE_PATH + "data/canada_list.xlsx",
    "ne": INPUT_BASE_PATH + "data/netherlands_list.xlsx"
}

IGNORE_BASE_PATH = "/home/igormafelipe/mysite/caches/"
IGNORE_FILE_PATH = {
    "ca": IGNORE_BASE_PATH + "canada_ignore_list.csv",
    "ne": IGNORE_BASE_PATH + "netherlands_ignore_list.csv"
}

# Labels for columns in the files
FILTER_COL_LABEL = {
    "ca": 'Occupation',
    "ne": None  # If there's no such column, put None (but this might increase processing time)
}

COMPANY_COL_LABEL = {
    "ca": 'Employer',
    "ne": 'Companies'
}

# Filenames and paths for filtered files
FILTERED_FILE_NAME = {
    "ca": "filtered_sheet_canada.csv",
    "ne": "filtered_sheet_netherlands.csv"
}

FILTERED_BASE_PATH = "/home/igormafelipe/mysite/caches/"
FILTERED_PATH = {
    "ca": FILTERED_BASE_PATH + FILTERED_FILE_NAME["ca"],
    "ne": FILTERED_BASE_PATH + FILTERED_FILE_NAME["ne"]
}