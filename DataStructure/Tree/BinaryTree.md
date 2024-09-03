
# Binary Tree

## 1. Introduction

A **Binary Tree** is a tree data structure where each node has at most two children, referred to as the left child and the right child. This structure is widely used in algorithms, data structures, and various applications due to its efficiency in search, sort, and hierarchical storage.

### 1.1 Categories of Binary Trees

Binary trees can be categorized into several types:

#### 1.1.1 Full Binary Tree

A **Full Binary Tree** is one in which every node has either 0 or 2 children.

```
      1
     / \
    2   3
   / \ 
  4  5 
```

#### 1.1.2 Perfect Binary Tree

A **Perfect Binary Tree** is a full binary tree in which all leaves are at the same level.

```
          1
       /     \
      2       3
     / \     / \
    4   5   6   7
   / \ / \ / \ / \
  8  9 10 11 12 13 14 15
```

#### 1.1.3 Complete Binary Tree

A **Complete Binary Tree** is a binary tree where all levels are completely filled except possibly the last, which is filled from left to right.

```
      1
     / \
    2   3
   / \  /
  4   5 6
```

#### 1.1.4 Balanced Binary Tree

A **Balanced Binary Tree** is one where the height of the two subtrees of every node differs by at most one.

```
      1
     / \
    2   3
   /     \
  4       5
```

#### 1.1.5 Degenerate (or Pathological) Tree

A **Degenerate Tree** is one where each parent node has only one child, effectively forming a linked list.

```
    1
     \
      2
       \
        3
         \
          4
```

## 2. Traversal Methods

Traversal is the process of visiting all the nodes in a specific order. There are several ways to traverse a binary tree:

### 2.1 In-Order Traversal (Left, Root, Right)

For a binary tree:

```
      1
     / \
    2   3
   / \
  4   5
```

In-Order Traversal (Left, Root, Right) visits the nodes in this order:

```
4 → 2 → 5 → 1 → 3
```
#### Recursive Method

```python
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)   # Step 1: Traverse the left subtree
        print(root.value, end=" ")     # Step 2: Visit the root node
        inorder_traversal(root.right)  # Step 3: Traverse the right subtree
```

#### Iterative Method

```python
def inorder_traversal_iterative(root):
    stack = []
    current = root
    result = []
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result
```

### 2.2 Pre-Order Traversal (Root, Left, Right)

For the same binary tree:

```
      1
     / \
    2   3
   / \
  4   5
```

Pre-Order Traversal (Root, Left, Right) visits the nodes in this order:

```
1 → 2 → 4 → 5 → 3
```
#### Recursive Method

```python
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")      # Step 1: Visit the root node
        preorder_traversal(root.left)   # Step 2: Traverse the left subtree
        preorder_traversal(root.right)  # Step 3: Traverse the right subtree
```

#### Iterative Method

```python
def preorder_traversal_iterative(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current.value)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result
```

### 2.3 Post-Order Traversal (Left, Right, Root)

For the same binary tree:

```
      1
     / \
    2   3
   / \
  4   5
```

Post-Order Traversal (Left, Right, Root) visits the nodes in this order:

```
4 → 5 → 2 → 3 → 1
```
#### Recursive Method

```python
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)   # Step 1: Traverse the left subtree
        postorder_traversal(root.right)  # Step 2: Traverse the right subtree
        print(root.value, end=" ")       # Step 3: Visit the root node
```

#### Iterative Method

```python
def postorder_traversal_iterative(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []
    
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    
    while stack2:
        result.append(stack2.pop().value)
    
    return result
```

### 2.4 Level-Order Traversal (Breadth-First)

For the same binary tree:

```
      1
     / \
    2   3
   / \
  4   5
```

Level-Order Traversal visits the nodes level by level:

```
1 → 2 → 3 → 4 → 5
```

## 3. Representation of Binary Trees in Python

Binary trees can be represented in various ways in Python:

### 3.1 Node-Based Representation

The most common way to represent a binary tree is by using a `Node` class:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### 3.2 List-Based Representation

A binary tree can also be represented using a list, particularly useful when dealing with a complete binary tree:

```python
# Example of a binary tree represented as a list:
#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7

tree = [1, 2, 3, 4, 5, 6, 7]
```

### 3.3 Dictionary-Based Representation

For certain applications, you might use a dictionary to store the binary tree:

```python
tree_dict = {
    'root': 1,
    'left': {
        'root': 2,
        'left': {'root': 4},
        'right': {'root': 5},
    },
    'right': {
        'root': 3,
        'left': {'root': 6},
        'right': {'root': 7},
    }
}
```

## 4. Visual Representation of Binary Trees

Visualizing a binary tree can greatly enhance understanding. Below is a simple example of how you can visualize a binary tree using text-based output:

### 4.1 Simple Text Visualization

```python
def print_tree(root, level=0, label="."):
    prefix = " " * (level * 4) + label + ": "
    print(prefix + str(root.value))
    if root.left:
        print_tree(root.left, level + 1, "L")
    if root.right:
        print_tree(root.right, level + 1, "R")
```

### 4.2 Visualization Using Libraries (e.g., `graphviz`)

For more complex visualizations, you can use external libraries like `graphviz` to create graphical representations of the binary tree.

```python
from graphviz import Digraph

def visualize_tree(root):
    def add_nodes_edges(tree, dot=None):
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree.value), label=str(tree.value))
        
        if tree.left:
            dot.node(name=str(tree.left.value), label=str(tree.left.value))
            dot.edge(str(tree.value), str(tree.left.value))
            dot = add_nodes_edges(tree.left, dot=dot)
        
        if tree.right:
            dot.node(name=str(tree.right.value), label=str(tree.right.value))
            dot.edge(str(tree.value), str(tree.right.value))
            dot = add_nodes_edges(tree.right, dot=dot)
        
        return dot
    
    dot = add_nodes_edges(root)
    return dot

# Example usage:
# tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# visualize_tree(tree).view()
```

## 5. Example Problems and Solutions
### 5.1 Problem: Maximum Depth of a Binary Tree

```python
def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1
```

### 5.2 Problem: Check if a Binary Tree is Balanced

```python
def is_balanced(root):
    def check(root):
        if not root:
            return 0, True
        left_height, left_balanced = check(root.left)
        right_height, right_balanced = check(root.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced
    
    return check(root)[1]
```
## LeetCode Problems

- [144. Binary Tree Preorder Traversal](../Leetcode/DataStructure/Tree/binary_tree_preorder_traversal_144.py) - Easy
- [145. Binary Tree Postorder Traversal](../Leetcode/DataStructure/Tree/binary_tree_postorder_traversal_145.py) - Easy
- [94. Binary Tree Inorder Traversal](../Leetcode/DataStructure/Tree/binary_tree_inorder_traversal_94.py) - Easy