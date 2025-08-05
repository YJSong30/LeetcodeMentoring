'''
LeetCode 974: Subarray Sums Divisible by K

Problem Statement:
Given an integer array nums and an integer k, return the number of non-empty
subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

Task:
- Implement a brute force solution.
- Implement a hashmap-based solution using prefix sum and modulo.
- Analyze the time and space complexity of both.

4, 5, 0, -2, -3, 1

iter1:
i = 0
j = i = 0
total = 0 + nums[0] = 0 + 4 = 4
if 4 % 5 == 0? no -> no increment count

i = 0
j = 1
total = 4 + 5 = 9
if 9 % 5 == 0? no -> no increment count
...

two loops:
    - i and j will loop through the nums array
    - add up (nums[i] + nums[j]) % k == 0 

-------
hashmaps
prefix_sum

0  1  2   3   4  5
4, 5, 0, -2, -3, 1
4, 9, 9,  7,  4, 5

prefix_sum[4] = 4 % 5 = 4
prefix_sum[1] = 9 % 5 = 4
sum(2,4) = -5 % 5 == 0


to make the prefix_sum[i] = prefix_sum[i-1] + nums[i]

prefix_sum[j] - prefix_[i-1] -> sum of subarray from i to j

hashmap = { remainder: count }

original goal: (sum of subarray from i to j) % k == 0
(p[j] - p[i-1]) % k == 0
(A - B) % K = 0
(A % K) - (B % K) = 0
(A % K) = (B % K)

k = 10
34 % 10 = 4
84 % 10 = 4

84 - 34 = 50 % 10 == 0
'''

from typing import List

class Solution:
    """
    Contains solutions for the Subarray Sums Divisible by K problem.
    """

    def subarraysDivByK_brute_force(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total % k == 0:
                    count += 1
        return count

        '''
        sum = 5
        if 5 % 5 == 0 in our hashmap? -> { 0: 1 }
        count += hashmap[remainder]
        count = count + 1

        0  1  2   3   4  5
        4, 5, 0, -2, -3, 1 (original)
           ^
        4, 9, 9,  7,  4, 5 (prefix sum)


        goal: to find if previous remainder exists using current running sum

        1) Create Map
        2) Intialize Count
        3) Prefix Sum = 0
        4) Loop through array
        - Add Current value to prefix sum
        - Check if remainder already in hashmap
            -> if yes, add freq of remainders to count
        - Add remainder to the map 
        
        for num in nums

        k = 5
        iter 1: 
        - num = 4
        - if 4 % 5 == 4 is this in hashmap? no
        - {0:1, 4:1}

        iter 2:
        - num = 5
        - if 9 % 5 == 4 is this in hashmap? yes
        - count = 0 + 1 = 1
        - found a new, valid subarray that ends at the current position

        '''
    # from collections import defaultdict
    def subarraysDivByK_hashmap(self, nums: List[int], k: int) -> int:
        remainder_freq = {} # remainder: count
        remainder_freq[0] = 1

        count = 0
        current_prefix_sum = 0

        for num in nums:
            current_prefix_sum += num
            remainder = current_prefix_sum % k
            if remainder in remainder_freq:
                count += remainder_freq[remainder]
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
            
        return count

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [4,5,0,-2,-3,1], "k": 5, "expected": 7},
        {"nums": [5], "k": 9, "expected": 0},
        {"nums": [0,0,0], "k": 3, "expected": 6},
        {"nums": [-1,2,9], "k": 2, "expected": 2},
        {"nums": [2,-2,2,-4], "k": 6, "expected": 2},
        {"nums": [7,4,-10], "k": 5, "expected": 1},
        {"nums": [0], "k": 1, "expected": 1}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraysDivByK_brute_force(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraysDivByK_hashmap(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")