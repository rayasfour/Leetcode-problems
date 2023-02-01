# PROBLEM: GROUP ANAGRAMS
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.

# EXAMPLE
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# SOLUTION 1 (Sorting)
# Time Complexity: nlogn

# SOLUTION 2 (HashMap)
# Time Complexity: O(m*n*26) where 
#                            m is the total number of words in list, 
#                            n is the average length of word, 
#                            question mentions only lower case letters, so 26
# HashMap -> Key: count of letters found in word, Value: strings that have the pattern of count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list) # key: count of letters, value: list of anagrams
        for each_word in strs:
            # Array of 26, 0's
            count = [0] * 26

            # Map a to index 0 and so on
            for each_letter in each_word:
                count[ord(each_letter) - ord("a")] += 1
            
            result[tuple(count)].append(each_word)

        return result.values()

