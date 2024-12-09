class A:
    a="welcome to A sec..."
class B:
    b="welcome to B sec..."
class c(A,B):
    c="welcome to C sec..."
c1=c()
print(c1.a)
print(c1.c)