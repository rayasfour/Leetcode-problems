# PROBLEM: CONTAINS DUPLICATE
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# EXAMPLE
# Input: nums = [1,2,3,1]
# Output: true

# SOLUTION 1 (Using sort)
# Runtime 61ms
# Time Complexity nlog(n)
# Space Complexity O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]):
        nums.sort()
        for i in range(len(nums)):
            if len(nums) == 1:
                return False
            return nums[i] == nums[i+1]

# SOLUTION 2 (Using additional list)
# Runtime 40ms 
# Time Complexity O(n)
# Space Complexity O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]):
        unique_list = []
        for number in nums:
            if number not in unique_list:
                unique_list.append(number)
        
        return len(unique_list) != len(nums)

# SOLUTION 3 (Using HashSet)
# Runtime 40ms
# Time Complexity O(n) 
# Space Complexity O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
