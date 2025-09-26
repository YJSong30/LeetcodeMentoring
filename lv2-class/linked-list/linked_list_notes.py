'''
Create Linked List data structure from scratch
https://www.w3schools.com/dsa/dsa_theory_linkedlists.php

Input: [1, 2, 3, 4]
Output: 1 -> 2 -> 3 -> 4

list1.add_node(5)
1 -> 2 -> 3 -> 4 -> 5

1) Create ListNode class
2) Create Linked List Class
  - include print function
  - include add_node function

'''

items = [1,2,3,4]

class ListNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def build_linked_list(self, items):
    # [1, 2, 3, 4]
    if len(items) > 0:
      self.head = ListNode(items[0])

    ptr = self.head

    for i in range(1, len(items)):
      node = ListNode(items[i])
      ptr.next = node
      ptr = ptr.next
  
  def print_linked_list(self):
    ptr = self.head
    while ptr:
      if ptr.next:
        print(ptr.data, end=" -> ")
      else:
        print(ptr.data)
      ptr = ptr.next
  
  def add_node(self, val): # 1 -> 2 -> 3 -> 4 -> 5
    ptr = self.head
    while ptr.next:
      ptr = ptr.next
    node = ListNode(val)
    ptr.next = node

  def reverse_linked_list(self):
    prev = None
    curr = self.head

    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    self.head = prev

l1 = LinkedList()
l1.build_linked_list(items)
l1.print_linked_list()
l1.add_node(5)
l1.add_node(7)
l1.add_node(11)
l1.print_linked_list()
l1.reverse_linked_list()
l1.print_linked_list()


'''
previousNode = None

0 (Done)
1
2
'''

