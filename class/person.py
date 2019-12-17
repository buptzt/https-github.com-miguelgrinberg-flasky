# -*- coding:UTF-8 -*-

class MyParentClass:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def printName(self):
        print("<{}>".format(self.name))


class ChildClass(MyParentClass):
    def getParentName(self):
        return self.name
    def printParentName(self):
        print("<{}>".format(self.name))



person1 = ChildClass()
person1.setName("zt")


print(issubclass(ChildClass, MyParentClass))

person1.printName()
person1.printParentName()

