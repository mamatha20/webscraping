import requests
from bs4 import BeautifulSoup
import json
url=requests.get("https://www.rottentomatoes.com/m/toy_story_4")
data=BeautifulSoup(url.text,"html.parser")
def scrape_movie_details(movieName,moviceurl):
    # rating=data.find_all("li",class_="meta-row clearfix")
    mainDiv=data.find_all("li",class_="meta-row clearfix")
    dict1={}
    for i in mainDiv:
        a=i.text
        b=a.split(":")
        # print(b)
        if "\nRating" in b:
            dict1["Rating"]= b[1].replace("\n","").strip()
        elif "\nGenre" in b:
            dict1["Genre:"]=b[1].replace("\n                        ","").strip()
        elif "\nOriginal Language" in b:
            dict1["language"]=b[1].replace("\n","").strip()
        elif "\nDirector" in b:
            dict1["Director:"]=b[1].replace("\n","").strip()
        elif "\nProducer" in b:
            dict1["Producer"]=b[1].replace("\n                        ","").strip()
    # print(dict1)
    with open("task4.json","w+") as file4:
            json.dump(dict1,file4,indent=4)
            a=json.dumps(dict1)
            print(a)
scrape_movie_details("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")