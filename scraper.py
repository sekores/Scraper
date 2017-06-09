#Unser Programm erstellt eine CSV Datei und gibt die Top 3 Wörter aus
# imports
from bs4 import BeautifulSoup
import requests
import csv

def top3(my_list):
    result = {}
    for i in my_list:
        result.update({i:my_list.count(i)})

    sortedValue = sorted(result.values(), reverse=True)
    sortedKeys = sorted(result, key=result.get, reverse=True)
    
    for i in range(3):
        print(str(sortedValue[i]) + ":" + str(sortedKeys[i]))
        
# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: heise.de
def main():

    fobj = open('heise_https.csv', 'w')      # open file
    csvw = csv.writer(fobj)     # create csv writer

    
    heise_https_url_site0 = "https://www.heise.de/thema/https?seite=0"
    heise_https_url_site1 = "https://www.heise.de/thema/https?seite=1"
    heise_https_url_site2 = "https://www.heise.de/thema/https?seite=2"
    heise_https_url_site3 = "https://www.heise.de/thema/https?seite=3"

    text=[]     #zum Ausgeben unserer Top 3 Wörter

    # seite 1
    content = getPage(heise_https_url_site0).find("div",{"id":"container"})
    content = content.find("div",{"class":"keywordliste"})
    content = content.findAll("header")
    content = content[1:]

    for c in range(len(content)):
        text=text+content[c].contents[0].replace("\n                 ","").split(" ")
        csvw.writerow(content[c].contents)

    # seite 2
    content = getPage(heise_https_url_site1).find("div",{"id":"container"})
    content = content.find("div",{"class":"keywordliste"})
    content = content.findAll("header")
    content = content[1:]

    for c in range(len(content)):
        text=text+content[c].contents[0].replace("\n                 ","").split(" ")
        csvw.writerow(content[c].contents)

    # seite 3
    content = getPage(heise_https_url_site2).find("div",{"id":"container"})
    content = content.find("div",{"class":"keywordliste"})
    content = content.findAll("header")
    content = content[1:]

    for c in range(len(content)):
        text=text+content[c].contents[0].replace("\n                 ","").split(" ")
        csvw.writerow(content[c].contents)

    # seite 4
    content = getPage(heise_https_url_site3).find("div",{"id":"container"})
    content = content.find("div",{"class":"keywordliste"})
    content = content.findAll("header")
    content = content[1:]

    for c in range(len(content)):
        text=text+content[c].contents[0].replace("\n                 ","").split(" ")
        csvw.writerow(content[c].contents)

    fobj.close()                                # close file
    print("\nDONE !\n\n\nhttps://www.heise.de/thema/https was scraped completely.\n")

    top3(text)      #wandelt unser text Array zu einem Dictionary und gibt die
                    #höchsten 3 Values(Anzahl Häufigkeit) mit den Keys aus
    
    
# main program
if __name__ == '__main__':
    main()
