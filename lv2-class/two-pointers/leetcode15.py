'''
LeetCode 15: 3Sum

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Task:
- Implement a brute-force solution.
- Implement an optimized two-pointer solution.
- Analyze the time and space complexity of both.

'''
from typing import List

class Solution:
    """
    Contains solutions for the 3Sum problem.
    """

    def threeSum_brute_force(self, nums: List[int]) -> List[List[int]]:
        # TODO: Implement brute-force solution
        pass

    def threeSum_two_pointers(self, nums: List[int]) -> List[List[int]]:
        # TODO: Implement two-pointer solution
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [-1, 0, 1, 2, -1, -4], "expected": [[-1, -1, 2], [-1, 0, 1]]},
        {"nums": [0, 1, 1], "expected": []},
        {"nums": [0, 0, 0], "expected": [[0, 0, 0]]},
        {"nums": [-2, 0, 1, 1, 2], "expected": [[-2, 0, 2], [-2, 1, 1]]}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        result = solver.threeSum_brute_force(nums.copy())
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        status = "✅ Pass" if result_sorted == expected_sorted else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, expected = case["nums"], case["expected"]
        result = solver.threeSum_two_pointers(nums.copy())
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        status = "✅ Pass" if result_sorted == expected_sorted else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")