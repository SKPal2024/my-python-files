MOD = 10 ** 9 + 7


# Function to compute the Pisano period for modulo k
def pisano_period(k):
    fib_mod = [0, 1]
    for i in range(2, k * k + 1):  # Pisano period is at most k^2
        fib_mod.append((fib_mod[-1] + fib_mod[-2]) % k)
        if fib_mod[-2] == 0 and fib_mod[-1] == 1:
            return fib_mod[:-2]  # Found the period
    return fib_mod


# Function to find the index of the nth Fibonacci number divisible by k
def find_G_n_k(n, k):
    period = pisano_period(k)
    divisible_indices = [i for i in range(len(period)) if period[i] == 0]

    # If n is larger than the length of divisible indices, calculate modulo
    if len(divisible_indices) == 0 or len(divisible_indices) < n:
        return -1  # Handle case where there aren't enough divisible Fibonacci numbers

    # Return the index of the nth Fibonacci divisible by k
    return divisible_indices[n - 1] % MOD


# Main function to handle input and output
def main():
    t = int(input())  # Number of test cases
    results = []

    for _ in range(t):
        n, k = map(int, input().split())
        result = find_G_n_k(n, k)
        results.append(result)

    # Output all results
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
#for n in[*open(0)][1:]:print('SKaoksuurkaek o'[int(n)%2::2])