try:
    a=int(input("enter numarator "))
    b=int(input("nter denominator "))
    print("ans= ",a/b)
except ZeroDivisionError as e:
    print(e)
    print("can't devide by 0")
except ValueError as e:
    print(e)
    print("enter numbers only")
except :
    print("error")