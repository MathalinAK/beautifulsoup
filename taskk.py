from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://docs.infisign.io/"
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Accept-Language': 'en-US:qn=0.5'})
page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
outerheading = []
getouterheading = soup.find_all('h3')
#print(getouterheading)
for getheading in getouterheading:
    outerheading.append(getheading.text)
    #print(outerheading)
finaldata = []
links = soup.find_all("a", attrs={'class': 'category'})
#print(links)
for link in links:
    getlink = link.get('href')
    outerlink = "https://docs.infisign.io" + getlink
    getlink = requests.get(outerlink)
    innerheading = BeautifulSoup(getlink.text, 'html.parser')
    getinnerheading = innerheading.find_all('h1')
    #print(getinnerheading)
    for finalheading in getinnerheading:
        getfinalheading = finalheading.get_text()
    articlel = []
    articlelist = innerheading.find_all('ul', attrs={'class': 'articleList'})
    #print(articlelist)
    for getarticlelist in articlelist:
        mainlink = getarticlelist.find_all('a')
        #print(mainlinks)
        for getmainlink in mainlink:
            mainurl = "https://docs.infisign.io" + getmainlink.get('href')
            finaldata.append((getfinalheading, mainurl))
            #print(mainurl)
            #articlel.append(mainurl)
        #print(articlel)
    #for article in articlel:
    
    #print(finaldata)
df = pd.DataFrame(finaldata, columns=['Product', 'Article'])
df.to_csv('infisign2.csv', index=False)
print("*****")