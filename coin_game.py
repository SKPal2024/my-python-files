def min_coins_to_add(t, test_cases):
    results = []
    for case in test_cases:
        n, k = case[0]
        a = case[1]

        current_total = sum(a)

        if current_total >= k:
            results.append(0)
            continue

        # Calculate how many more coins we need
        needed = k - current_total

        # Sort the chests in descending order
        a.sort(reverse=True)

        # Monocarp's greedy approach
        coins_taken = 0
        for coins in a:
            if coins_taken >= k:
                break
            coins_taken += coins

        # If we already have enough coins taken, we don't need to add any more
        if coins_taken >= k:
            results.append(0)
            continue

        # Calculate how much we need to add to reach exactly k
        # We can only take from the sorted chests
        coins_taken = 0
        coins_needed = 0

        for coins in a:
            coins_taken += coins
            if coins_taken >= k:
                break
            coins_needed += coins

        # We need to ensure that coins_taken plus the added coins equals k
        results.append(max(0, k - coins_taken))

    return results


# Example usage
t = 4
test_cases = [
    ((5, 4), [4, 1, 2, 3, 2]),
    ((5, 10), [4, 1, 2, 3, 2]),
    ((2, 10), [1, 1]),
    ((3, 8), [3, 3, 3])
]

results = min_coins_to_add(t, test_cases)
for result in results:
    print(result)