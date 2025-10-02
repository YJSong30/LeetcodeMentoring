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

    def longestConsecutive_optimized(self, nums: List[int]) -> int:
        # TODO: Implement the optimized solution using a hashmap/set.
        pass

'''      0  1  2  3 4 5
nums = [100,4,200,1,3,2] -> [1,2,3,4,100,200]
                             ^
                             i = 1
                             count = 3
                             max_length = max(max_length, count) -> max_length = 4


for i in range(len(nums)) -> i starts at 0 and goes up to 5
o(n log n) -> o(n)
n = len(nums)

dict = { key: value }

set = { key }

nums_set = {100, 4, 200, 1, 3, 2, 99, 98}
if 3 in nums_set

1) i want to check for consecutive numbers
2) i want to initialize a variable called max_length to track longest consecutive sequence
3) i want to initialize a variable called length to track the current length of consecutive sequence


for num in nums_set:
    if num - 1 not in nums_set: # good starting point
        current_num = num
        length = 1

        while current_num + 1 in nums_set: # o(1)
            length += 1
            current_num += 1
        
        max_length = max(max_length, length)

return max_length

        







    



'''