def low(text):
    return text.lower()
def up(text):
    return text.upper()
def hello(f):
    text=f("qwert" )
    print(text)
hello(low)
hello(up)
print("------------------------")
def devisor(x):
    def devidend(a):
        print(a/x)
    return devidend
devide = devisor(5)
devide(100)