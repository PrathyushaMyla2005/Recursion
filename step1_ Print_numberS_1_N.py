'''
Docstring for Recursion.step1_ Print_numberS_1_N
"Given a number N, print all numbers from 1 to N in increasing order using recursion.
You are NOT allowed to use loops (no for, no while)."

Meaning:
You must print → 1, 2, 3, 4, ... N
But using recursion only.
example:
Input: N = 5
Output: 1 2 3 4 5
'''
def print_numbers(n):
    # BASE CASE:
    # If n is 1, we print 1 because this is the smallest number.
    # This condition stops further recursive calls.
    if n == 1:
        print(1)        # Print the first number in the sequence.
        return          # End the current function call and go back.

    # RECURSIVE CALL:
    # Before printing n, we first print all numbers from 1 to n-1.
    # This breaks the problem into a smaller version of itself.
    print_numbers(n - 1)

    # AFTER RECURSION:
    # Once all smaller numbers (1 to n-1) are printed,
    # we print the current number n.
    # This ensures the numbers appear in increasing order.
    print(n)
# Example usage:
N = 5
print_numbers(N)
'''tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def print_numbers(n):
    # BASE CASE:
    # When n becomes 0, there are no numbers left to print.
    # So simply stop the recursion. This is the cleanest stopping condition.
    if n == 0:
        return          # End the current recursive call.

    # RECURSIVE CALL:
    # First solve the smaller problem: print numbers from 1 to n-1.
    # This ensures that smaller numbers get printed first.
    print_numbers(n - 1)

    # AFTER THE RECURSIVE CALL:
    # Now print the current number 'n'.
    # This prints numbers in increasing order as the stack unwinds.
    print(n)
# Example usage:
N = 5
print_numbers(N)
'''
tc = O(N) because we make N recursive calls.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
