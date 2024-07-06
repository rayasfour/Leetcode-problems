# SOLUTION 1
# Create an empty list, unique
# Loop through all values in the original list
# If the value doesn't exist in unique[], add it to unique
# If it already exists in unique[], return False
# If all values are unique, and the original list is now empty, return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for number in nums:
            if number not in unique:
                unique.append(number)
        if len(unique) == len(nums):
            return False
        return True

