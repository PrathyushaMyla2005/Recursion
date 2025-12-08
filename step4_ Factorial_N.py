'''Given a positive integer N, find the factorial of N using recursion."
Factorial means:
N! = N × (N - 1) × (N - 2) × ... × 2 × 1
The factorial of a number is the product of all positive integers from 1 to N.
For example:
Input: N = 5
Output: 120
Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120
'''
def factorial(n):
    # BASE CASE:
    # When n is 1, factorial is 1.
    # This stops further recursive calls.
    if n == 1:
        return 1
    
    # RECURSIVE CASE:
    # Multiply current number 'n' with factorial of (n-1).
    return n * factorial(n - 1)
# Example usage:
N = 5
result = factorial(N)
print(result)  # Output: 120
'''
tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def factorial(n):
    # BASE CASE:
    # 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1

    # RECURSIVE CASE:
    # n! = n * (n-1)!
    return n * factorial(n - 1)
# Example usage:
N = 5
result = factorial(N)
print(result)  # Output: 120
'''
tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
