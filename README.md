# Career Jet Job Search API with Sponsorship Verification

This API aims to assist job seekers in identifying job opportunities where companies are authorized to sponsor applicants for their roles within a specific country. It utilizes the Career Jet API to locate job openings and validates companies' sponsorship eligibility by cross-referencing with the embassy's verified list of sponsoring entities.

## API Endpoints

`GET http://igormafelipe.pythonanywhere.com/getjobs`
This endpoint returns a list of job openings that are allowed to sponsor, verified by the embassy of the job seeker's country.

### Query Parameters

`
{
    "location": ["ca" | "ne"],
    "keywords_include": ["Software Engineer"],
    "keywords_exclude": ["Senior", "Junior", "Manager", "Associate", "Contract", "Part Time"]
}`


Explanation:
- `"ca"` represents Canada.
- `"ne"` represents the Netherlands.

## Sample Request with AXIOS
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

## To Do
Plans:
- Implement a token system for authentication.
- Enhance input filtering using Elastic Search.
- Expansion of available locations.

