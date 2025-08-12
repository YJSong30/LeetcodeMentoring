'''
LeetCode 1: Two Sum

Problem Statement:
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Task:
- Implement a brute-force solution.
- Implement an optimized hashmap-based solution.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Two Sum problem.
    Input: nums = [2,7,11,15], target = 9
    Input: nums = [3,2,4], target = 6
    """

    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        # TODO: Implement brute-force solution 
        #   
        # So you want to iterate through the array, by 
        # adding one index with all the other indexes in the array. Using 
        # that sum and comparing it with the target. 
        # 
        #
        # t.c: O(n^2)
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
               if (nums[i] + nums[j] == target):
                  return [i,j]
        return []
    

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        # TODO: Implement hashmap solution
        #  bookshelf = {}
        #  bookshelf["Book 1"] = "Cracking the Coding Interview"
        #  print(bookshelf) -> { "Book 1": "Cracking the Coding Interview"}
        #  bookshelf["Book 2"] = "Harry Potter"
        # print(bookshelf) -> { "Book 1": "Cracking the Coding Interview",
        #                       "Book 2": "Harry Potter"                  }
        # 
        # check if "Book 1" is in my hashmap -> if "Book 1" in bookshelf:
        # 
        # let's add numbers into our hashmap
        # Input: nums = [2,7,11,15], target = 9
        # for index, num in enumerate(nums):
        # 
        # seen = {}
        # 
        # iteration 1: index = 0, num = 2
        #   
        # difference = 7 
        #
        # seen = {2:0}
        # 
        # iteration 2: index = 1, num = 7
        #
        # difference = 9 - 7 = 2
        # if(seen[difference]):
        #   return [seen[difference], index]
        #     
        # seen = {2:0, 7:1 }
        # t.c: O(n)
        # s.p: O(n)
        seen = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference],index]
            seen[num]=index
        return []



if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},
        {"nums": [0, 4, 3, 0], "target": 0, "expected": [0, 3]},
        {"nums": [-3, 4, 3, 90], "target": 0, "expected": [0, 2]}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, target, expected = case["nums"], case["target"], case["expected"]
        result = solver.twoSum_brute_force(nums, target)
        # Check if result contains same indices (order doesn't matter)
        status = "✅ Pass" if sorted(result) == sorted(expected) else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, target = {target}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, target, expected = case["nums"], case["target"], case["expected"]
        result = solver.twoSum_hashmap(nums, target)
        # Check if result contains same indices (order doesn't matter)
        status = "✅ Pass" if sorted(result) == sorted(expected) else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, target = {target}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")