'''
LeetCode 75: Sort Colors

Problem Statement:
Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant
extra space?

'''
from typing import List

class Solution:
    """
    Contains solutions for the Sort Colors problem.
    """

    def sortColors_brute_force(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

    def sortColors_two_pointers(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [2, 0, 2, 1, 1, 0], "expected": [0, 0, 1, 1, 2, 2]},
        {"nums": [2, 0, 1], "expected": [0, 1, 2]},
        {"nums": [0], "expected": [0]},
        {"nums": [1, 2, 0, 0, 1, 2], "expected": [0, 0, 1, 1, 2, 2]}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums = case["nums"].copy()
        expected = case["expected"]
        solver.sortColors_brute_force(nums)
        status = "✅ Pass" if nums == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {case["nums"]}')
        print(f"  Output:   {nums}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums = case["nums"].copy()
        expected = case["expected"]
        solver.sortColors_two_pointers(nums)
        status = "✅ Pass" if nums == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {case["nums"]}')
        print(f"  Output:   {nums}")
        print(f"  Expected: {expected}\n")