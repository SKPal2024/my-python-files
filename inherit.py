class animal:
    alive=True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")
class rabbit(animal):
    def run(self):
        print("rabbit is running")
    def eat(self):
        print("it is eating carrot")
# it will first prioritise function from the child class then perent cla ss
class fish(animal):
    def swim(self):
        print("fish is swimming")
        pass
    def size(self):
        print("this fish is very tiny")
ra=rabbit()
fi=fish()
print(ra.alive)
ra.eat()
print(fi.eat())
print()
print(fi.swim())
fi.size()