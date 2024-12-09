# def find_smallest_key(s, test_cases):
#     results = []
#     for a, b in test_cases:
#         m = max(a, b)
#         while True:
#             if m % a == m % b:
#                 results.append(m)
#                 break
#             m += 1
#     return results
# if __name__ == "__main__":
#     s = int(input(""))
#     test_cases = []
#     for _ in range(s):
#         a, b = map(int, input("").split())
#         test_cases.append((a, b))
#     results = find_smallest_key(s, test_cases)
#     print("")
#     for result in results:
#        print(result)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a=int(input(""))
# b=int(input(""))
# s=max(a,b)
# while(True):
#     if(s%a==s%b):
#         break
#     s+=1
# print(s)
def find_smallest_key(s, test_cases):
    results = []
    for a, b in test_cases:
        lcm = max(a, b)
        while True:
            if lcm % a == lcm % b:
                results.append(lcm)
                break
            lcm += 1
    return results
s = int(input(""))
test_cases = []
for _ in range(s):
    a, b = map(int, input("").split())
    test_cases.append((a, b))
results = find_smallest_key(s, test_cases)
print("")
for i in results:
        print(i)