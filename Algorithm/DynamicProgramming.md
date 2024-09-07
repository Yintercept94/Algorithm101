
# Dynamic Programming: Fibonacci Number

## Introduction to Dynamic Programming

Dynamic Programming (DP) is an algorithmic technique used to solve optimization problems by breaking them down into simpler subproblems. The key idea is to store the solutions to the subproblems, avoiding the need to recompute them multiple times, leading to efficient problem-solving.

### Key Concepts of Dynamic Programming:

1. **Overlapping Subproblems**:  
   Many problems can be divided into subproblems that are solved repeatedly. DP solves each subproblem once and stores the result.

2. **Optimal Substructure**:  
   A problem exhibits an optimal substructure if the solution to the problem can be composed of solutions to its subproblems.

3. **Memoization** (Top-down approach):  
   A technique to store intermediate results to avoid recomputation.

4. **Tabulation** (Bottom-up approach):  
   A method to solve subproblems first and use their solutions to build up the solution to the original problem.

---

## Fibonacci Number Using Dynamic Programming

The Fibonacci problem is an excellent introduction to dynamic programming. In this problem, the goal is to compute the nth Fibonacci number. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

---

## Dynamic Programming Steps (Five Steps):

1. **Define the DP array**:  
   Let `dp[i]` be the Fibonacci number for index `i`.

2. **Recurrence relation**:  
   The relation is simple:  
   `dp[i] = dp[i - 1] + dp[i - 2]`  
   This defines how the ith Fibonacci number is derived from the previous two.

3. **Initialization**:  
   The base cases are already given:  
   `dp[0] = 0` and `dp[1] = 1`.

4. **Order of computation**:  
   Since `dp[i]` depends on `dp[i - 1]` and `dp[i - 2]`, the iteration will go from 2 to n.

5. **Example of DP Array**:  
   For `n = 10`, the dp array will look like this:  
   `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`.

---

## Python Implementation

### Tabulation (Bottom-up) Approach:

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example
print(fib(10))  # Output: 55
```

- **Time Complexity**: O(n)  
  We compute each Fibonacci number exactly once.

- **Space Complexity**: O(n)  
  We store the results of each Fibonacci number in an array.

---

## Optimized Space Solution

Instead of storing all Fibonacci numbers, we can optimize space by only keeping the last two values.

### Optimized Python Code:

```python
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Example
print(fib(10))  # Output: 55
```

- **Time Complexity**: O(n)  
  Same as the previous approach.

- **Space Complexity**: O(1)  
  We only maintain two variables.

---

## Recursive Approach

The recursive approach calculates Fibonacci numbers without memoization. This solution is inefficient for large inputs because it recalculates subproblems many times.

### Recursive Python Code:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Example
print(fib(10))  # Output: 55
```

- **Time Complexity**: O(2^n)  
  The function calls itself multiple times, leading to exponential growth.

- **Space Complexity**: O(n)  
  The space complexity includes the recursion stack depth.

---

## Leetcode Problems

### LeetCode: [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

The Fibonacci numbers, denoted as F(n), form a sequence defined by the recurrence relation:
- F(0) = 0, F(1) = 1
- F(n) = F(n - 1) + F(n - 2) for n > 1

Given an integer `n`, compute the nth Fibonacci number.

### Example 1:

**Input**: 2  
**Output**: 1  
**Explanation**: F(2) = F(1) + F(0) = 1 + 0 = 1

### Example 2:

**Input**: 3  
**Output**: 2  
**Explanation**: F(3) = F(2) + F(1) = 1 + 1 = 2

### Example 3:

**Input**: 4  
**Output**: 3  
**Explanation**: F(4) = F(3) + F(2) = 2 + 1 = 3

### Constraints:
- 0 <= n <= 30

- [509. Fibonacci Number](../Leetcode/Algorithm/DynamicProgramming/fibonacci_number_509.py) - Easy
- [70. Climbing Stairs](../Leetcode/Algorithm/DynamicProgramming/climbing_stairs_70.py) - Easy
- [746. Min Cost Climbing Stairs](../Leetcode/Algorithm/DynamicProgramming/min_cost_climbing_stairs_746.py) - Easy