# import random
# choices =[2,3,4,5,6,7,8,9,10,11,12]
# c=random.choice(choices)
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []

    for i in range(1, t + 1):
        s = data[i]

        # If the string length is even, return any two-character substring
        if len(s) % 2 == 0:
            results.append(s[:2])
        else:
            # Find a pair of consecutive distinct characters
            found = False
            for j in range(len(s) - 1):
                if s[j] != s[j + 1]:
                    results.append(s[j:j + 2])
                    found = True
                    break

            # If no such pair is found, return -1
            if not found:
                results.append("-1")

    # Print all results at once
    sys.stdout.write("\n".join(results) + "\n")
