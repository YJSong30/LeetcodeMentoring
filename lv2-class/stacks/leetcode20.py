'''
LeetCode 20: Valid Parentheses

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Task:
- Implement a brute-force solution.
- Implement an optimized stack-based solution.
- Analyze the time and space complexity of both.
'''

class Solution:
    """
    Contains solutions for the Valid Parentheses problem.
    """

    def isValid_brute_force(self, s: str) -> bool:
        """
        Brute force approach: repeatedly remove valid pairs until string is empty or no more pairs can be removed.
        """

    def isValid_stack(self, s: str) -> bool:
        """
        Stack-based approach: use stack to track opening brackets.
        """

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "()", "expected": True},
        {"s": "()[]", "expected": True},
        {"s": "(]", "expected": False},
        {"s": "([)]", "expected": False},
        {"s": "{[]}", "expected": True},
        {"s": "((", "expected": False},
        {"s": "))", "expected": False},
        {"s": "({[]})", "expected": True}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.isValid_brute_force(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Stack Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.isValid_stack(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")