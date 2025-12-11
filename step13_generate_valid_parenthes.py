def generate_parentheses_bruteforce(n):
    results = []

    # Step 1: generate all possible strings of '(' and ')'
    def generate(prefix):
        # If prefix length is 2*n, check if valid
        if len(prefix) == 2 * n:
            if is_valid(prefix):
                results.append(prefix)
            return
        
        # Option 1: add '('
        generate(prefix + '(')

        # Option 2: add ')'
        generate(prefix + ')')

    # Step 2: validity check
    def is_valid(s):
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1

            # if at any point closing > opening → invalid
            if balance < 0:
                return False
        
        # at end, must end exactly at balance = 0
        return balance == 0

    generate("")     # start brute-force generation
    return results


# Example:
print(generate_parentheses_bruteforce(3))
