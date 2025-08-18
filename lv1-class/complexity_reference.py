'''
Time and Space Complexity Reference Guide

================================
WHAT IS BIG O NOTATION?
================================
Big O notation describes the worst-case scenario of how an algorithm performs 
as the input size grows. It helps us understand efficiency and scalability.

Key Rule: Drop constants and lower-order terms
- O(2n) → O(n)
- O(n² + n) → O(n²)
- O(3n² + 100n + 42) → O(n²)

================================
COMMON TIME COMPLEXITIES
================================
From fastest to slowest:

O(1) - Constant Time
--------------------
Time doesn't change with input size.
Examples:
- Array access by index: arr[5]
- Hash table lookup: dict[key]
- Basic math operations: x + y
- Variable assignment: x = 5

O(log n) - Logarithmic Time
----------------------------
Time grows slowly as input doubles.
Examples:
- Binary search
- Balanced tree operations
- Finding height of balanced tree

O(n) - Linear Time
------------------
Time grows proportionally with input.
Examples:
- Single loop through array
- Finding max/min in unsorted array
- Linear search
- Counting elements

O(n log n) - Linearithmic Time
-------------------------------
Common in efficient sorting algorithms.
Examples:
- Merge Sort
- Heap Sort
- Quick Sort (average case)
- Sorting-based solutions

O(n²) - Quadratic Time
----------------------
Nested loops over the same data.
Examples:
- Bubble Sort
- Selection Sort
- Nested loops comparing all pairs
- Checking for duplicates (brute force)

O(2ⁿ) - Exponential Time
-------------------------
Doubles with each additional input.
Examples:
- Recursive Fibonacci (naive)
- Generating all subsets
- Recursive solutions without memoization

O(n!) - Factorial Time
-----------------------
Extremely slow, impractical for large n.
Examples:
- Generating all permutations
- Traveling salesman (brute force)

================================
SPACE COMPLEXITY
================================
Memory used by the algorithm.

Important Distinctions:
-----------------------
1. Auxiliary Space: Extra space used by the algorithm (not including input)
2. Total Space: Input space + auxiliary space
3. Usually we care about auxiliary space complexity

What Counts as Space?
---------------------
- Variables (primitives like int, float, bool)
- Data structures (arrays, hash tables, sets, etc.)
- Recursion call stack
- Temporary objects created during execution

What Doesn't Count?
------------------
- The input itself (unless we're modifying/copying it)
- The output (if it's expected/required by the problem)


O(1) - Constant Space
---------------------
Uses fixed amount of extra memory.
Examples:
- Using a few variables
- In-place algorithms
- Two pointers technique

Algorithm Example:
def find_max(nums):
    # Only using a single variable, regardless of input size
    max_val = float('-inf')  # O(1) space
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

O(n) - Linear Space
-------------------
Memory grows with input size.
Examples:
- Creating a hash table of all elements
- Recursion call stack (depth n)
- Storing results in new array

Algorithm Example:
def remove_duplicates(nums):
    # Creating a set that could hold all n elements
    unique = set(nums)  # O(n) space
    return list(unique)  # O(n) space for the new list

O(n²) - Quadratic Space
-----------------------
Examples:
- 2D matrix/grid
- Adjacency matrix for graphs

Algorithm Example:
def create_pascal_triangle(n):
    # Creating an n x n triangle (roughly n²/2 elements)
    triangle = []  # Will grow to O(n²) space
    for i in range(n):
        row = [1] * (i + 1)  # Each row grows
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle  # Total: ~n²/2 elements = O(n²)

================================
ANALYZING LEETCODE PATTERNS
================================
'''

def example_constant_time():
    """O(1) Time, O(1) Space"""
    arr = [1, 2, 3, 4, 5]
    first = arr[0]  # O(1) - direct access
    last = arr[-1]  # O(1) - direct access
    return first + last  # O(1) - simple operation


def example_linear_time(nums):
    """O(n) Time, O(1) Space"""
    max_val = float('-inf')
    for num in nums:  # O(n) - one pass
        max_val = max(max_val, num)  # O(1) operation
    return max_val


def example_quadratic_time(nums):
    """O(n²) Time, O(1) Space - Finding duplicates brute force"""
    n = len(nums)
    for i in range(n):  # O(n)
        for j in range(i + 1, n):  # O(n)
            if nums[i] == nums[j]:
                return True
    return False


def example_linear_space(nums):
    """O(n) Time, O(n) Space - Using hash set"""
    seen = set()  # O(n) space in worst case
    for num in nums:  # O(n) time
        if num in seen:  # O(1) average time
            return True
        seen.add(num)  # O(1) average time
    return False


def example_sorting_solution(nums):
    """O(n log n) Time, O(1) or O(n) Space depending on sort implementation"""
    nums.sort()  # O(n log n) time
    for i in range(1, len(nums)):  # O(n) time
        if nums[i] == nums[i-1]:
            return True
    return False
    # Total: O(n log n) + O(n) = O(n log n)


'''
================================
COMMON LEETCODE COMPLEXITIES
================================

1. Two Sum Problem:
   - Brute Force: O(n²) time, O(1) space
   - Hash Table: O(n) time, O(n) space

2. Valid Anagram:
   - Sorting: O(n log n) time, O(1) space
   - Hash Table: O(n) time, O(1) space (26 letters max)

3. Contains Duplicate:
   - Brute Force: O(n²) time, O(1) space
   - Sorting: O(n log n) time, O(1) space
   - Hash Set: O(n) time, O(n) space

================================
OPTIMIZATION STRATEGIES
================================

1. Trade Space for Time:
   - Use hash tables/sets to avoid nested loops
   - Cache/memoize repeated calculations

2. Sort First:
   - Sometimes O(n log n) sorting enables O(n) solution
   - Useful for two-pointer techniques

3. Mathematical Tricks:
   - Sum formulas, XOR properties
   - Often achieve O(1) space

4. Early Termination:
   - Return as soon as answer is found
   - Doesn't change Big O but improves average case

================================
COMPLEXITY QUIZ
================================
'''

def quiz_1(n):
    """What's the time complexity?"""
    result = 0
    for i in range(n):
        result += i
    return result
    # Answer: O(n) - single loop


def quiz_2(n):
    """What's the time complexity?"""
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result
    # Answer: O(n²) - nested loops


def quiz_3(arr):
    """What's the time complexity?"""
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        print(arr[j])
    # Answer: O(n) + O(n) = O(n) - sequential loops


def quiz_4(sorted_arr, target):
    """What's the time complexity? (Binary Search)"""
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    # Answer: O(log n) - binary search


'''
================================
REMEMBER
================================
1. Always consider both time AND space complexity
2. Different approaches often trade one for the other
3. Best solution depends on constraints:
   - Limited memory? Optimize space
   - Need fast response? Optimize time
   - Small input? Even O(n²) might be fine
4. In interviews, discuss trade-offs between solutions
'''