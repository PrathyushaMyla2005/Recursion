'''x × x × x × ... × x   (n times)
2⁵ = 2 × 2 × 2 × 2 × 2 = 32  
3⁴ = 3 × 3 × 3 × 3 = 81  
5² = 5 × 5 = 25  
7⁰ = 1  (anything power 0 is 1)
Given two integers x and n, calculate x raised to the power n (x^n) using recursion.
'''
def power_bruteforce(x, n):
    # BASE CASE:
    # If exponent n is 0, x^0 is always 1 (by definition).
    # This condition stops further recursive calls.
    if n == 0:
        return 1

    # RECURSIVE CASE:
    # Using the simple mathematical identity:
    #   x^n = x * x^(n-1)
    # We compute x^(n-1) by calling the same function recursively,
    # then multiply the result by x to get x^n.
    return x * power_bruteforce(x, n - 1)
# Example usage:
X = 2
N = 5
result = power_bruteforce(X, N)
print(result)  # Output: 32
'''
tc = O(n) because we make n recursive calls.
sc = O(n) because of the recursion stack that goes n levels deep.
'''
def power_optimal(x, n):
    # BASE CASE:
    # When n becomes 0, return 1 because x^0 = 1 by definition.
    if n == 0:
        return 1

    # RECURSIVE CASE:
    # Compute power for half exponent.
    half = power_optimal(x, n // 2)

    # If exponent n is even:
    # x^n = (x^(n/2))^2
    if n % 2 == 0:
        return half * half
    
    # If exponent n is odd:
    # x^n = x * (x^((n-1)/2))^2
    else:
        return x * half * half
# Example usage:
X = 2
N = 5
result = power_optimal(X, N)
print(result)  # Output: 32
'''
tc = O(log n) because we halve the exponent in each recursive call.
sc = O(log n) because of the recursion stack that goes log n levels deep.
'''
