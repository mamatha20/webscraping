import requests
from bs4 import BeautifulSoup
import json
import os
from web1 import moviedata
from web4 import scrape_movie_details
movie = moviedata()
def get_movie_list_details():
    movie_list = []
    for i in movie:
        path="/home/dmamatha/Desktop/web/allfiles.txt"+i["movieName"]+".text"
        if os.path.exists("file.json"):
            pass
        else:
            create=open(i["movieName"]+".text","w")
            url=requests.get(i["moviceurl"])
            create1=create.write(url.text)
            create.close()
            a=scrape_movie_details(i["movieName"],i["moviceurl"])
            movie_list.append(a)
        with open("task5.json","w+") as file5:
            json.dump(movie_list,file5,indent=4)
            print(movie_list)
get_movie_list_details()