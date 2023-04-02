# Similar to Two Sum
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of 
# numbers that sum to target, false otherwise. This problem is similar to Two Sum.

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

# Let's use the example input. With two pointers, we start by looking at the first and last number. Their sum is 1 + 15 = 16. 
# Because 16 > target, we need to make our current sum smaller. Therefore, we should move the right pointer. Now, we have 1 + 14 = 15. 
# Again, move the right pointer because the sum is too large. Now, 1 + 9 = 10. Since the sum is too small, we need to make it bigger,
# which can be done by moving the left pointer. 2 + 9 = 11 < target, so move it again. Finally, 4 + 9 = 13 = target.

# The reason this algorithm works: because the numbers are sorted, moving the left pointer permanently increases the value the 
# left pointer points to (nums[left] = x). Similarly, moving the right pointer permanently decreases the value the right pointer 
# points to (nums[right] = y). If we have x + y > target, then we can never have a solution with y because x can only increase. 
# So if a solution exists, we can only find it by decreasing y. The same logic can be applied to x if x + y < target.

def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False
