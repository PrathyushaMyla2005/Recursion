'''Given an integer N, find the sum of all its digits using recursion."
You must break the number digit-by-digit and add them.
N = 456
4 + 5 + 6 = 15
'''
def sum_of_digits(n):
    # BASE CASE:
    # When n becomes 0, there are no digits left to add.
    if n == 0:
        return 0
    
    # RECURSIVE CASE:
    # Extract last digit and add it to the sum of remaining digits.
    last_digit = n % 10          # last digit
    remaining = n // 10          # number without last digit
    
    return last_digit + sum_of_digits(remaining)
# Example usage:
N = 456
result = sum_of_digits(N)
print(result)  # Output: 15
'''
tc = O(d) where d is the number of digits in N, because we make d recursive calls.
sc = O(d) because of the recursion stack that goes d levels deep.
'''
def sum_of_digits(n):
    # BASE CASE:
    # When n reaches 0, there are no more digits left to add.
    if n == 0:
        return 0

    # RECURSIVE CASE:
    # Add the last digit to the sum of the remaining digits.
    return (n % 10) + sum_of_digits(n // 10)
# Example usage:
N = 456
result = sum_of_digits(N)
print(result)  # Output: 15
'''
tc = O(d) where d is the number of digits in N, because we make d recursive calls.
sc = O(d) because of the recursion stack that goes d levels deep.
'''
