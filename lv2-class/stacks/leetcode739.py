'''
LeetCode 739: Daily Temperatures

Problem Statement:
Given a list of daily temperatures, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each
temperature will be an integer in the range [30, 100].

Task:
- Implement a brute-force solution.
- Implement an optimized stack-based solution.
- Analyze the time and space complexity of both.
'''

'''
[73, 74, 75, 71, 69, 72, 76, 73]
 ^    ^

current = 0
hotIter = 1
hotter = []

 iter 1:
    current -> 73 [0]
    hotIter -> 74 [1]
    74 > 73 -> difference = hotIter - current = 1
    
    add the difference to array:
    hotter = [1]

iter 2:
    current -> 74 [1]
    hotIter -> 75 [2]
    75 > 74 -> difference = hotIter - current = 1
    
    add the difference to array:
    hotter = [1, 1]

iter 3:
    current -> 75 [2]
    hotIter -> 71 [3]
    75 < 71 -> hotIter go to next index

    current -> 75 [2]
    hotIter -> 69 [4]
    75 < 69 -> hotIter go to next index

    current -> 75 [2]
    hotIter -> 72 [5]
    75 < 72 -> hotIter go to next index

    current -> 75 [2]
    hotIter -> 76 [6]
    75 > 76 -> difference = hotIter - current = 4
    
    add the difference to array:
    hotter = [1, 1, 4]

iter 4:
    current -> 71 [3]
    hotIter -> 69 [4]
    71 < 71 -> hotIter go to next index

[30,40,50,60]

iter 1:
    i = 30
    j = 40

iter 2:
    i = 40
    j = 50

iter 3: 
    i = 50
    j = 60 [4, last index]

iter 4: 
    i = 60

    return [1, 1, 1, 0]

Wrong: [1,1,0,0]
'''
class Solution:

    def dailyTemperatures_brute_force(self, temperatures: list[int]) -> list[int]:
        hotter = []

        for i in range(len(temperatures)):

            if i == len(temperatures) - 1:
                hotter.append(0)

            for j in range(i+1, len(temperatures)):

                if temperatures[i] < temperatures[j]:
                    hotter.append(j-i)
                    break
                
                # if j is last element
                if j == len(temperatures) - 1:
                    hotter.append(0)
                    
            # else:
            #     hotter.append(0)

        return hotter        

    def dailyTemperatures_stack(self, temperatures: list[int]) -> list[int]:
        
        days = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)): # o(n)
            
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                days[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return days

        """
        0 -> 73
        1 -> 74
        2 -> 75
        3 -> 71
        4 -> 69
        5 -> 72
        6 -> 76
        7 -> 73

        [6, 7]

        days = [1, 1, 4, 2, 1, 1, 0, 0]

        i = 1
        """


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {
            "temperatures": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0]
        },
        {
            "temperatures": [89, 62, 70, 58, 47, 47, 46, 76, 100, 70],
            "expected": [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        },
        {
            "temperatures": [55, 38, 53, 81, 61, 93, 97, 32, 43, 78],
            "expected": [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
        }
    ]

    print()
    print("--- Testing Brute-Force Solution ---")
    print()
    for i, case in enumerate(test_cases):
        temperatures, expected = case["temperatures"], case["expected"]
        result = solver.dailyTemperatures_brute_force(temperatures)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    temperatures = {temperatures}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing Stack Solution ---")
    print()
    for i, case in enumerate(test_cases):
        temperatures, expected = case["temperatures"], case["expected"]
        result = solver.dailyTemperatures_stack(temperatures)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    temperatures = {temperatures}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")
