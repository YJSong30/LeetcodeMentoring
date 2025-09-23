'''
LeetCode 347: Top K Frequent Elements

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: The 2 most frequent elements are 1 and 2.

Example 2:
Input: nums = [1], k = 1
Output: [1]
Explanation: The only element is the most frequent.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Task:
- Implement a brute-force solution.
- Implement an optimized solution using a hashmap and bucket sort or heap.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Top K Frequent Elements problem.
    """

    def topKFrequent_brute_force(self, nums: List[int], k: int) -> List[int]:
        # TODO: Implement brute-force solution
        pass

    def topKFrequent_optimized(self, nums: List[int], k: int) -> List[int]:
        # TODO: Implement the optimized solution using a hashmap and bucket sort or heap.
        pass