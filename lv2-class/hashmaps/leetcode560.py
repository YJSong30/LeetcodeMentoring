'''
LeetCode 560: Subarray Sum Equals K

Problem Statement:
Given an array of integers nums and an integer k, return the total number
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays with sum = 2 are [1,1] and [1,1].

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: The subarrays with sum = 3 are [1,2] and [3].

Example 3:
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: The subarrays with sum = 0 are [1,-1], [-1,0], [0], and [1,-1,0].

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Task:
- Implement a brute-force solution.
- Implement an optimized hashmap-based solution using prefix sums.
- Analyze the time and space complexity of both.

Hint:
- Think about prefix sums. If the sum from index i to j equals k,
what can you say about prefixSum[j] - prefixSum[i-1]?
'''
from typing import List

class Solution:
    """
    Contains solutions for the Subarray Sum Equals K problem.
    """

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        matches = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    matches += 1
        return matches

    """
    [1,2,3]

    current_sum = 0
    i = 1
    j = 1

    Iter 1 (i = 0)
    sum = 1
    sum = 3 (1 match)
    sum = 6

    Iter 2 (i = 1)
    sum = 2
    sum = 5

    Iter 2 (i = 2)
    sum = 3  (1 match)

    Total = 2 matches
    
    """

        

    def subarraySum_hashmap(self, nums: List[int], k: int) -> int:
        seen = { 0: 1 }
        matches = 0
        current_prefix_sum = 0
            
        for num in nums:
            current_prefix_sum += num
            difference = current_prefix_sum - k
            if difference in seen:
                matches += seen[difference]

            seen[current_prefix_sum] = seen.get(current_prefix_sum, 0) + 1

        return matches


'''
current_prefix_sum - previous_prefix_sum = k

1) iterate through array
2) keep track of the current prefix_sum
3) at each step ask "have i seen a previous prefix sum that if i subtract it from my current prefix_sum, gives me k" 
    - current_prefix_sum - previous_prefix_sum = k
    - prevous_prefix_sum = current_prefix_sum - k
    - we were go through array -> complement = target - num -> have we seen this complement is in the hashmap -> two sum
    - hashmap = { previous_prefix_sum : count }


0   1  2  3  4  5    
1, -1, 1, 1, 1, 1

seen = { 0: 1 }


iter 1: 
current_prefix_sum = 1
difference = current_prefix_sum (1) - k (3) = -2
no -> update seen -> { 0:1, 1:1 }

iter 2:
current_prefix_sum = 0
difference = 0 - 3 = -3
have we seen this in our seen hashmap? -> no
update seen -> {0:2, 1:1}

iter 3:
current_prefix_sum = 1
difference = 1 - 3 = -2
is this in our hashmap -> no
update seen -> {0:2, 1:2}

iter 4:
current_prefix_sum = 2
difference = 2 - 3 = -1
in hashmap? -> no
update seen -> {0:2, 1:2, 2:1}

iter 5:
current_prefix_sum = 3
difference = 3 - 3 = 0
is 0 in our hashmap? 
yes -> increment count by seen[0] = 2
update seen -> {0:3, 1:2, 2:1, 3:1}

iter 6:
current_prefix_sum = 4
difference = 4 - 3 = 1
have we seen 1 in our hashmap? -> yes
increment count by seen[1] = 2 -> 2 + 2 = 4
update 4

'''

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},
        {"nums": [1, 2, 3], "k": 3, "expected": 2},
        {"nums": [1, -1, 0], "k": 0, "expected": 3},
        {"nums": [3, 4, 7, 2, -3, 1, 4, 2], "k": 7, "expected": 4},
        {"nums": [1], "k": 0, "expected": 0},
        {"nums": [1], "k": 1, "expected": 1}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraySum_brute_force(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        nums, k, expected = case["nums"], case["k"], case["expected"]
        result = solver.subarraySum_hashmap(nums, k)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    nums = {nums}, k = {k}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")