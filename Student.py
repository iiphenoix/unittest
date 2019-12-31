from test.Person import Person as Person
class Student(Person):
    def __init__(self,name,age,sex,**score):
        Person.__init__(self, name, age, sex)
        self.score = score

