'''
LeetCode 268: Missing Number

Problem Statement:
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Task:
- Implement a brute-force solution using a hash set.
- Implement a math-based solution using sum formula.
- Implement a bit manipulation solution using XOR (bonus).
- Analyze the time and space complexity of each.

'''
from typing import List

class Solution:
    """
    Contains solutions for the Missing Number problem.
    """

    def missingNumber_hashset(self, nums: List[int]) -> int:
        # TODO: Implement hashset solution
        pass


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [3, 0, 1], "expected": 2},
        {"nums": [0, 1], "expected": 2},
        {"nums": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
        {"nums": [0], "expected": 1},
        {"nums": [1], "expected": 0},
        {"nums": [1, 2], "expected": 0},
        {"nums": [0, 1, 2, 3, 4, 5, 6, 7, 9], "expected": 8},
        {"nums": list(range(1, 100)), "expected": 0},
        {"nums": [0] + list(range(2, 101)), "expected": 1},
    ]

    print()
    print("--- Testing Hash Set Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        # Show abbreviated version for large arrays
        display_nums = nums if len(nums) <= 10 else f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}]"
        result = solver.missingNumber_hashset(nums)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {display_nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Math Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        display_nums = nums if len(nums) <= 10 else f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}]"
        result = solver.missingNumber_math(nums)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {display_nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing XOR Solution (Bonus) ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        display_nums = nums if len(nums) <= 10 else f"[{nums[0]}, {nums[1]}, ..., {nums[-2]}, {nums[-1]}]"
        result = solver.missingNumber_xor(nums)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {display_nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")