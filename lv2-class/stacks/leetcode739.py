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

class Solution:

    def dailyTemperatures_brute_force(self, temperatures: list[int]) -> list[int]:
        pass

    def dailyTemperatures_stack(self, temperatures: list[int]) -> list[int]:
        pass


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
