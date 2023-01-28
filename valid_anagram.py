# PROBLEM: VALID ANAGRAM
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or 
# phrase, typically using all the original letters exactly once.

# EXAMPLE
# Input: s = "anagram", t = "nagaram"
# Output: true

# EXAMPLE
# Input: s = "rat", t = "car"
# Output: false

# SOLUTION 1
class Solution:
    def isAnagram(self, s: str, t: str):
        word=[]

        # Most obvious check: two strings must be same number of letters
        if len(s) != len(t):
            return False

        for each in s:
            word.append(each)
        
        for each_2 in t:
            # If letter is found in word s, remove it from the list
            if each_2 in word:
                word.remove(each_2)
            # If letter is not found in word s, words are not anagrams
            else:
                return False
        
        # If list is empty, all letters were matched up and the two words are anagrams
        if len(word) == 0:
            return True
