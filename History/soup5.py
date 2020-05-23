import requests
from bs4 import BeautifulSoup
url = 'https://conjugator.reverso.net/conjugation-german-verb-%20machen.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml", from_encoding='utf-8')
cards_file = open("cards.csv", "a")


input_verbs_file=open('verbs.txt',"r")
lines=input_verbs_file.readlines()
result=[]
for x in lines:
    result.append(x)
input_verbs_file.close()
#english_verb
#print(result[1].split(',')[0])

#german_verb
#print(result[1].split(',')[1])

#divTag=soup.find_all("div", {"class": "blue-box-wrap"})
divTag=soup.find_all("div", {"class": "result-block-api"})
#person=divTag.find_all("i", {"class": "graytxt"})
for x in range(len(result)):
    english_verb=(result[x].split(',')[0])


divTag2=divTag[0].find_all("div", {"class": "blue-box-wrap"})
print("conjugations found: " + str(len(divTag2)))

for tense in range(len(divTag2)):
    li_tag = divTag2[tense].find_all("li")
    for x in range(len(li_tag)):
        if x <=2:
            cards_file.write(english_verb + '<br>' + divTag2[tense].attrs.get('mobile-title') + '<br>' + "Singular " + str(x+1) + ',' + li_tag[x].text)
        else:
            cards_file.write(english_verb + '<br>' + divTag2[tense].attrs.get('mobile-title') + '<br>' + "Plural " + str(x-2) + ',' + li_tag[x].text)

f.close()
