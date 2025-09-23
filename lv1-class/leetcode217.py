'''
LeetCode 217: Contains Duplicate

Problem Statement:
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The value 1 appears twice in the array.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Explanation: Multiple values appear more than once.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Task:
- Implement a brute-force solution.
- Implement an optimized hashset-based solution.
- Analyze the time and space complexity of each.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Contains Duplicate problem.
    """

    def containsDuplicate_brute_force(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate_hashset(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
# nums = [1,2,3,1] -> {1, 2, 3} -> {1, 2}

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [1, 2, 3, 1], "expected": True},
        {"nums": [1, 2, 3, 4], "expected": False},
        {"nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True},
        {"nums": [1], "expected": False},
        {"nums": [1, 2], "expected": False},
        {"nums": [1, 1], "expected": True},
        {"nums": [-1, -1, -2, -3], "expected": True},
        {"nums": [0, 4, 3, 0], "expected": True},
        {"nums": list(range(10000)), "expected": False},
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        # Show abbreviated version for large arrays
        display_nums = nums if len(nums) <= 10 else f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}]"
        result = solver.containsDuplicate_brute_force(nums)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {display_nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashset Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        display_nums = nums if len(nums) <= 10 else f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}]"
        result = solver.containsDuplicate_hashset(nums)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {display_nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")