'''
LeetCode 167: Two Sum II - Input Array Is Sorted

Problem Statement:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the
same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

Task:
- Implement a two-pointer solution.
- Implement a hashmap solution.
- Analyze the time and space complexity of both.

Hint:
- Since the array is sorted, you can use two pointers from opposite ends.
- Move the left pointer right to increase the sum, right pointer left to decrease it.
'''

class Solution:
    """
    Contains solutions for the Two Sum II problem.
    """
    
    def twoSum_two_pointers(self, numbers: list[int], target: int) -> list[int]:
        """
        Two-pointer approach solution.
        """
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"numbers": [2,7,11,15], "target": 9, "expected": [1,2]},
        {"numbers": [2,3,4], "target": 6, "expected": [1,3]},
        {"numbers": [-1,0], "target": -1, "expected": [1,2]},
        {"numbers": [1,2,3,4,4,9,56,90], "target": 8, "expected": [4,5]},
        {"numbers": [5,25,75], "target": 100, "expected": [2,3]},
        {"numbers": [0,0,3,4], "target": 0, "expected": [1,2]},
        {"numbers": [-3,3,4,90], "target": 0, "expected": [1,2]}
    ]

    print()
    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        numbers, target, expected = case["numbers"], case["target"], case["expected"]
        result = solver.twoSum_two_pointers(numbers, target)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    numbers = {numbers}, target = {target}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        numbers, target, expected = case["numbers"], case["target"], case["expected"]
        result = solver.twoSum_hashmap(numbers, target)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    numbers = {numbers}, target = {target}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")