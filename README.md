# Career Jet Job Search API with Sponsorship Verification

This API is designed to help job seekers find job openings that are allowed by country's to sponsor applicants for their positions. It uses Career Jet API to find job openings and verifies whether the companies can sponsor by cross-referencing the embassy's list of verified companies.

## API Endpoints
Search Jobs
This endpoint returns a list of job openings that are allowd to sponsor, verified by the embassy of the job seeker's country.

### Endpoint URL
GET http://igormafelipe.pythonanywhere.com/getjobs

### Query Parameters
    {
        location: ["ca" | "ne"]
        keywords_include: ["Software Engineer"]
        keywords_exclude: ["Senior", "Junior", "Manager", "Associate", "Contract", "Part Time"],
    };

"ca" : "Canada"

"ne" : "Netherlands"

## Example Request with AXIOS
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

## Example Response
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
This API is rate-limited to 100 requests per hour per IP address.

### Data Sources
This API uses the following data sources:

Career Jet API: https://www.careerjet.com/partners/api/

Embassy of the job seeker's country: [canada](https://www.canada.ca/en.html), [netherlands](https://www.netherlandsworldwide.nl)
