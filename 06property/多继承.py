class Parent(object):
    def __init__(self, name):
        print("parent的init开始")
        self.name = name
        print("parent的init结束")


class Son1(Parent):
    def __init__(self, name, age):
        print("son1的init开始")
        self.age = age
        Parent.__init__(self, name)
        print("son1的init结束")


class Son2(Parent):
    def __init__(self, name, gender):
        print("son2的init开始")
        self.gender = gender
        Parent.__init__(self, name)
        print("son2的init结束")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("grandson的init开始")
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print("grandson的init结束")


gs = Grandson("孙子", 12, "男")
print("姓名：", gs.name)
print("年龄", gs.age)
print("性别", gs.gender)
