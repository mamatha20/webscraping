import requests
import json
from bs4 import BeautifulSoup
file1 = open("task1.json")
movies = json.load(file1)
# print(movies[0]["Year"],)
# print(movies)
def group_by_year():
    emp_dic={}
    for i in movies:
        movie_list=[]
        year=i["Year"]
        if year not in  emp_dic:
            for j in movies:
                if year==j["Year"]:
                    movie_list.append(j)
            emp_dic[year]=movie_list
    with open("task2.json","w+")as file:
        json.dump(emp_dic,file,indent=4)
        a=json.dumps(emp_dic)
group_by_year()