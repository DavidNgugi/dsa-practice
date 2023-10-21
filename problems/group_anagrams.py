from collections import defaultdict
from typing import List

# https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Time -> O(N)
    Space -> O(N) 
    """
    # for each string in list of strings, make key from sorted string and add to hashtable
    # add anagram to hashtable of each sorted word

    if len(strs) < 2:
        return [strs]
    
    anagrams = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)

    return anagrams.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    output = [["bat"],["nat","tan"],["ate","eat","tea"]]

    print(groupAnagrams(strs))