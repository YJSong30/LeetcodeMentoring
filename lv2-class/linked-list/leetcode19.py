'''
LeetCode 19: Remove Nth Node From End of List

Problem Statement:
Given the head of a linked list, remove the n-th node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The 2nd node from the end is node with value 4.

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: The only node is removed.

Example 3:
Input: head = [1,2], n = 1
Output: [1]
Explanation: The last node (2) is removed.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Task:
- Implement a brute-force (two-pass) solution.
- Implement an optimized one-pass solution using two pointers.
- Analyze the time and space complexity of each.

'''
from typing import Optional

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Contains solutions for the Remove Nth Node From End of List problem.
    """

    def removeNthFromEnd_twopass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: Implement two-pass solution
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next

        if count == n: 
            return head.next

        ptr = head
        for i in range(count - n - 1):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head


    def removeNthFromEnd_onepass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: Implement one-pass solution with two pointers
        ptr1 = head
        ptr2 = head
        
        # Move ptr2 ahead so it can find the end
        for i in range(n):
            ptr2 = ptr2.next

        # ptr2 outside linked list, if n = size of list (remove first node)
        if not ptr2:
            return head.next

        # ptr2 is still in linked list (means n < size of list)
        while ptr2.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next

        # removes the node after after ptr1
        ptr1.next = ptr1.next.next

        return head

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        {"head": [1,2,3,4,5], "n": 2, "expected": [1,2,3,5]},
        {"head": [1], "n": 1, "expected": []},
        {"head": [1,2], "n": 1, "expected": [1]},
        {"head": [1,2], "n": 2, "expected": [2]},
        {"head": [1,2,3], "n": 3, "expected": [2,3]},
        {"head": [1,2,3,4,5,6,7,8,9,10], "n": 7, "expected": [1,2,3,5,6,7,8,9,10]},
    ]

    print()
    print("--- Testing Two-Pass Solution ---")
    print()
    for i, case in enumerate(test_cases):
        values, n, expected = case["head"], case["n"], case["expected"]
        head = create_linked_list(values)
        result_head = solver.removeNthFromEnd_twopass(head, n)
        result = linked_list_to_list(result_head)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    head = {values}, n = {n}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")

    print("--- Testing One-Pass Solution ---")
    print()
    for i, case in enumerate(test_cases):
        values, n, expected = case["head"], case["n"], case["expected"]
        head = create_linked_list(values)
        result_head = solver.removeNthFromEnd_onepass(head, n)
        result = linked_list_to_list(result_head)
        status = "✅ Pass" if result == expected else "❌ Fail"

        print(f"Test Case {i+1}: {status}")
        print(f'  Input:    head = {values}, n = {n}')
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}\n")