# Career Jet Job Search API with Sponsorship Verification

This API aims to assist job seekers in identifying job opportunities where companies are authorized to sponsor applicants for their roles within a specific country. It utilizes the Career Jet API to locate job openings and validates companies' sponsorship eligibility by cross-referencing with the embassy's verified list of sponsoring entities.

## API Endpoints

```GET http://igormafelipe.pythonanywhere.com/getjobs```<br/><br/>
This endpoint returns a list of job openings that are allowed to sponsor, verified by the embassy of the job seeker's country.

### Query Parameters

```
{
     "location": ["ca" | "ne"],
     "keywords_include": ["Software Engineer"],
     "keywords_exclude": ["Senior", "Junior", "Manager", "Associate", "Contract", "Part Time"]
}
```

Explanation:
- `"ca"` represents Canada.
- `"ne"` represents the Netherlands.

## Sample Request with AXIOS
```
    await axios(
      {
          method: "GET",
          url: "http://igormafelipe.pythonanywhere.com/getjobs",
          params: {
              location: "ca",
              keywords_include: ["Software Engineer"],
              keywords_exclude: ["Senior", "Junior", "Manager", "Associate", "Contract", "Part Time"],
          },
          })
          .then((response) => {
              const res = response.data;
              setLoading(false);
              navigate('results', { state: { data: res } })
          })
          .catch((error) => {
              if (error.response) {
              console.log(error.response);
              }
      });
```

## Sample Response
    { 
      "success": true, 
      "jobs": [
                { 
                  "locations": "Toronto, ON", 
                  "date": "Wed, 26 Apr 2023 07:57:22 GMT", 
                  "title": "Software Engineering II", 
                  "company": "Big Viking Games", 
                  "url": "https://URL_TO_JOB"
                },
                { 
                  "locations": "Toronto, ON", 
                  "date": "Wed, 26 Apr 2023 07:57:22 GMT", 
                  "title": "Software Engineering II", 
                  "company": "Big Viking Games", 
                  "url": "https://URL_TO_JOB"
                },
              ]
    }
    
### Authentication
This API does not require authentication.

### Rate Limiting
This API is rate-limited to 10 requests per minute.

### Data Sources
This API utilizes the following data sources:

- Career Jet API: [Career Jet API](https://www.careerjet.com/partners/api/)
- Embassy of the job seeker's country: [Canada](https://www.canada.ca/en.html), [Netherlands](https://www.netherlandsworldwide.nl)

## Local Setup
1. Update `AFF_KEY` on `search_params.py` with your Career Jet API affiliate key.
2. Update the variable `DATA_ABSOLUTE_PATH` in `search_params.py` to the absolute path of the data folder
3. Run the general_tests.py to ensure flask server works
4. Initialize the flask server by running `python3 flask_app.py`
5. Update the cache in your server by running the populate function in populate_cache.py, or the update function in update_cache.py. The difference is, update takes into account the companies listed in `ignore_list` from the previous populate run. These companies had no job listings, are are ignored until we run populate again.   

## To Do
Plans:
- Implement a token system for authentication.
- Enhance input filtering using Elastic Search.
- Expansion of available locations.

