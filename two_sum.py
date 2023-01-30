# PROBLEM: TWO SUM
# Given an array of integers nums and an integer target, return indices of the two 
# numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# EXAMPLE
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# SOLUTION 1 (not entirely correct)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]

# SOLUTION 2 (HashMap)
# Time Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oldMap = {}
        for i, n in enumerate(nums):
            leftover = target - n
            if leftover in oldMap:
                return [i, oldMap[leftover]]
            oldMap[n] = i
