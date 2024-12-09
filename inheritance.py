class Car:
    good=True
    @staticmethod
    def start(self):
        print("start the car...")

    @staticmethod
    def stop(self):
        print("car is stopped...")


class Toyotacar(Car):
    pass
#    def __init__(self, name):
#        self.name = name

#    c1 = Toyotacar("fortuner")
#    c2 = Toyotacar("qwert")
   # print(c1.na)
#    print(c1.start())
class Fordcar(Car):
    pass
toyota=Toyotacar()
ford=Fordcar()
print(toyota.good)
ford.stop()