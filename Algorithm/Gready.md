# Greedy Algorithm

## Introduction

Greedy algorithms are a class of algorithms that build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. The idea behind a greedy algorithm is to follow the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum.

Greedy algorithms are typically used for optimization problems. While greedy algorithms are faster and simpler to implement, they do not always produce the optimal solution for every problem. However, for many problems, they provide a correct solution, and they are particularly useful in scenarios where we can prove that a locally optimal choice leads to a globally optimal solution.

## Characteristics of Greedy Algorithms

1. **Greedy Choice Property**:
   - A globally optimal solution can be arrived at by selecting a locally optimal choice. This property means that the algorithm can build up a solution by choosing the best option at each step.

2. **Optimal Substructure**:
   - A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property is essential for the correctness of a greedy algorithm.

## Common Applications of Greedy Algorithms

Greedy algorithms are widely used in various areas of computer science, particularly in:

1. **Activity Selection Problem**:
   - Selecting the maximum number of activities that don't overlap.

2. **Huffman Coding**:
   - A method used for lossless data compression.

3. **Dijkstra's Algorithm**:
   - For finding the shortest path in a graph with non-negative edge weights.

## Example: The Activity Selection Problem

The Activity Selection Problem is a classic example of a greedy algorithm. The problem is as follows:

Given a set of activities with their start and finish times, select the maximum number of activities that don't overlap. Assume that the activities are sorted by their finish times.

### Solution

1. **Sort the activities** by their finish times.
2. **Select the first activity** from the sorted list and add it to the solution set.
3. For each subsequent activity, **check if it overlaps** with the last selected activity. If it doesn't, add it to the solution set.
4. **Repeat** until all activities have been checked.

### Pseudocode

```text
Sort the activities by finish time
Select the first activity and add it to the solution
For each subsequent activity:
    If the start time of this activity is greater than or equal to the finish time of the last selected activity, select this activity and add it to the solution
Return the solution set
