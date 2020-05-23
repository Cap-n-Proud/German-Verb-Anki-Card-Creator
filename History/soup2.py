import requests
from bs4 import BeautifulSoup
url = 'https://conjugator.reverso.net/conjugation-german-verb-%20machen.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')


divTag=soup.find_all("div", {"mobile-title": "Indikativ Futur I"})
#person=divTag.find_all("i", {"class": "graytxt"})

result=[]
print divTag[0]
#print len(divTag.find_all("i", {"class": "graytxt"}))

for p in divTag:
    person = p.find_all("i", {"class": "graytxt"}) #+ ' ' + tag.find_all("i", {"class": "auxgraytxt"})

for v in divTag:
    verb = v.find_all("i", {"class": "auxgraytxt"}) #+ ' ' + tag.find_all("i", {"class": "auxgraytxt"})


for i,p in zip(verb, person):
    result.append(str(p.text) + ' ' + str(i.text))

for x in result:
    print(x)
