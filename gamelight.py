def solve(test_cases):
    results = []
    for n, switches in test_cases:
        count_on = sum(switches)
        min_lights_on = 1 if count_on % 2 != 0 else 0
        if (sum(switches)!=2*n):
            max_lights_on=count_on
        else:
            max_lights_on = 0
        results.append((min_lights_on, max_lights_on))
    return results
a = int(input())
test_cases = []
for _ in range(a):
    n=int(input())
    switches = list(map(int, input().split()))
    test_cases.append((n, switches))
results = solve(test_cases)
for result in results:
    print(result[0], result[1])
