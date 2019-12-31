import unittest
from test.Student import Student as Student
class UnitTest_Student(unittest.TestCase):
    def setUp(self):
        self.score = {
            "语文":90,
            "数学":80,
            "历史":80,
            "地理":70,
            "生物":80
        }
        self.stu = Student("Joy",20,"女",**self.score)
        self.meanscore = sum(self.stu.score.values()) / len(self.stu.score.values())

    def test_name(self):
        self.assertEqual(self.stu.name,"Joy")

    def test_age(self):
        self.assertEqual(self.stu.age, 20)

    def test_sex(self):
        self.assertEqual(self.stu.sex, "女")

    def test_score(self):
        self.assertEqual(self.stu.score,self.score)


    def test_mean(self):
        self.assertEqual(self.meanscore ,(90+80+80+80+70)/5)

    def Down(self):
        del(self.score )
        del(self.stu)
        del(self.meanscore)




