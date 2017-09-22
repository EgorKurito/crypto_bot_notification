import csv
import urllib
from bs4 import BeautifulSoup

BASE_URL = 'https://www.bfxdata.com/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_ = 'container')

    projects = []

    for row in table.find_all('div', class_ = 'container'):
        for row1 in table.find_all('div', class_ = 'row landingrow'):
            for row2 in row.find_all('div', class_ = 'price clearfix'):

                projects.append({
                    'title': row2.find('p', class_ = 'price_text').a.text,
                    'price': row2.p.text,
                    })
    return projects

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Название', 'Цена'))

        for project in projects:
            writer.writerow((project['title'], project['price']))

def main():
    projects = []
    projects.extend(parse(get_html(BASE_URL)))
    save(projects, 'projects.csv')

if __name__ == '__main__':
    main()
