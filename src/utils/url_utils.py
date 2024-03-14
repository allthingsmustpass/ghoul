import requests
from bs4 import BeautifulSoup

def checkUrl(url):
    """
    Check if the URL is reachable.

    Args:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is reachable (status code 2xx), False otherwise.
    """
    try:
        response = requests.head(url)
        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def responseUrl(url):
    """
    Retrieve and parse the HTML content of a URL.

    Args:
        url (str): The URL to retrieve the content from.

    Returns:
        BeautifulSoup: Parsed HTML content of the URL.
    """
    response = requests.get(url)
    webContent = BeautifulSoup(response.content, 'html.parser')
    return webContent
