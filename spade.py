rows = int(input("Enter the number of rows: "))
for i in range(rows):
     spaces = " " * (rows - i -1)
     stars = "*" *(2*(i)+1)
     print(spaces + stars)
for j in range(rows):
     sp = " " *(j)
     st = "*" *((rows-j)*2-1)
     print(sp + st)