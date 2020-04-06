import requests
from bs4 import BeautifulSoup
url = 'https://conjugator.reverso.net/conjugation-german-verb-%20machen.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')

#divTag=soup.find_all("div", {"class": "blue-box-wrap"})
divTag=soup.find_all("div", {"class": "result-block-api"})
#person=divTag.find_all("i", {"class": "graytxt"})


divTag2=divTag[0].find_all("div", {"class": "blue-box-wrap"})
print("conjugations found: " + str(len(divTag2)))

for tense in range(len(divTag2)):
    print('----------------------------')
    li_tag = divTag2[tense].find_all("li")
    print ("tense: " + str(tense))
    print(divTag2[tense].attrs.get('mobile-title'))
    print("items found: " + str(len(li_tag)))

    for x in range(len(li_tag)):
            print(li_tag[x].text)
