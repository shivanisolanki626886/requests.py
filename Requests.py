# step=1
# import requests
# a=requests.get("http://saral.navgurukul.org/api/courses")
# # print(a)
# import json
# with open(" courses.json","w")as f:
#     x=json.loads(a.text)
#     json.dump(x,f,indent=3)

# step=2
# import requests
# x=requests.get("http://saral.navgurukul.org/api/courses")
# data=x.json()
# def course():
#     i =0
#     for j in data["availableCourses"]:
#         print(i+1,j["name"],j["id"])
#         i+=1
# course()
# course=int(input("enter your course: "))
# select=data["availableCourses"][course-1]["id"]
# var1=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
# data1=var1.json()
# print(data1)




# step=3
import requests
x=requests.get("http://saral.navgurukul.org/api/courses")
dic=x.json()
def course():
    i =0
    for j in dic["availableCourses"]:
        print(i+1,j["name"],j["id"])
        i+=1
    couse=int(input("enter your course: "))
    select=dic["availableCourses"][couse-1]["id"]
    # print(type(select))
    exercise_api=requests.get("http://saral.navgurukul.org/api/courses/"+select+"/exercises")
    print(exercise_api)
    data=exercise_api.json()
    c=1
    slug=[]
    for dic_data in data["data"]:
        print(c,dic_data["slug"])
        slug.append(dic_data["slug"]) 
        c+=1
    slug_input=int(input("enter slug number:"))
    slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+slug[slug_input])
    print(slug_api)
    slug_json=slug_api.json()
    print(slug_input,slug_json["content"])
   
course()