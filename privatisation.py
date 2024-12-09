class Person:
    def __init__(self,name):
        self.__na=name

    def namywa(self):
        print("name = ",self.__na)
p1=Person("annonymas")
print(p1.namywa())
print("your name is ",p1.self__na)