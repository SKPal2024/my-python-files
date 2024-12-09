while True:
    try:
        x=int(input("enter a number: "))
    except ValueError as e:
        print("your input isn't integer")
    else:
        break
        # else statement is with try not with except
print(f"your number is {x}")