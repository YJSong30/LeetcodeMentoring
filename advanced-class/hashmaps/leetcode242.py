'''
LeetCode 242: Valid Anagram

Problem Statement:
Given two strings, s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters
exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Task:
- Implement a sorting-based solution.
- Implement a hashmap-based solution.
- Analyze the time and space complexity of both.

Hint:
- For the hashmap solution, you can use a dictionary or a fixed-size array
  (since we only have 26 lowercase English letters).
'''

from collections import Counter
class Solution:
    """
    Contains solutions for the Valid Anagram problem.
    Input: s = "anagram", t = "nagaram"

    hints:
    sorted(s) -> ['a','a','a','g','m','n','r']
    "".join(sorted(s)) -> "aaagmnr"

    check if values are same length?  
        return false if not

    sortedS = "".join(sort(s))
    sortedT = "".join(sort(t)) 

    for loop once
        if (sortedS[i] != sortedT[i])
            return false

    return true
    """
    
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # sorted(s) -> ['a','a','a','g','m','n','r'] o(n)
        # "".join = "aaagmnr" o(n)
        # o(n) + o(n) = o(n)

        sortedS = "".join(sorted(s)) # t.c: o(n) + o(n log n) -> o(n log n). s.c: o(n) + o(n) = o(n)
        sortedT = "".join(sorted(t)) # t.c: o(n) + o(n log n) -> o(n log n). s.c: o(n) + o(n) = o(n)

        for i in range(len(s)): # o(n)
            if sortedS[i] != sortedT[i]:
                return False
        
        return True
    
        # t.c = o(n log n)
        # s.c = o(n)


    def isAnagram_hashmap(self, s: str, t: str) -> bool:
        '''
        if len(s) != len(t):
            return False

        hashS = hashmap(s) = {}
        hashT = hashmap(t) = {}

        ['a','a','a','g','m','n','r']
        # in the hashmap, keys = letters, value = frequency of each letter
        # loop through both hashmap and populating both hashmaps
        for i in range(len(s)):
            check if s[i] is in hashS
            if true -> hashS[s[i]] += 1
            if false -> hashS[s[i]] = 1

            check if t[i] is in hashT
            if true -> hashT[t[i]] += 1
            if false -> hashT[t[i]] = 1

        for char in s:
          hashS[char] = hashS.get(char, 0) + 1


        # conditional
        (loop)
            if hashS[i] != hashT[i]
                return False

        return True
        
        '''
        if len(s) != len(t):
            return False

        hashS = dict()
        hashT = dict()

        for char in s:
            hashS[char] = hashS.get(char, 0) + 1
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1

        # s_freq = Counter(s)
        # t_freq = Counter(t)

        for i in hashS:
            # another check
            if i not in hashT:
                return False

            if hashS[i] != hashT[i]:
                return False

        return True

        # t.c: o(n)
        # s.c: o(k) worst case k is all the unique letters in the alphabet -> o(26) -> o(1)

'''
set = {"apples", "bananas", "oranges"}
if "strawberry" not in set:
  return True

hashS = {
  "a": 2,
  "b": 3,
  "c": 1,
}

hashT = {
  "a": 2,
  "b": 3
  "d": 1
}
'''
if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "anagram", "t": "nagaram", "expected": True},
        {"s": "rat", "t": "car", "expected": False},
        {"s": "aacc", "t": "ccac", "expected": False},
        {"s": "listen", "t": "silent", "expected": True},
        {"s": "python", "t": "java", "expected": False},
        {"s": "a", "t": "b", "expected": False},
        {"s": "ab", "t": "a", "expected": False}
    ]

    print()
    print("--- Testing Brute Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, t, expected = case["s"], case["t"], case["expected"]
        result = solver.isAnagram_sorting(s, t)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}", t = "{t}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, t, expected = case["s"], case["t"], case["expected"]
        result = solver.isAnagram_hashmap(s, t)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}", t = "{t}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")