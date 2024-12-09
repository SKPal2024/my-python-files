num = int(input("enter number "))
a = None

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            a = True
            # break out of loop
            break
    if a==True:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")