'''
LeetCode 974: Subarray Sums Divisible by K

Problem Statement:
Given an integer array nums and an integer k, return the number of non-empty
subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

Task:
- Implement a brute force solution.
- Implement a hashmap-based solution using prefix sum and modulo.
- Analyze the time and space complexity of both.

Hint:
- For the hashmap solution, use the fact that if two prefix sums have the same
  remainder when divided by k, their difference is divisible by k.
- Handle negative remainders by adding k to make them positive.
'''
from typing import List

class Solution:
    """
    Contains solutions for the Subarray Sums Divisible by K problem.
    """

    def subarraysDivByK_brute_force(self, nums: List[int], k: int) -> int:
        pass

    def subarraysDivByK_hashmap(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [4,5,0,-2,-3,1], "k": 5, "expected": 7},
        {"nums": [5], "k": 9, "expected": 0},
        {"nums": [0,0,0], "k": 3, "expected": 6},
        {"nums": [-1,2,9], "k": 2, "expected": 2},
        {"nums": [2,-2,2,-4], "k": 6, "expected": 2},
        {"nums": [7,4,-10], "k": 5, "expected": 1},
        {"nums": [0], "k": 1, "expected": 1}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraysDivByK_brute_force(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraysDivByK_hashmap(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")