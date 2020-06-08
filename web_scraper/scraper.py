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
results = soup.findAll('sup', class_="noprint Inline-Template Template-Fact")
# print(results)

def get_citations_needed_count(URL):
    return len(results)

def get_citations_needed_report(URL):
    # takes in a url, returns a string 
    # String should have a line for each citation, in order

    #list to push the results of the parents of the citation
    list_of_results = []
    
    # string to push results too
    new_string = ""

    for each in results:
        parent_citation = each.parent.text.strip()
        list_of_results.append(parent_citation)

    # iterate of all of the text from the citations
    for new_line in list_of_results: 
        # adding a new line inbetween credit due to Nate C-K from stack overflow  
        new_string += new_line + "\r\n" + "\r\n"
    print(new_string)


print(get_citations_needed_count(URL))
get_citations_needed_report(URL)