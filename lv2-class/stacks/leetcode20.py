'''
LeetCode 20: Valid Parentheses

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]" 
Output: false

Example 5:
Input: s = " { [ ] } "
                 ^
                 p
Output: true
 
|   [    | <--
|   {    |

Iter 0: 

LIFO - last in first out

step 1)
    stack=[]
    hashmap = {
        "}" : "{"        
        "]" : "["
    }

    hashmap.keys()
    hashmap.values()
    
    set = {"apples", "bananas", "cherries"}
    how to check if "cherries" in this set?

    if "cherries" in set: 
    set["cherries"]    

    for char in s:
        if char in hashmap.values():
            stack.append(s)
        elif check if it's a closing
            if stack[-1] == hashmap[char]:
                if stack != empty:
                    stack.pop()

    if stack != empty 
        return False
    else:
        return True
         
            
Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Task:
- Implement a brute-force solution.
- Implement an optimized stack-based solution.
- Analyze the time and space complexity of both.
'''

class Solution:
    """
    Contains solutions for the Valid Parentheses problem.
    """

    def isValid_stack(self, s: str) -> bool:
        stack = []
        hashmap = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        
        for char in s:
            # opening char
            if char in hashmap.values():
                stack.append(char)
            # closing char
            elif char in hashmap.keys():
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            #invalid char
            else:
                return False

        return len(stack) == 0
            
            # if stack.isEmpty():
            #     return True
            # else:
            #     return False
                    
if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"s": "()", "expected": True},
        {"s": "()[]", "expected": True},
        {"s": "(]", "expected": False},
        {"s": "([)]", "expected": False},
        {"s": "{[]}", "expected": True},
        {"s": "((", "expected": False},
        {"s": "))", "expected": False},
        {"s": "({[]})", "expected": True}
    ]

    # print()
    # print("--- Testing Brute-Force Solution ---")
    # print()
    # for i, case in enumerate(test_cases):
    #     s, expected = case["s"], case["expected"]
    #     result = solver.isValid_brute_force(s)
    #     status = "✅ Pass" if result == expected else "❌ Fail"

    #     print(f"Test Case {i+1}: {status}")
    #     print(f'  Input:    s = "{s}"')
    #     print(f"  Output:   {result}")
    #     print(f"  Expected: {expected}\n")

    print("--- Testing Stack Solution ---")
    print()
    for i, case in enumerate(test_cases):
        s, expected = case["s"], case["expected"]
        result = solver.isValid_stack(s)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    s = "{s}"')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")