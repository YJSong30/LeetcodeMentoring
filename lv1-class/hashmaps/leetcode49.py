'''
LeetCode 49: Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for word in strs:
          sorted_word = "".join(sorted(word)) # eat -> ['a', 'e', 't'] -> "aet", tea -> ['a', 'e', 't']
          grouped_anagrams[sorted_word].append(word)
            
        return list(grouped_anagrams.values())

'''
{
"aet" : ["eat", "tea", "ate"]
"ant" : ["tan", "nat"]
"abt" : ["bat"]
}


[["eat", "tea", "ate"]]



sorted() -> a list of the characters in a word sorted -> "eat" -> sorted -> ['a', 'e', 't'] -> "".join() -> "aet"
.sort()
"eat", "ate", "tea" -> somehow compare these to something in order to confirm that these are anagrams

"eat", "ate" -> 
1) same frequency of characters
2) sort them and compare them
"eat" -> "aet"
"aet"
"ate" -> "aet"
"tea" -> "aet"
1) sort the word
2) hashmap
    - key : the sorted word "aet"
    - value : word itself
list(hashmap.values())
'''
        