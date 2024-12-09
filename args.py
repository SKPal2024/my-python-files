def calsum(* qwert):# * argument by this method I can add multiple numbers
    a=0
    for i in qwert:
        a+=i
    return a
print(calsum(2,89,4))

def name1(** kwargs):
    for keys,values in kwargs.items():
        print(values,end="        ")
print(name1(z="hello ",a="Surya ",b="Kanta ",c="Pal",end="               "))