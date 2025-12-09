def print_subsequences(arr):
    # Count how many items are in the list
    n = len(arr)

    # This list will store the current subsequence we are building
    path = []

    # A helper function that tries all possibilities
    def helper(i):
        # If i reaches n, we finished checking all elements
        if i == n:
            # Print the current subsequence (what we collected in path)
            print(path)
            return

        # ----------------------------------
        # CHOICE 1: Do NOT take arr[i]
        # Just move to the next index
        helper(i + 1)

        # ----------------------------------
        # CHOICE 2: Take arr[i]
        # Add this element into our "path" bag
        path.append(arr[i])

        # After taking arr[i], move to the next index
        helper(i + 1)

        # Remove the last added element, so path becomes clean again
        # This is needed to try other possibilities
        path.pop()

    # Start from index 0 (start of the array)
    helper(0)


# Call the function with example input
print_subsequences([1, 2])
