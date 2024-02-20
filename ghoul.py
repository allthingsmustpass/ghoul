import requests
from bs4 import BeautifulSoup
import csv

def extractData(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Error:", response.status_code)

def saveInFormat(soup, nameFile):
    with open(nameFile, 'w', newline='', encoding='utf-8') as csvFile:
        csvwriter = csv.writer(csvFile)

        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for header in headers:
            csvwriter.writerow(['Title', header.text.strip()])

        images  = soup.find_all(['img'])
        for image in images:
            csvwriter.writerow(['Image', image['src']])
        
        texts = soup.find_all(['p'])
        for text in texts:
            csvwriter.writerow(['Text', text.text.strip()])

        links = soup.find_all(['a'])
        for link in links:
            href = link.get('href')
            if href:
                csvwriter.writerow(['Link', link['href']])
            else:
                print('Link with no href')

if __name__ == "__main__":
    url = 'url'
    namefile = 'content.csv'
    contentExtracted = extractData(url)
    if contentExtracted:
        saveInFormat(contentExtracted, namefile)
        print("Content saved!")
    else:
        print("Error:", url)
