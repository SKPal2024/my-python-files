class Student:
    def __init__(asdf,sec,roll,name,school):
        asdf.qwert=sec
        asdf.r=roll
        asdf.n=name
        asdf.s="THS"
        print("Adding new data...")
    def welcome(self):
        print("welcome student")
s1=Student("A",1,"Surya","tyi")
print(s1.welcome(),"name= ",s1.n, ", sec=",s1.qwert,", roll=",s1.r,", school=",s1.s)
del s1.r
print(s1.r)