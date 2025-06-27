# SOLUTION 1: Additional List
# Create an empty list, unique
# Loop through all values in the original list
# If the value doesn't exist in unique[], add it to unique
# Compare list length of unique[] and original list, if the two list lengths are identical, return False
 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for number in nums:
            if number not in unique:
                unique.append(number)
        if len(unique) == len(nums):
            return False
        return True

# SOLUTION 2: Hash Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
    