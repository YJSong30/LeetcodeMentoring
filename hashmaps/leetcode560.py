'''
LeetCode 560: Subarray Sum Equals K

Problem Statement:
Given an array of integers nums and an integer k, return the total number
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays with sum = 2 are [1,1] and [1,1].

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: The subarrays with sum = 3 are [1,2] and [3].

Example 3:
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: The subarrays with sum = 0 are [1,-1], [-1,0], [0], and [1,-1,0].

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Task:
- Implement a brute-force solution.
- Implement an optimized hashmap-based solution using prefix sums.
- Analyze the time and space complexity of both.

Hint:
- Think about prefix sums. If the sum from index i to j equals k,
what can you say about prefixSum[j] - prefixSum[i-1]?
'''
from typing import List

class Solution:
    """
    Contains solutions for the Subarray Sum Equals K problem.
    """

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        pass

    def subarraySum_hashmap(self, nums: List[int], k: int) -> int:
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},
        {"nums": [1, 2, 3], "k": 3, "expected": 2},
        {"nums": [1, -1, 0], "k": 0, "expected": 3},
        {"nums": [3, 4, 7, 2, -3, 1, 4, 2], "k": 7, "expected": 4},
        {"nums": [1], "k": 0, "expected": 0},
        {"nums": [1], "k": 1, "expected": 1}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraySum_brute_force(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraySum_hashmap(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")