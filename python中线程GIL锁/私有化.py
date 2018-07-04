class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print("my _work")

    def __away(self):  # 私有方法
        print("my __away")


class Student(Person):
    def introduction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()


class _Bug(object):
    @staticmethod
    def showbug():
        print("showbug")


s1 = Student("李四",20,"跑步")
s1.showperson()
s1._work()
print("*"*20)

# s1.showstudent()
s1.introduction("张三",18,"跳远")
s1.showperson()
s1.showstudent()

Student.testbug()