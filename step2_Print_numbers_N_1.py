'''problem statement:
Docstring for Recursion.step2_Print_numbers_N_1
"Given a number N, print all numbers from N to 1 in decreasing order using recursion.
You are NOT allowed to use loops (no for, no while)."
example:
Input: N = 5
Output: 5 4 3 2 1'''
def print_numbers_reverse(n):
    # Base Case:
    # When n becomes 1, only one number is left to print.
    if n == 1:
        print(1)      # print the last number
        return        # stop recursion
    
    # Print current number first (N, N-1, ...)
    print(n)
    
    # Recursive Call:
    # Now print the remaining numbers from n-1 to 1
    print_numbers_reverse(n - 1)
# Example usage:
N = 5
print_numbers_reverse(N)
'''tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def print_numbers_reverse(n):
    # BASE CASE:
    # When n becomes 0, there are no numbers left to print.
    # So we stop recursion here.
    if n == 0:
        return
    
    # Print the current number first (for decreasing order).
    print(n)
    
    # Recursive call:
    # Ask recursion to print the remaining numbers.
    print_numbers_reverse(n - 1)
# Example usage:
N = 5
print_numbers_reverse(N)
'''
tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
