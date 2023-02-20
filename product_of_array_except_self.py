# PROBLEM: PRODUCT OF ARRAY EXCEPT SELF
# Given an integer array nums, return an array answer such that answer[i] is equal 
# to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# EXAMPLE: 
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# SOLUTION 1: without restriction
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            result = nums[i] * nums [i+1]
            for each in nums:
                if each != 0:
                    final_number = result / each
                    answer = []
                    answer.append(final_number)
        return answer

# SOLUTION 2: with restriction (no division operator)
class Solution:
    def