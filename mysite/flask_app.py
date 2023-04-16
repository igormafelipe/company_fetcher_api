# A very simple Flask Hello World app for you to get started with...
import sys
sys.path.append('../')
sys.path.append('./')

from flask import Flask, request
from filter import get_jobs
import search_params as sp
import json

#Starts flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    return json.dumps("To fetch, request from /getjobs")


# Expects the following payload:
#   Mandatory:
#       location: The country code of the job.
#       keywords_include: Keywords looked for. If Software Engineer, will find jobs with that in the title
#   Optional:
#       keywords_exclude: Keywords to be filtered out. Can be level of seniority, type of job, etc.
#
#   Example payload:
#   data: {
#       location: "ca",
#       keywords_include: "Software Engineering,Software,Programmer,Developer",
#       keywords_exclude: "Senior,Staff,Lead,III,manager"
#   }
#
# Not case sensitive.
@app.route('/getjobs', methods=['GET'])
def data():
    location = request.args.get("location")
    keywords_include = request.args.get("keywords_include")
    keywords_exclude = request.args.get("keywords_exclude")
    if location is None:
        return 'Bad request! location not found', 400

    if location not in sp.VALID_LOCATIONS:
        return 'Invalid location!', 400

    if keywords_include is None:
        return 'Bad request! keywords_include not found', 400

    keywords_include = [k.strip() for k in keywords_include.split(',') if k.strip()]
    keywords_exclude = [] if keywords_exclude == None else keywords_exclude.split(',')

    jobs = get_jobs(location, keywords_include, keywords_exclude)

    return json.dumps(jobs)