import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup)

        # Extract information based on HTML elements
        # For example, let's extract all the text from <p> tags
        paragraphs = soup.find_all('h6')

        # Print the text content of each paragraph
        for paragraph in paragraphs:
            print(paragraph.get_text())

    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")

# Example usage:
url_to_crawl = 'https://uis.ptithcm.edu.vn'
crawl_website(url_to_crawl)
