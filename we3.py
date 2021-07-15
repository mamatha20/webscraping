import  requests
from bs4 import BeautifulSoup
import json
file1 = open("task1.json")
movies = json.load(file1)
# print(movies)
decade_dic={"1937":[],"1947":[],"1957":[],"1967":[],"1977":[],"1987":[],"1997":[],"2007":[],"2017":[],"2027":[]}
def decade_by_year(movies):
    for i in movies:
        # print(i)
        if i["Year"]>=1937 and i["Year"]<=1947:
            decade_dic["1937"].append(i)
        elif i["Year"]>=1947 and i["Year"]<=1957:
            decade_dic["1947"].append(i)
        elif i["Year"]>=1957 and i["Year"]<=1967:
            decade_dic["1957"].append(i)
        elif i["Year"]>=1967 and i["Year"]<=1977:
            decade_dic["1967"].append(i)
        elif i["Year"]>=1977 and i["Year"]<=1987:
            decade_dic["1977"].append(i)
        elif i["Year"]>=1987 and i["Year"]<=1997:
            decade_dic["1987"].append(i)
        elif i["Year"]>=1997 and i["Year"]<=2007:
            decade_dic["1997"].append(i)
        elif i["Year"]>=2007 and i["Year"]<=2017:
            decade_dic["2007"].append(i)
        elif i["Year"]>=2017 and i["Year"]<=2027:
            decade_dic["2017"].append(i)
    with open("task3.json","w+")as file3:
        json.dump(decade_dic,file3,indent=4)
        a=json.dumps(decade_dic)

decade_by_year(movies)
        

