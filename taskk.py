from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://docs.infisign.io/"
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Accept-Language': 'en-US:qn=0.5'})
page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.text, "html.parser")
finaldata = [] 
mainurls=[]
links = soup.find_all("a", attrs={'class': 'category'})
for link in links:
    getlink = link.get('href')
    outerlink = "https://docs.infisign.io" + getlink
    getlink = requests.get(outerlink)
    innerheading = BeautifulSoup(getlink.text, 'html.parser')
    getinnerheading = innerheading.find('h1')
    getfinalheading = getinnerheading.get_text()
    articlelist = innerheading.find_all('ul', attrs={'class': 'articleList'})
    for getarticlelist in articlelist:
        mainlink = getarticlelist.find_all('a')
        for getmainlink in mainlink:
            mainurl = "https://docs.infisign.io" + getmainlink.get('href')
            if mainurl not in finaldata:
                finaldata.append((getfinalheading, mainurl))
          
            
df = pd.DataFrame(finaldata, columns=['category', 'links'])
df.to_csv('infisign2.csv', index=False)
print("*****")