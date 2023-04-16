Company Filter: A certified way of applying for jobs that offer sponsorship.

Coded by: Igor Mafra Felipe, github: https://github.com/igormafelipe

Description: Given a country and a list o keywords, return jobs from companies
             that are listed on that country's embassy website as holders of
             the right to sponsor.

How to use: Send a GET request to igormafelipe.pythonanywhere.com/getjobs with
            the following payload:
            {
                'location' : '',
                'keywords_include' : [],
                'keywords_exclude' : [],
            }

            location options:
                "ca" = Canada
                "ne" = Netherlands
                more coming soon.

            keywords_include: An array of keywords that must be present in the
                              job title. Not case sensitive.
                              Example: ["software", "programming", "data"]

            keywords_exclude: An array of keywords that, if present in the title,
                              exclude that job from the items to be returned.
                              Example: ["Senior", "manager", "Staff"]