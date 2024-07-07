# PROBLEM: TOP K FREQUENT ELEMENTS
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# EXAMPLE
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# SOLUTION 1 (Sorting)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_numbers = sorted(nums)
        repeating_numbers = []

        for i in range(k+1):
            if sorted_numbers[i] == sorted_numbers[i+1]:
                repeating_numbers.append(sorted_numbers[i])

        return repeating_numbers