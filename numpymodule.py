import numpy as np

list1 = [10, 20, 30, 40, 50]
list2 = [11, 12, 13, 14, 15]

vtr1 = np.array(list1)

vtr2 = np.array(list2)

print("We create vector from a list 1:")
print(vtr1)
print("We create vector from a list 2:")
print(vtr2)

vctr_add = vctr1 + vctr2
print("Addition of two vectors: ", vtr_add)