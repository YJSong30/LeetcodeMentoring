'''
LeetCode 349: Intersection of Two Arrays

Problem Statement:
Given two integer arrays, nums1 and nums2, return an array of their
intersection. Each element in the result must be unique, and you can
return the result in any order.

Example 1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]

Example 2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4] (the order does not matter)

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Task:
- Brute force algorithm
- Optimized algorithm
- Give me time and space complexity

Hint:
- Use set data structure
'''

from typing import List

class Solution:
    """
    Contains solutions for finding the intersection of two arrays.
    """
    
    def intersection_brute_force(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    intersection.add(num1)
                    break
                    
        return list(intersection)

        # t.c: o( n * m) n = len(nums1), m = len(nums2)
        # s.c: o(k) where k is the size of intersection list
    
        """
        {2}

        [1, 2, 2, 1]
        [2, 2]
        
        Iter 1 of num1:
        num1 = 1
        num2 = 2

        Iter 2 of num1:
        num1 = 2
        num2 = 2

        Iter 3 of num1:
        num1 = 2
        num2 = 2
        
        Iter 4 of num1:
        num1 = 1
        num2 = 2
        
        """ 

    def intersection_optimized(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
        0) Create result set
        1) Convert nums1 to set ( need for optimization to conduct the lookup in o(1) time )
        2) Loop through nums2 and check if it is in nums1
        3) If it it in the set add to the result list
        4) return list(result)
        
        result = set() 

         
        nums1 = [1, 2, 2, 1], nums2 = [2, 2]
        
        nums1 = {1, 2}
        Iter 1: 
        2 is in nums1 -> True  
        result = { 2 }

        Iter 2:
        2 is in nums1 -> True
        result = { 2 }

        4) 
        return [2]    
        '''

        result = set()
        nums1_set = set(nums1)
        
        for num in nums2: 
            if num in nums1_set:
                result.add(num)
        
        return list(result)
    
if __name__ == "__main__":
    solver = Solution()
    
    test_cases = [
        {"nums1": [1, 2, 2, 1], "nums2": [2, 2], "expected": [2]},
        {"nums1": [4, 9, 5], "nums2": [9, 4, 9, 8, 4], "expected": [4, 9]},
        {"nums1": [1, 2, 3], "nums2": [4, 5, 6], "expected": []}
    ]
    
    print()
    print("--- Testing Brute Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums1, nums2, expected = case["nums1"], case["nums2"], case["expected"]
        result = solver.intersection_brute_force(nums1, nums2)
        status = "✅ Pass" if set(result) == set(expected) else "❌ Fail"
        
        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    nums1 = {nums1}, nums2 = {nums2}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")
    
    print("--- Testing Optimized Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums1, nums2, expected = case["nums1"], case["nums2"], case["expected"]
        result = solver.intersection_optimized(nums1, nums2)
        status = "✅ Pass" if set(result) == set(expected) else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f"  Input:    nums1 = {nums1}, nums2 = {nums2}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")