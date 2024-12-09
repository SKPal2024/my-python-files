import math


def solve():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Read n and m
        S = list(map(int, input().split()))  # Read the set S

        # Case 1: If there is only one element in the set and n > 1, return -1
        if m == 1 and n > 1:
            print(-1)
            continue

        # Case 2: Greedily construct the lexicographically largest valid array
        # Result array initialized to -1
        result = [-1] * n

        # Try filling the array with the largest element in S first
        used_values = set()

        # Fill the array from left to right with the largest possible values
        for i in range(n):
            placed = False
            for val in reversed(S):  # Try placing values from largest to smallest in S
                if val not in used_values:
                    # Try to place val at position i
                    # We need to check that placing val does not violate the GCD condition
                    valid = True
                    for j in range(i):
                        if math.gcd(i + 1, j + 1) == math.gcd(val, result[j]):
                            valid = False
                            break

                    if valid:
                        result[i] = val
                        used_values.add(val)
                        placed = True
                        break

            if not placed:
                print(-1)
                break
        else:
            print(" ".join(map(str, result)))

