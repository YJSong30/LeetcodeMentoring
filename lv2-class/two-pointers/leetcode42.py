'''
LeetCode 42: Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Task:
- Implement a brute-force solution.
- Implement an optimized two-pointer solution.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Trapping Rain Water problem.
    """

    def trap_brute_force(self, height: List[int]) -> int:
        pass

    def trap_two_pointers(self, height: List[int]) -> int:
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], "expected": 6},
        {"height": [4, 2, 0, 3, 2, 5], "expected": 9},
        {"height": [2, 0, 2], "expected": 2},
        {"height": [3, 0, 2, 0, 4], "expected": 7}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        height, expected = case["height"], case["expected"]
        result = solver.trap_brute_force(height)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    height = {height}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        height, expected = case["height"], case["expected"]
        result = solver.trap_two_pointers(height)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    height = {height}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")