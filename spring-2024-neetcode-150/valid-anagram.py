# SOLUTION 1: Sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = []
        sorted_t = []

        if len(s) != len(t):
            return False
        
        for letter in s:
            sorted_s.append(letter)

        for letter in t:
            sorted_t.append(letter)

        sorted_s.sort()
        sorted_t.sort()
        if sorted_s == sorted_t:
            return True
        return False
    