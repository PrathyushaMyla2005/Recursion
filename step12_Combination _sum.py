'''problem statement:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
example:
Input: candidates = [2,3,6,7], target = 7
Output: [[7],[2,2,3]]'''
def combinationSum(nums, target):
    answer = []

    def helper(i, bag, total):
        # If total == target → good answer
        if total == target:
            answer.append(bag.copy())
            return
        
        # If total > target or no numbers left → stop
        if total > target or i == len(nums):
            return
        
        # ---- CHOICE 1: Take nums[i] again ----
        bag.append(nums[i])        # put number in your bag
        helper(i, bag, total + nums[i])   # stay on same number
        bag.pop()                  # remove last number (clean your bag)

        # ---- CHOICE 2: Skip this number ----
        helper(i + 1, bag, total)  # go to next number

    helper(0, [], 0)
    return answer
