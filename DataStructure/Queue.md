# Queue Data Structure

A **queue** is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed. Think of it like a line of people waiting for a service; the first person in line is the first person to be served.

## Key Operations

- **enqueue(x)**: Add element `x` to the end of the queue.
- **dequeue()**: Remove the element from the front of the queue.
- **front()**: Retrieve the front element of the queue without removing it.
- **isEmpty()**: Check if the queue is empty.

## Queue Implementation in Python

Below is a simple implementation of a queue using Python lists:

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.dequeue())  # Output: 1
print(my_queue.front())    # Output: 2
print(my_queue.is_empty()) # Output: False

## Applications of Queues

Queues are used in various real-world and computational scenarios, such as:

- **Scheduling processes in operating systems:** Queues manage the order of processes to be executed.
- **Handling requests in web servers:** Queues manage incoming requests in the order they are received.
- **Breadth-First Search (BFS) algorithm:** Queues are used to explore all nodes in a graph level by level.

## LeetCode Problems

Here are some common LeetCode problems that can be solved using a queue:

- [225. Implement Stack using Queues](../Leetcode/DataStructure/Queue/implement_stack_using_queues_225.py) - Easy
- [346. Moving Average from Data Stream](../Leetcode/DataStructure/Queue/moving_average_from_data_stream_346.py) - Easy
- [933. Number of Recent Calls](../Leetcode/DataStructure/Queue/number_of_recent_calls_933.py) - Easy
