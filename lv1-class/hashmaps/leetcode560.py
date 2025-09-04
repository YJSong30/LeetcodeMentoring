
'''
LeetCode 560: Subarray Sum Equals K

Problem Statement:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The two subarrays are [1,1] and [1,1].

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: The two subarrays are [1,2] and [3].

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Task:
- Implement a brute-force solution.
- Implement an optimized solution using a hashmap and prefix sums.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Subarray Sum Equals K problem.
    """

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        # TODO: Implement brute-force solution
        pass

    def subarraySum_prefix_sum(self, nums: List[int], k: int) -> int:
        # TODO: Implement the optimized solution using a hashmap and prefix sums.
        pass