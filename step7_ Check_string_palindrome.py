'''problem statement:
Docstring for Recursion.step2_Print_numbers_N_1
"Given a string S, check if the string is a palindrome using recursion."
Meaning:
A palindrome is a string that reads the same forwards and backwards.
You must return True if S is a palindrome, otherwise return False.
S = "racecar"
Output: True
S = "hello"
Output: False'''
def is_palindrome(s):
    # BASE CASE:
    # If string is empty or has one character, 
    # it is already a palindrome.
    if len(s) <= 1:
        return True

    # If first and last characters don't match,
    # it's not a palindrome.
    if s[0] != s[-1]:
        return False

    # RECURSIVE CASE:
    # Remove first and last characters,
    # and check the inner substring.
    return is_palindrome(s[1:-1])
# Example usage:
S = "racecar"
result = is_palindrome(S)
print(result)  # Output: True
'''
tc = O(N) because we make N/2 recursive calls, where N is the length of the string.
sc = O(N) because of the recursion stack that goes N/2 levels deep.
'''
def is_palindrome_optimal(s, left, right):
    # BASE CASE:
    # If left crosses right, we checked all characters
    if left >= right:
        return True

    # If mismatch occurs, it's not a palindrome
    if s[left] != s[right]:
        return False

    # RECURSIVE CASE:
    # Move inward: left+1, right-1
    return is_palindrome_optimal(s, left + 1, right - 1)
# Example usage:
S = "racecar"
result = is_palindrome_optimal(S, 0, len(S) - 1)
print(result)  # Output: True
'''
tc = O(N) because we make N/2 recursive calls, where N is the length of the string.
sc = O(N) because of the recursion stack that goes N/2 levels deep.
'''
