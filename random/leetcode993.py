'''
993. Cousins in Binary Tree

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.

same depth, different parents

dfs way:
dfs(node, parent)

bfs way:
1) use bfs
- create queue
- add root to queue
- check in each level if parents are the same
- [1] -> [2, 3] -> [(4, 2), (5, 3)]
- if parents different, then return true if same level

x_found = y_found = False

if x_found and y_found:
  if level[x] == level[y]:
    return True

if it's mutable, then it's hashable
hash((1,2,3)) works
hash(("a","b")) works
hash((1, (2,3)) works. tuples are immutable

hash(([1,2], 3)) doesn't work. lists are mutable



import deque

queue = deque([root])

x_level, y_level = -1,-1
x_parent, y_parent = None, None

while queue:
  level = 0
  for i in range(len(queue)):
    node = queue.popleft()
    
    if node.val == x:
      x_level = level
      
    if node.val == y:
      y_level = level

    if node.left:
      queue.append(node.left)
      if node.left.val == x:
        x_level = level
        x_parent = node.val
      
      if node.left.val == y:
        y_level = level
        y_parent = node.val

    if node.right:
      queue.append(node.right)
      if node.right.val == x:
        x_level = level
        x_parent = node.val
      
      if node.right.val == y:
        y_level = level
        y_parent = node.val

  level += 1


return x_level == y_level and x_parent != y_parent

'''


# (child, parent) -> (node.left, node)
queue = deque([(root, None)])
level = 0
while queue:
  for i in range(len(queue)):
    node, parent = queue.popleft()
    