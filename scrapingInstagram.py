from bs4 import BeautifulSoup
import requests
url_to_scrape = "https://practice.geeksforgeeks.org/courses/"

def getHtmlDocument(url_to_scrape):
    response = requests.get(url_to_scrape)
    return response.text

html_document = getHtmlDocument(url_to_scrape)
soup = BeautifulSoup(html_document, 'html.parser')

print(soup.prettify())
print(soup.title)