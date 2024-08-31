# Stack Data Structure

A **stack** is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed. Think of it like a stack of plates; you can only take the top plate off the stack, and you can only add a new plate on top.

## Key Operations

- **push(x)**: Add element `x` to the top of the stack.
- **pop()**: Remove the element from the top of the stack.
- **peek()** or **top()**: Retrieve the top element of the stack without removing it.
- **isEmpty()**: Check if the stack is empty.

## Stack Implementation in Python

Below is a simple implementation of a stack using Python lists:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())  # Output: 3
print(my_stack.peek()) # Output: 2
print(my_stack.is_empty()) # Output: False

## Applications of Stacks

Stacks are used in various real-world and computational scenarios, such as:

- **Expression evaluation and syntax parsing:** Stacks are used to evaluate expressions like infix, postfix, and prefix.
- **Backtracking:** Algorithms like depth-first search (DFS) use stacks to remember the path they have taken.
- **Undo functionality:** Applications like text editors use stacks to keep track of changes, allowing users to undo operations.

## LeetCode Problems

Here are some common LeetCode problems that can be solved using a stack:

- [20. Valid Parentheses](../Leetcode/DataStructure/Stack/valid_parentheses_20.py) - Easy
- [232. Implement Queue using Stacks](../Leetcode/DataStructure/Stack/implement_queue_using_stacks_232.py) - Easy
- [155. Min Stack](../Leetcode/DataStructure/Stack/min_stack_155.py) - Easy
