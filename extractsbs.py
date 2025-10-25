import requests
from bs4 import BeautifulSoup
import os


def get_sbs(sbs):

    """Gets the all the text (unformated) of all 
    SBS curretly listed on one piece wiki"""
    
    url = f'https://onepiece.fandom.com/wiki/{sbs}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    
    return [p.get_text(strip=True) for p in paragraphs]

#create a list for the URL of all currently listed SBS on the wiki (4 to 113) 
allsbsurl = [f'SBS_Volume_{sbs}' for sbs in range(4,113)]

#list to have all the SBS text 
allsbs = []

for sbs in allsbsurl:
    allsbs.append(get_sbs(sbs))

with open('sbstext.txt','w', encoding='utf-8') as file:
    for text in allsbs:
        file.write('\n'.join(text))
        file.write('\n-----------------NEXT SBS--------------\n')