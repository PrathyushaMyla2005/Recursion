'''problem statement
Docstring for Recursion.step6_ Reverse_string_recursion
"Given a string S, reverse the string using recursion."
Meaning:
You must return the reversed string.
S = "hello"
Output: "olleh"
'''
def reverse_string(s):
    # BASE CASE:
    # If the string is empty or has only one character,
    # it is already reversed.
    if len(s) <= 1:
        return s

    # RECURSIVE CASE:
    # Reverse everything except the first character,
    # then add the first character at the end.
    return reverse_string(s[1:]) + s[0]
# Example usage:
S = "hello"
result = reverse_string(S)
print(result)  # Output: "olleh"
'''
tc = O(N) because we make N recursive calls, where N is the length of the string.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
def reverse_string(s):
    # BASE CASE:
    # If the string is empty, return empty string.
    if len(s) == 0:
        return ""
    
    # RECURSIVE CASE:
    # Take last character and add reverse of remaining string.
    return s[-1] + reverse_string(s[:-1])
# Example usage:
S = "hello"
result = reverse_string(S)
print(result)  # Output: "olleh"
'''
tc = O(N) because we make N recursive calls, where N is the length of the string.
sc = O(N) because of the recursion stack that goes N levels deep.
'''
