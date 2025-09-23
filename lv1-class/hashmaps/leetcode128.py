'''
LeetCode 128: Longest Consecutive Sequence

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Task:
- Implement a brute-force solution.
- Implement an optimized solution using a hashmap/set.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Longest Consecutive Sequence problem.
    """

    def longestConsecutive_brute_force(self, nums: List[int]) -> int:
        # TODO: Implement brute-force solution
        pass

    # def longestConsecutive_optimized(self, nums: List[int]) -> int:
    #     # TODO: Implement the optimized solution using a hashmap/set.
    #     pass