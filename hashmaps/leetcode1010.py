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

seen = {}
1) initialize hashmap
2) go through time array
3) at each time, get the remainder (time[i] % 60) = r
4) find complement
5) check if complement in hashmap
6) increment count variable
6.5) increment freq
7) return count


'''
from typing import List
from collections import defaultdict

class Solution:
    """
    Contains solutions for the Pairs of Songs problem.
    """

    def numPairsDivisibleBy60_brute_force(self, time: List[int]) -> int:
        count = 0 
        
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        
        return count

    def numPairsDivisibleBy60_hashmap(self, time: List[int]) -> int:
        hash = {}

        '''
        Example: [60, 60, 60]
        {}
        
        Iter 1: 
        (60 - 60) % 60 = 0 % 60 = 0

        time = [40, 40, 20]
        hashmap = { 40: 2}
        complement = (60 - 20) % 60 = 40 o(1)
        count += 2

        remainder = time[i] % 60
        complement = (60 - remainder) % 60

        rem = 60 % 60 = 0
        com = 60 - 0 = 60 vs (60 - 0) % 60 = 0

        {60}
        
        '''
        count = 0
        for i in range(len(time)):
            remainder = time[i] % 60
            complement = (60 - remainder) % 60
            # remainder = time[i] % 60         <- doesnt account for 0 remainder
            # Check if complement exists
            if complement in hash:
                count += hash[complement]     # add current complement count

            hash[remainder] = hash.get(remainder, 0) + 1            # add current element's remainder to the hashmap
            
        return count
        
        '''
        t.c = o(n)
        s.c = o(60) -> o(1)

        t = [40, 40, 20]
        hash = {40 : 2, 20: 1}
        r=20
        c=40
        

        '''
        '''
        count = 0
        seen = {}
        for t in time:
            r = t % 60
            complement = (60 - r) % 60
            if complement in seen:
                count += seen[complement]
            seen[r] = seen.get(r, 0) + 1
        return count
        
        '''

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

'''
 thiss is the weird solution 

 def weird(self,time:Linst[int]) -> int:
    hashm= defaultdict(int)
    count = 0
    for i in time:
        count+=hashm[-i%60]
        hashm[i%60]+=1
    return count ;(
 
'''