# !/usr/bin/env python3
# Coded by Igor M. Felipe
# Last edited: 11/22/2023

from flask import Flask, request, json
from flask_cors import CORS, cross_origin
from filter import get_jobs
import search_params as sp

# Start Flask app
app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def handle_request():
    return json.dumps("To fetch, request from /getjobs")

@app.route('/getjobs', methods=['GET'])
@cross_origin()
def fetch_jobs():
    # Extract parameters from the request
    location = request.args.get("location")
    keywords_include = request.args.get("keywords_include")
    keywords_exclude = request.args.get("keywords_exclude")

    # Validate required parameters
    if location is None:
        return 'Bad request! Location not found', 400

    if location not in sp.VALID_LOCATIONS:
        return 'Invalid location!', 400

    if keywords_include is None:
        return 'Bad request! keywords_include not found', 400

    # Process keywords and split them into lists
    keywords_include = [keyword.strip() for keyword in keywords_include.split(',') if keyword.strip()]
    keywords_exclude = [] if keywords_exclude is None else keywords_exclude.split(',')

    # Fetch jobs based on provided parameters
    jobs = get_jobs(location, keywords_include, keywords_exclude)

    return json.dumps(jobs)