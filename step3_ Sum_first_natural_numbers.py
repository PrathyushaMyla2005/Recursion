'''problem statement:
Given a positive integer N, find the sum of the first N natural numbers using recursion."
Natural numbers start from:
1, 2, 3, 4, 5, ...
So you must find:
1 + 2 + 3 + ... + N
N = 5
Output: 15
1 + 2 + 3 + 4 + 5 = 15
'''
def sum_of_n(n):
    # BASE CASE:
    # If n becomes 1, there is only one number to return.
    # This stops recursion.
    if n == 1:
        return 1
    
    # RECURSIVE CASE:
    # Add current number 'n' to the sum of all numbers before it.
    return n + sum_of_n(n - 1)
# Example usage:
N = 5
result = sum_of_n(N)
print(result)  # Output: 15
'''
tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def sum_of_n_formula(n):
    # Use the mathematical formula for the sum of first n natural numbers.
    # This runs in O(1) time and uses O(1) space.
    return n * (n + 1) // 2   # integer division
# Example usage:
N = 5
result = sum_of_n_formula(N)
print(result)  # Output: 15
'''
tc = O(1) because we do a constant amount of work.
sc = O(1) because we use a constant amount of space.
'''


