def solve_game(t, test_cases):
    results = []

    for case in test_cases:
        n, k, arr = case
        found = False

        for i in range(n):
            valid = True
            # Check all other elements as "j"
            for j in range(n):
                if i != j:
                    if abs(arr[i] - arr[j]) % k == 0:
                        valid = False
                        break
            if valid:
                results.append(("YES", i + 1))  # 1-based index
                found = True
                break

        if not found:
            results.append(("NO",))

    return results


# Input handling
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((n, k, arr))

# Solve and print results
results = solve_game(t, test_cases)
for result in results:
    if result[0] == "NO":
        print(result[0])
    else:
        print(result[0])
        print(result[1])
