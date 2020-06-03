import requests
from bs4 import BeautifulSoup

# Sending a request to wiki webpage
URL = 'https://en.wikipedia.org/wiki/Battle_of_the_Bulge'
response = requests.get(URL)
# print(dir(response))

# Get the content 
content = response.content
# print(content)
# Converting to Beautiful soup object
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# Find an element 
results = soup.findAll('a href', title = "Category")
print(results)

def get_citations_needed_count(URL):
    citation = results
    return len(citation)

def get_citations_list(URL):
    citation = results 
    citation_list = []

    for cit in citation:
        cit = cit.parent.text.strip()
        citation_list.append(cit)
    return citation_list


print(get_citations_list(URL))
print(get_citations_needed_count(URL))