from array import *
v= array('i',[4,6,8,-1,78,12])
print(v)
print(v.buffer_info())
newv=array(v.typecode,(a*a for a in v))
#it gives addres and size
for i in range(len(newv)):
    print(newv[i])