import requests
from bs4 import BeautifulSoup
url = 'http://stash.compjour.org/samples/webpages/whitehouse-press-briefings-page-50.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

print ((soup.find_all('i')))
urls = []
for h in soup.find_all('h3'):
    urls.append(h.find('a').attrs['href'])

for x in range(len(urls)):
    print(urls[x])
