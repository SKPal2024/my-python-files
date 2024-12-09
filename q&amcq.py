print("q1.-->")
print("A.a   B.b   C.c   D.d")
a=(input("enter your ans of q1 "))
print("q2.-->")
print("A.a   B.b   C.c   D.d")
b=(input("enter your ans of q2 "))
if (a=="B"):
    d=1
else:
    d=0
if (b=="C"):
    e=1
else:
    e=0
print("your marks= ",d+e)
if (d+e==0):
    print("idiot")
print(" correct ans q1->B , q2->C ")