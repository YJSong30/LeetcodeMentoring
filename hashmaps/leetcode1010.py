'''
LeetCode 1010: Pairs of Songs With Total Durations Divisible by 60

Problem Statement:
You are given a list of songs where the ith song has a duration of
time[i] seconds.

Return the number of pairs of songs for which their total duration in
seconds is divisible by 60. Formally, we want the number of indices i, j
such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is
divisible by 60.

Constraints:
- 1 <= time.length <= 6 * 10^4
- 1 <= time[i] <= 500

Task:
- Implement a brute-force solution.
- Implement an optimized hashmap-based solution.
- Analyze the time and space complexity of both.

Hint:
- Think about the remainders. If (a + b) % 60 == 0, what does that
  tell you about (a % 60) and (b % 60)?
'''
from typing import List

class Solution:
    """
    Contains solutions for the Pairs of Songs problem.
    """

    def numPairsDivisibleBy60_brute_force(self, time: List[int]) -> int:
        pass

    def numPairsDivisibleBy60_hashmap(self, time: List[int]) -> int:
        pass

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"time": [30, 20, 150, 100, 40], "expected": 3},
        {"time": [60, 60, 60], "expected": 3},
        {"time": [10, 50, 90, 30], "expected": 2},
        {"time": [20, 40, 20, 40, 20], "expected": 6}
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        time, expected = case["time"], case["expected"]
        result = solver.numPairsDivisibleBy60_brute_force(time)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    time = {time}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Hashmap Solution ---")
    print()
    for i, case in enumerate(test_cases):
        time, expected = case["time"], case["expected"]
        result = solver.numPairsDivisibleBy60_hashmap(time)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    time = {time}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")
