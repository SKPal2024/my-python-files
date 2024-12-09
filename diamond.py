rows = int(input("Enter the number of rows: "))
for i in range(rows):
     spaces = " " *2* (rows - i -1)
     stars = "*" *2*(2 * (i+1) + 1)
     if len(stars)<3:
         continue
     else:
         print(spaces + stars)
r=2*(rows+1)+1
for i in range(r):
    sp1 = " " * (i)
    st1 = "*" * (2 * (r-i-1))
    print(sp1 + st1)


