import json
with open("task5.json","r") as file:
    data=json.load(file)
    # print(data)
def analyse_movies_directors(data):
    director_dict={}
    i=0
    while i<len(data):
        index=0
        count=0
        while index<len(data):
            if data[i]["director"]==data[index]["director"]:
                count+=1
                director=str(data[i]["director"])[0:]
                director_dict[director]=count
            index+=1    
        i+=1
    with open("task7.json","w+") as director_data:
        json.dump(director_dict,director_data,indent=4)
    print(director_dict)
analyse_movies_directors(data)