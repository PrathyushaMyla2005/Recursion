'''102030
Count the number of zeros in a given integer using recursion.
For example:   
N = 102030
Output: 3
'''
def count_zeros(n):
    # BASE CASE:
    # When n becomes 0, there are no more digits left to check.
    # So return 0 (no zeros found at this stage).
    if n == 0:
        return 0

    # Extract the last digit of the number.
    last_digit = n % 10

    # Extract the remaining number (removing the last digit).
    remaining = n // 10

    # If the last digit is zero, count it as 1.
    # Otherwise count it as 0.
    zero_count = 1 if last_digit == 0 else 0

    # RECURSIVE CALL:
    # Add the zero count for this digit to the total zero count
    # of the remaining digits.
    return zero_count + count_zeros(remaining)
# Example usage:
N = 102030
result = count_zeros(N)
print(result)  # Output: 3
'''
tc = O(d) where d is the number of digits in N, because we make d recursive calls.
sc = O(d) because of the recursion stack that goes d levels deep.
'''
def count_zeros(n):
    # BASE CASE:
    # If n becomes 0, no digits left → return 0.
    if n == 0:
        return 0

    # RECURSIVE CASE:
    # Check if the last digit is zero (gives 1 or 0)
    # Then add the count of zeros in the remaining digits.
    return (1 if n % 10 == 0 else 0) + count_zeros(n // 10)
# Example usage:
N = 102030
result = count_zeros(N)
print(result)  # Output: 3
'''
tc = O(d) where d is the number of digits in N, because we make d recursive calls.
sc = O(d) because of the recursion stack that goes d levels deep.
'''
