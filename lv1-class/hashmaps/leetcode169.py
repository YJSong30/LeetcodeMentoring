'''
LeetCode 169: Majority Element

Problem Statement:
Given an array of integers nums, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
'''
from typing import List

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq_map = Counter(nums)
        target = len(nums) // 2 # majority element
        for num, freq in freq_map.items():
            if freq > target:
                return num