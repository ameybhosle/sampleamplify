from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests


main_url = "https://www.justwatch.com/in/movies?release_year_from=2000"
tv_url = "https://www.justwatch.com/in/tv-shows?release_year_from=2000"
base_url = "https://www.justwatch.com"
def functionToGetTop20Movies(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    findAllDivs = soup.find_all("div",class_="title-list-grid")
    findAllDivs = soup.find_all("div",class_ ="title-list-grid__item")
    allLinks = []
    for i in range(0,len(findAllDivs)):
        if(i<=19):
            findI = findAllDivs[i].find("a")["href"]
            allLinks.append(findI)
    return allLinks


def functionToGetTop20TVShoes(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    findAllDivs = soup.find_all("div",class_="title-list-grid")
    findAllDivs = soup.find_all("div",class_ ="title-list-grid__item")
    allLinks = []
    for i in range(0,len(findAllDivs)):
        if(i<=19):
            findI = findAllDivs[i].find("a")["href"]
            allLinks.append(findI)
    return allLinks


allLinksForMovie = functionToGetTop20Movies(main_url)
allLinksForTV = functionToGetTop20TVShoes(tv_url)

alldata = []

# for i in range(0,len(allLinksForMovie)):
#     data = requests.get(base_url+allLinksForMovie[i])
#     soupMovie = BeautifulSoup(data.text)
#     pp = {}
#     pp['type'] = "Movie"
#     movieName = soupMovie.find('div',class_="title-block")
#     movieYear = movieName.find('span').text
#     pp['Title'] = movieName.find('h1').text
#     pp['Movie Year'] = movieYear[2:-2]
#     getGenere = soupMovie.find_all('div',class_="detail-infos")
#     for gener in getGenere:
#         if(gener.find('h3',class_="detail-infos__subheading").text == "Genres"):
#             pp["genre"] = gener.find('div',class_="detail-infos__value").text
#     rating = soupMovie.find_all('div',class_="jw-scoring-listing__rating")
#     rating = rating[1].find_all('span')
#     rating = rating[len(rating)-1].text
#     print(rating)
#     pp['rating'] = rating[1:4]
#     allstream = soupMovie.find('div',class_="buybox-row stream")
#     if allstream == None:
#         pp['Stream'] = "Not Streaming"
#     else:
#         allstream = allstream.find_all('img')
#         allstram = list(map(lambda p:p['alt'],allstream))
#         if len(allstram) > 1:
#             allstram = ",".join(allstram)
#         else:
#             allstram = allstram[0]
#         pp['Stream'] = allstram
#     print("All object is ",pp)
#     alldata.append(pp)

for i in range(0,len(allLinksForTV)):
    print(base_url+allLinksForTV[i])
    data = requests.get(tv_url+allLinksForTV[i])
    soupMovie = BeautifulSoup(data.text,'html.parser')
    pp = {}
    pp['type'] = "Movie"
    movieName = soupMovie.find('div',class_="title-block")
    print(movieName)
    # movieYear = movieName.find('span').text
    # pp['Title'] = movieName.find('h1').text
    # pp['Movie Year'] = movieYear[2:-2]
    getGenere = soupMovie.find_all('div',class_="detail-infos")
    for gener in getGenere:
        if(gener.find('h3',class_="detail-infos__subheading").text == "Genres"):
            pp["genre"] = gener.find('div',class_="detail-infos__value").text
    rating = soupMovie.find_all('div',class_="jw-scoring-listing__rating")
    print(rating)
    # rating = rating[1].find_all('span')
    # rating = rating[len(rating)-1].text
    # print(rating)
    # pp['rating'] = rating[1:4]
    allstream = soupMovie.find('div',class_="buybox-row stream")
    if allstream == None:
        pp['Stream'] = "Not Streaming"
    else:
        allstream = allstream.find_all('img')
        allstram = list(map(lambda p:p['alt'],allstream))
        if len(allstram) > 1:
            allstram = ",".join(allstram)
        else:
            allstram = allstram[0]
        pp['Stream'] = allstram
    print("All object is ",pp)
    alldata.append(pp)

print(alldata)