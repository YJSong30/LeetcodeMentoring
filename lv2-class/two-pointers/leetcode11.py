'''
LeetCode 11: Container With Most Water

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are drawn as [1,8,6,2,5,4,8,3,7]. The max area of
water the container can contain is 49 (between indices 1 and 8, with heights 8 and 7).

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Task:
- Implement a brute force solution (nested loops).
- Implement an optimized two-pointer solution.
- Analyze the time and space complexity of both.

Hint:
- The area is calculated as: min(height[left], height[right]) * (right - left)
- Start with the widest container and move the pointer pointing to the shorter line.
- Why? Moving the taller line inward will never give us more area.
'''

class Solution:
    """
    Contains solutions for the Container With Most Water problem.
    """
    
    def maxArea_brute_force(self, height: list[int]) -> int:
        """
        Brute force solution using nested loops.
        """
        pass
    
    def maxArea_two_pointers(self, height: list[int]) -> int:
        """
        Optimized two-pointer solution.
        """
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"height": [1,8,6,2,5,4,8,3,7], "expected": 49},
        {"height": [1,1], "expected": 1},
        {"height": [4,3,2,1,4], "expected": 16},
        {"height": [1,2,1], "expected": 2},
        {"height": [1,2,4,3], "expected": 4},
        {"height": [2,3,10,5,7,8,9], "expected": 36},
        {"height": [1,3,2,5,25,24,5], "expected": 24}
    ]

    print()
    print("--- Testing Brute Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        height, expected = case["height"], case["expected"]
        result = solver.maxArea_brute_force(height)
        status = " Pass" if result == expected else "L Fail"

        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    height = {height}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        height, expected = case["height"], case["expected"]
        result = solver.maxArea_two_pointers(height)
        status = " Pass" if result == expected else "L Fail"

        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    height = {height}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")