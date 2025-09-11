'''
LeetCode 496: Next Greater Element I

Problem Statement:
The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1
is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2. If there is no next
greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater
element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.

Task:
- Implement a brute-force solution.
- Implement an optimized monotonic stack solution.
- Analyze the time and space complexity of both.
'''

class Solution:
    
    def nextGreaterElement_brute_force(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass
    
    def nextGreaterElement_stack(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass


if __name__ == "__main__":
    solver = Solution()
    
    test_cases = [
        {
            "nums1": [4, 1, 2],
            "nums2": [1, 3, 4, 2],
            "expected": [-1, 3, -1]
        },
        {
            "nums1": [2, 4],
            "nums2": [1, 2, 3, 4],
            "expected": [3, -1]
        },
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected": [7, 7, 7, 7, 7]
        },
        {
            "nums1": [6],
            "nums2": [6, 5, 4, 3, 2, 1],
            "expected": [-1]
        }
    ]
    
    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums1, nums2, expected = case["nums1"], case["nums2"], case["expected"]
        result = solver.nextGreaterElement_brute_force(nums1, nums2)
        status = "✅ Pass" if result == expected else "❌ Fail"
        
        print(f"Test Case {i+1}: {status}")
        print(f'  nums1:    {nums1}')
        print(f'  nums2:    {nums2}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")
    
    print("--- Testing Stack Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums1, nums2, expected = case["nums1"], case["nums2"], case["expected"]
        result = solver.nextGreaterElement_stack(nums1, nums2)
        status = "✅ Pass" if result == expected else "❌ Fail"
        
        print(f"Test Case {i+1}: {status}")
        print(f'  nums1:    {nums1}')
        print(f'  nums2:    {nums2}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")