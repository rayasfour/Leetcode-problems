# PROBLEM
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# EXAMPLE
# Input: nums = [1,2,3,1]
# Output: true

# SOLUTION 1 (Using set)
# Runtime 50ms
# Time Complexity O(n^2) 
# Space Complexity O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]):
        unique_list = []
        for number in nums:
            if number not in unique_list:
                unique_list.append(number)
        
        if len(unique_list) == len(nums):
            return False
        
        return True

# SOLUTION 2 (Using set)
# Runtime 40ms 
# Time complexity O(n^2)
# Space Complexity O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]):
        unique_list = []
        for number in nums:
            if number not in unique_list:
                unique_list.append(number)
        
        return len(unique_list) != len(nums)

# SOLUTION 3 (Using sort)
# Runtime 34ms
# Time Complexity nlog(n)
# Space Complexity O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]):
        nums.sort()
        for i in range(len(nums)):
            if len(nums) == 1:
                return False
            return nums[i] == nums[i+1]
