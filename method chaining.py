class car:
    def turn_on(self):
        print("car is started")
        return self
    def drive(self):
        print("I am driving car")
        return self
    def stop(self):
        print("car is stopped")
        return self
c=car()
(c.turn_on().\
 #(\)line continuation chracter
 drive().\
 stop())
c.turn_on().drive()