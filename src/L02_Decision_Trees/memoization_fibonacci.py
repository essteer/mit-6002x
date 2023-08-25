# Memoization

# - Memoization is an efficient solution to the problem of exponential complexity for search trees
# - Do not repeat the same calculations
# - Make a memo of them and refer back to them


def fast_fibonacci(n, memo={}):
    """
    Assumes n is an int >= 0, memo used only by recursive calls
    Returns Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fibonacci(n-1, memo) + fast_fibonacci(n-2, memo)
        memo[n] = result
        return result


for i in range(30):
    print(f"fib({i}) = {fast_fibonacci(i)})")


# SLow implementation:
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(30):
    print(f"fib({i}) = {fibonacci(i)})")
