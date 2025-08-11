'''
LeetCode 125: Valid Palindrome

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Task:
- Implement a two-pointer solution.
- Analyze the time and space complexity of both.

1) clean the input string into just letters and numbers
2) convert all uppercase letters to lowercase
3) initialize two pointers: left and right
4) while loop l <= r
5) check if string[l] != string[r]
5.5) return false

6) if it is then, continue -> increment l by 1 and decrement r by 1
7) break out of loop
8) return true

'''

class Solution:
    """
    Contains solutions for the Valid Palindrome problem.
    """
    
    def isPalindrome_two_pointers(self, s: str) -> bool:
        """
        Two-pointer approach solution.
        letter.isalnum() A-Z, a-z, 0-9 -> return True
        letter.lower()

        A man, a plan, a canal
        ["a", "m", "a", "n", "a"... "l"]
        """
        cleanedArray = []
        for char in s:
            if char.isalnum():
                cleanedArray.append(char.lower()) # "race" + "c" = "racec". this is o(n^2)
            else: 
                continue

        cleanedStr = "".join(cleanedArray)

        left = 0
        right = len(cleanedStr) - 1

        while left <= right:
            if cleanedStr[left] != cleanedStr[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

        # res = ["a", "c", "b"]
        # "".join(res) -> "acb"

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "A man, a plan, a canal: Panama", "expected": True},
        {"s": "race a car", "expected": False},
        {"s": " ", "expected": True},
        {"s": "ab_a", "expected": True},
        {"s": "0P", "expected": False},
        {"s": "a", "expected": True},
        {"s": ".,", "expected": True}
    ]

    print()
    print("--- Testing Two-Pointer Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.isPalindrome_two_pointers(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")
