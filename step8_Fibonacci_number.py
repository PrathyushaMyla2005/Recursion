'''fibonacci numbers look like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
How are they made?
👉 First number = 0
👉 Second number = 1
👉 Every next number = sum of previous 2 numbers'''
def fib(n):
    # BASE CASES:
    # If n is 0 or 1, return n directly.
    if n == 0 or n == 1:
        return n

    # RECURSIVE CASE:
    # Fibonacci formula: fib(n) = fib(n-1) + fib(n-2)
    return fib(n - 1) + fib(n - 2)
# Example usage:
N = 7
result = fib(N)
print(result)  # Output: 13
'''
tc = O(2^N) because the recursion tree grows exponentially.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def fib_memo(n, memo={}):
    # MEMO CHECK:
    # If we already computed fib(n) earlier and stored it in memo,
    # then directly return that saved value.
    # This avoids recalculating the same Fibonacci number.
    if n in memo:
        return memo[n]

    # BASE CASES:
    # If n is 0 or 1, Fibonacci value is n itself.
    # These stop the recursion.
    if n == 0 or n == 1:
        return n

    # RECURSIVE CASE:
    # Compute Fibonacci using the formula:
    # fib(n) = fib(n-1) + fib(n-2)
    # But now we compute only once and save (memoize) the result.
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    # RETURN SAVED RESULT:
    # Return the stored Fibonacci value for n.
    return memo[n]
# Example usage:
N = 7
result = fib_memo(N)
print(result)  # Output: 13
'''
tc = O(N) because we compute each Fibonacci number from 0 to N only once.
sc = O(N) because of the memo dictionary and the recursion stack that goes N levels deep.
'''
