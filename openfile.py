for i in range(3):
    n=input("enter name: ")
    file = open("names.txt", "a")
    file.write("\nhello " + n)

file.close()