class Solution:
    def containsDuplicate(self, nums):
      duplicate_numbers = []
      for number in nums:
        if number in duplicate_numbers:
          return True
        duplicate_numbers.append(number)
      return False
