# import json
# from web1 import moviedata
# from web44 import scrape_movie_details
# movie=moviedata()
# def get_movie_list_details ():
#     movie_list=[]
#     for i in movie:
#         count=1
#         n=scrape_movie_details(i["movieName"],i["moviceurl"])
#         movie_list.append(n)
#         print(count)
#         count+=1
#         # print(n)
#     with open("task5.json","w+") as file5:
#         json.dump(movie_list,file5,indent=4)
# get_movie_list_details()

import json
import requests
from bs4 import BeautifulSoup
from web1 import moviedata
from web44 import scrape_movie_details
movie = moviedata()
def get_movie_list_details():
    movie_list = []
    count=0
    for i in movie[:100]:
        a=scrape_movie_details(i["movieName"],i["moviceurl"])
        movie_list.append(a)
        print(count)
        count+=1
    with open("task5.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()