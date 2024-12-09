arr=[11,2,3,4,5,6,7,8,9,0]
arr.sort()
h=len(arr)-1
l=0
h=len(arr)-1
l=0
t=int(input("enter number "))
while(h>=l):
    mid=(h+l)//2
    if (arr[mid]==t):
        print("index: ",mid)
        break
    elif(t>arr[mid]):
        l = mid + 1
    else:
        h=mid-1

