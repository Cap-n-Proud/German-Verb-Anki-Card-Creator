import requests
from bs4 import BeautifulSoup
url = 'https://conjugator.reverso.net/conjugation-german-verb-%20machen.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')

divTag=soup.find_all("div", {"class": "blue-box-wrap"})
#person=divTag.find_all("i", {"class": "graytxt"})



print("conjugations found: " + str(len(divTag)))

for tense in range(len(divTag)):
    print('----------------------------')
    print ("tense: " + str(tense))
    graytxt = divTag[tense].find_all("i", {"class": "graytxt"})
    auxgraytxt = divTag[tense].find_all("i", {"class": "auxgraytxt"})
    particletxt = divTag[tense].find_all("i", {"class": "particletxt"})
    verbtxt = divTag[tense].find_all("i", {"class": "verbtxt"})
    auxgraytxt = divTag[tense].find_all("i", {"class": "auxgraytxt"})
    print(divTag[tense].find("p").text)
    print("graytxt: " + str(len(graytxt)))
    print("auxgraytxt: " + str(len(auxgraytxt)))
    print("particletxt: " + str(len(particletxt)))
    print("verbtxt: " + str(len(verbtxt)))
    for x in range(6):
        conjugation=""
        if len(graytxt):
            conjugation = conjugation + ' ' + graytxt[x].text
        if len(auxgraytxt):
            conjugation  = conjugation  + ' ' + auxgraytxt[x].text
        if len(particletxt):
            conjugation  = conjugation  + ' ' + particletxt[x].text
        if len(verbtxt):
            conjugation  = conjugation   + '' + verbtxt[x].text
        #if len(auxgraytxt):
        #     conjugation  = conjugation   + ' ' + auxgraytxt[x].text
        #print(len(auxgraytxt))
        print(conjugation)
