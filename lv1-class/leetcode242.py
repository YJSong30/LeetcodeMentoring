'''
LeetCode 242: Valid Anagram

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and return false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Explanation: "nagaram" is an anagram of "anagram".

Example 2:
Input: s = "rat", t = "car"
Output: false
Explanation: "car" is not an anagram of "rat".

Example 3:
Input: s = "listen", t = "silent"
Output: true
Explanation: "silent" is an anagram of "listen".

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Task:
- Implement a brute-force (sorting) solution.
- Implement an optimized hashmap-based solution.
- Analyze the time and space complexity of each.

'''

class Solution:
    """
    Contains solutions for the Valid Anagram problem.
    """

    def isAnagram_sorting(self, s: str, t: str) -> bool:
        # TODO: Implement sorting solution
        pass

    def isAnagram_hashmap(self, s: str, t: str) -> bool:
        # TODO: Implement hashmap solution
        pass


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "anagram", "t": "nagaram", "expected": True},
        {"s": "rat", "t": "car", "expected": False},
        {"s": "listen", "t": "silent", "expected": True},
        {"s": "a", "t": "ab", "expected": False},
        {"s": "aa", "t": "aa", "expected": True},
        {"s": "ac", "t": "bb", "expected": False},
        {"s": "aacc", "t": "ccac", "expected": False},
        {"s": "abc", "t": "bca", "expected": True},
        {"s": "abcdefghijklmnopqrstuvwxyz", "t": "zyxwvutsrqponmlkjihgfedcba", "expected": True},
    ]

    print()
    print("--- Testing Sorting Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, t, expected = case["s"], case["t"], case["expected"]
        # Show abbreviated version for long strings
        display_s = s if len(s) <= 10 else f'"{s[:4]}...{s[-4:]}"'
        display_t = t if len(t) <= 10 else f'"{t[:4]}...{t[-4:]}"'
        result = solver.isAnagram_sorting(s, t)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{display_s}", t = "{display_t}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, t, expected = case["s"], case["t"], case["expected"]
        display_s = s if len(s) <= 10 else f'"{s[:4]}...{s[-4:]}"'
        display_t = t if len(t) <= 10 else f'"{t[:4]}...{t[-4:]}"'
        result = solver.isAnagram_hashmap(s, t)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{display_s}", t = "{display_t}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")