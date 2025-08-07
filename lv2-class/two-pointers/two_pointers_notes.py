"""
TWO POINTERS TECHNIQUE - CLASS NOTES
====================================

The Two Pointers technique is a pattern where we use two pointers to iterate through 
data structures (usually arrays or strings) to solve problems efficiently.

KEY CONCEPTS:
------------
1. Two pointers can move in the same direction or opposite directions
2. Often reduces time complexity from O(n^2) to O(n)
3. Usually requires sorted data or specific patterns
4. Common in array/string manipulation problems

COMMON PATTERNS:
---------------
"""

# PATTERN 1: OPPOSITE DIRECTION (Meeting in the Middle)
# =====================================================
# Start from both ends and move towards center
# Use cases: Palindromes, reversing, two-sum in sorted array

def is_palindrome_simple(s: str) -> bool:
    """
    Check if string is palindrome using two pointers from opposite ends.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target in a SORTED array.
    Time: O(n), Space: O(1)
    
    Example: nums = [2, 7, 11, 15], target = 9
    Returns: [0, 1] because nums[0] + nums[1] = 9
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum, move left pointer right
        else:
            right -= 1  # Need smaller sum, move right pointer left
    
    return []  # No solution found


def reverse_string(s: list[str]) -> None:
    """
    Reverse a string in-place using two pointers.
    Time: O(n), Space: O(1)
    
    Example: ["h","e","l","l","o"] -> ["o","l","l","e","h"]
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# PATTERN 2: SAME DIRECTION (Fast & Slow Pointers)
# ================================================
# Both pointers move in same direction but at different speeds
# Use cases: Remove duplicates, sliding window problems

def remove_duplicates(nums: list[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    Returns the length of array with unique elements.
    Time: O(n), Space: O(1)
    
    Example: [1,1,2,2,3] -> [1,2,3,_,_] returns 3
    """
    if not nums:
        return 0
    
    # Slow pointer tracks position for next unique element
    slow = 0
    
    # Fast pointer explores the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def move_zeroes(nums: list[int]) -> None:
    """
    Move all zeros to the end while maintaining relative order.
    Time: O(n), Space: O(1)
    
    Example: [0,1,0,3,12] -> [1,3,12,0,0]
    """
    # Slow pointer tracks position for next non-zero element
    slow = 0
    
    # Fast pointer finds non-zero elements
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# PATTERN 3: SLIDING WINDOW (Variable Size)
# =========================================
# Use two pointers to maintain a window that expands/contracts
# Use cases: Substrings, subarrays with specific properties

def longest_substring_without_repeating(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    Time: O(n), Space: O(min(n, m)) where m is charset size
    
    Example: "abcabcbb" -> 3 ("abc")
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Contract window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character and update max
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# PATTERN 4: MULTIPLE POINTERS (3+ pointers)
# ==========================================
# Use cases: 3Sum, 4Sum problems

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets that sum to zero.
    Time: O(n�), Space: O(1) excluding output
    
    Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()  # Sort first for two-pointer technique
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Use two pointers for remaining two numbers
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


# TIPS AND TRICKS
# ==============
"""
1. WHEN TO USE TWO POINTERS:
   - Array is sorted or can be sorted
   - Need to find pairs/triplets with specific sum
   - Palindrome problems
   - Partitioning arrays
   - Removing duplicates in-place

2. CHOOSING POINTER MOVEMENT:
   - Opposite direction: When you need to compare/combine elements from both ends
   - Same direction: When you need to track positions (fast/slow pattern)
   - Sliding window: When dealing with subarrays/substrings

3. COMMON MISTAKES TO AVOID:
   - Forgetting to handle edge cases (empty array, single element)
   - Not updating pointers correctly in while loops
   - Off-by-one errors with indices
   - Not handling duplicates when required

4. TIME/SPACE COMPLEXITY:
   - Usually O(n) time for single pass
   - O(n�) for nested two-pointer (like 3Sum)
   - O(1) space (not counting output)

5. PRACTICE PROBLEMS BY DIFFICULTY:
   Easy:
   - Valid Palindrome (LC 125)
   - Two Sum II - Sorted Array (LC 167)
   - Remove Duplicates from Sorted Array (LC 26)
   - Move Zeroes (LC 283)
   
   Medium:
   - 3Sum (LC 15)
   - Container With Most Water (LC 11)
   - Longest Substring Without Repeating Characters (LC 3)
   
   Hard:
   - Trapping Rain Water (LC 42)
   - Minimum Window Substring (LC 76)
"""

if __name__ == "__main__":
    print("\n=== TWO POINTERS TECHNIQUE EXAMPLES ===\n")
    
    # Test Pattern 1: Opposite Direction
    print("1. Palindrome Check:")
    test_strings = ["racecar", "hello", "a", ""]
    for s in test_strings:
        print(f"   '{s}' -> {is_palindrome_simple(s)}")
    
    print("\n2. Two Sum in Sorted Array:")
    nums = [2, 7, 11, 15]
    target = 9
    print(f"   Array: {nums}, Target: {target}")
    print(f"   Indices: {two_sum_sorted(nums, target)}")
    
    # Test Pattern 2: Same Direction
    print("\n3. Remove Duplicates:")
    nums = [1, 1, 2, 2, 3, 3, 3, 4]
    original = nums.copy()
    length = remove_duplicates(nums)
    print(f"   Original: {original}")
    print(f"   Result: {nums[:length]} (length: {length})")
    
    print("\n4. Move Zeroes:")
    nums = [0, 1, 0, 3, 12]
    original = nums.copy()
    move_zeroes(nums)
    print(f"   Original: {original}")
    print(f"   Result: {nums}")
    
    # Test Pattern 3: Sliding Window
    print("\n5. Longest Substring Without Repeating:")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in test_strings:
        print(f"   '{s}' -> {longest_substring_without_repeating(s)}")
    
    # Test Pattern 4: Multiple Pointers
    print("\n6. Three Sum:")
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"   Array: {nums}")
    print(f"   Triplets summing to 0: {three_sum(nums)}")