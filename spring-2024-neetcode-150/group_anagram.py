# SOLUTION 1: Hash map
# Use defaultdict(list) since the values in the dictionary will be a list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dictionary[sorted_word].append(word)
        
        return list(dictionary.values())