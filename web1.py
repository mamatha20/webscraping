import requests
from bs4 import BeautifulSoup
import json
user=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
data=BeautifulSoup(user.text,"html.parser")
def moviedata():
    list=[]
    mainDiv=data.find("div",class_="body_main container")
    # print(mainDiv)
    subDiv=mainDiv.find("table",class_="table")
    # print(subDiv)
    tableall=subDiv.find_all('tr')
    # print(tableall)
    for i in tableall:
        d1={}
        alltds=i.find_all('td')
        for j in alltds:
            rank=i.find('td',class_="bold").get_text()[:-1]
            d1["rank"]=int(rank)
            # print(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            d1["rating"]=int(rating)
            # print(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            d1["review"]=int(review)
            # print(review)
            movieName=i.find("a",class_="unstyled articleLink")["href"][3:]
            d1["movieName"]=movieName
            moviceurl=i.find("a",class_="unstyled articleLink")["href"]
            m="https://www.rottentomatoes.com"+moviceurl
            d1["moviceurl"]=m
            # print(movieName)
            Year=i.find('a',class_="unstyled articleLink").text
            year1=Year.strip()
            d1["Year"]=int(Year[-5:-1])
        # print(d1)
        list.append(d1.copy())
        if {} in list:
            list.remove({})
        print(list)
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
moviedata()