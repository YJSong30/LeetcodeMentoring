'''
LeetCode 1047: Remove All Adjacent Duplicates In String

Problem Statement:
You are given a string s consisting of lowercase English letters. A duplicate
removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can
be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and
equal, and this is the only possible move. The result of this move is that the
string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

'''

class Solution:

    def removeDuplicates_stack(self, s: str) -> str:
        pass


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "abbaca", "expected": "ca"},
        {"s": "azxxzy", "expected": "ay"},
        {"s": "aaa", "expected": "a"},
        {"s": "aaaa", "expected": ""},
        {"s": "abcd", "expected": "abcd"},
        {"s": "aabbcc", "expected": ""},
        {"s": "mississippi", "expected": "mppi"}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.removeDuplicates_brute_force(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   "{result}"")
        print(f"  Expected: "{expected}"\n")

    print("--- Testing Stack Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.removeDuplicates_stack(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   "{result}"")
        print(f"  Expected: "{expected}"\n")