import requests
import re

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url='https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Computer%20Science%20Intern&f_TPR=r86000&isDsc=true&start=0&count=50'

res = requests.get(url=target_url, headers=headers)

out = re.findall(r"urn:li:jobPosting:([0-9]+)", str(res.content))

target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
urls = []
for j in out:
    urls.append(target_url.format(j))

for url in urls:
    resp = requests.get(url=url)
    s = str(resp.text)
    title_identifier = "topcard__title\">";
    title_strt = s.find(title_identifier)+len(title_identifier);
    title = s[title_strt:s.find("<", title_strt)]

    location_identifier = "class=\"topcard__flavor topcard__flavor--bullet\">\n              ";
    location_strt = s.find(location_identifier) + len(location_identifier);
    location = s[location_strt:s.find("<", location_strt)]

    company_identifier = "rel=\"noopener\" target=\"_blank\">\n";
    company_strt = s.find(company_identifier) + len(company_identifier)
    company = s[company_strt:s.find("<", company_strt)]

    print(title)
    print("URL:      " + url)
    print("COMPANY:  " + company.strip())
    print("LOCATION: " + location.strip() + "\n")