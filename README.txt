# Career Jet Job Search API with Sponsorship Verification

This API is designed to help job seekers find job openings that are sponsored by companies verified by the embassy of the job seeker's country. It uses Career Jet API to find job openings and verifies whether the companies can sponsor by cross-referencing the embassy's list of verified companies.

API Endpoints
Search Jobs
This endpoint returns a list of job openings that are sponsored by companies verified by the embassy of the job seeker's country.

Endpoint URL
GET /api/search

Query Parameters
q (required): The search query string.
location (required): The location where the job openings should be searched.
country (required): The country of the job seeker.
page: The page number to return (default is 1).
per_page: The number of job openings to return per page (default is 10).
Example Request
sql
Copy code
GET /api/search?q=software+engineer&location=san+francisco&country=united+states&page=1&per_page=10
Example Response
json
Copy code
{
  "success": true,
  "data": [
    {
      "title": "Software Engineer",
      "company": "Acme Inc.",
      "location": "San Francisco, CA",
      "sponsorship": true,
      "url": "https://example.com/job/123"
    },
    {
      "title": "Backend Engineer",
      "company": "Beta Corp.",
      "location": "San Francisco, CA",
      "sponsorship": true,
      "url": "https://example.com/job/456"
    }
  ]
}
Authentication
This API does not require authentication.

Rate Limiting
This API is rate-limited to 100 requests per hour per IP address.

Data Sources
This API uses the following data sources:

Career Jet API: https://www.careerjet.com/partners/api/
Embassy of the job seeker's country: https://www.example.com/embassy/
Support
If you have any questions or issues, please contact us at support@example.com.
