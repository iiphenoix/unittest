from test.Person import Person as Person
from test.Student import Student as Student

score = {
    "语文":90,
    "数学":80,
    "历史":80,
    "地理":70,
    "生物":80
}
stu = Student("Joy",20,"女",**score)
meanscore = sum(stu.score.values())/len(stu.score.values())
print(meanscore)