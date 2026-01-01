# Beginner-solving-algorithms
This repository is focused on python programs for learning and solving algorithms. It is ideal for beginner Python programmers.



# 1. Binary Search Implementation

## Overview
A Python function that performs binary search on a sorted list and returns the path to the target value.

## Usage
- Call `binary_search` with a sorted list and a target value.
- Returns a tuple: (path to target, result message).




# 2. Luhn Algorithm Credit Card Validator

## Overview
A Python function that validates credit card numbers using the Luhn algorithm.

## Usage
- Call `verify_card_number` with a credit card number (string).
- Returns `'VALID!'` if the number is valid, `'INVALID!'` otherwise.




# 3. Square Root Bisection Method

## Overview
A Python function that calculates the square root of a number using the bisection method.

## Usage
- Call `square_root_bisection` with a number and optional tolerance and max iterations.
- Returns the approximate square root or None if it fails to converge.

## Parameters
- `number`: The input number (must be non-negative).
- `tolerance`: The desired precision (default=0.01).
- `max_iteration`: Max iterations before giving up (default=100).




# 4. Tower of Hanoi Solver

## Overview

This repository contains a Python implementation of the Tower of Hanoi problem, a classic problem in computer science and mathematics. The code solves the problem for a given number of disks and prints the sequence of moves required to solve it.

## Usage

To use this code, simply call the `hanoi_solver` function with the desired number of disks.

## Example Output

The code will print the sequence of moves required to solve the Tower of Hanoi problem for the given number of disks.

## Notes

- The code uses a recursive approach to solve the Tower of Hanoi problem.
- The implementation includes test cases for 5, 4, and 3 disks.


# 5. Dijkstra's Algorithm Implementation

## Overview

This repository contains an implementation of Dijkstra's algorithm in Python, used to find the shortest path between nodes in a weighted graph.

## Code Structure

- The code is contained in a single Python file.
- The `shortest_path` function takes an adjacency matrix, a start node, and an optional target node as input.
- The function returns the shortest distances and paths from the start node to all other nodes (or the target node if specified).

## Usage

To use this code, simply call the `shortest_path` function with the required parameters:
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

shortest_path(adj_matrix, 0, 5)

## Example Output

The code will print the shortest distance and path from the start node to the target node (or all nodes if no target is specified).
0-5 distance: 5
Path: 0 -> 2 -> 1 -> 5

## Notes

- The code assumes that the input graph is represented as an adjacency matrix, where `matrix[i][j]` is the weight of the edge from node `i` to node `j`.
- If there is no edge between nodes `i` and `j`, `matrix[i][j]` should be set to `INF` (defined as `float('inf')`).
- The code uses a priority queue (implemented using a list) to efficiently select the next node to visit.

# Adjacency List to Matrix Converter

## Overview
Converts a graph from adjacency list (dictionary) to adjacency matrix (2D array).

## Input/Output
**Input**: Dictionary where keys = nodes, values = list of connected nodes  
**Output**: 2D matrix where `matrix[i][j] = 1` means edge from i to j

## Example
```python
{0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}

# Becomes:
[[0, 1, 1, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 1],
 [0, 0, 1, 0]]
```

## Algorithm
1. Get number of nodes from dictionary length
2. Create n×n matrix filled with zeros
3. Loop through each node and its neighbors, set `matrix[node][neighbor] = 1`
4. Print and return matrix

## Complexity
- **Time**: O(n²) to create matrix + O(E) to fill edges
- **Space**: O(n²)


# Two Sum - Two Pointers

## Overview
Finds two numbers in a sorted array that add up to a target sum.

## Input/Output
**Input**: Sorted list + target sum  
**Output**: The two numbers that sum to target (or None)

## Example
```python
two_sum([1, 2, 3, 4, 6], 6)  # Returns [2, 4] or similar pair
```

## Algorithm
1. Set `left = 0` and `right = n-1` (start and end)
2. While left < right:
   - If `nums[left] + nums[right] == target`: return pair
   - If sum too small: move left pointer right (increases sum)
   - If sum too large: move right pointer left (decreases sum)
3. Return None if no pair found

## Why It Works
Sorted array means moving left pointer increases sum, moving right decreases it. Single pass finds the answer.

## Complexity
- **Time**: O(n) - one pass through array
- **Space**: O(1) - only two pointers
- **vs Brute Force**: O(n²) → O(n)


# N-Queens - Backtracking

## Overview
Places N queens on N×N chessboard so no two queens attack each other (no shared row, column, or diagonal).

## Input/Output
**Input**: Integer n (board size)  
**Output**: List of all solutions, where each solution is a list showing queen column positions per row

## Example
```python
dfs_n_queens(4)  # Returns [[1, 3, 0, 2], [2, 0, 3, 1]]

# [1, 3, 0, 2] means:
# Row 0: queen in column 1
# Row 1: queen in column 3
# Row 2: queen in column 0
# Row 3: queen in column 2
```

## Algorithm Structure

**is_safe(board, row, col)** - Checks if position is valid
- Loop through previous rows
- Check: same column, both diagonals
- Return True if no conflicts

**backtrack(board, row)** - Recursively places queens
- Base case: if row == n, solution found, save it
- Try each column in current row
- If safe: place queen, recurse to next row, backtrack (remove queen)

**dfs_n_queens(n)** - Main function
- Initialize board as [-1] * n
- Call backtrack starting at row 0
- Return all solutions

## Key Concepts
- **Backtracking**: Try solution → if fails, undo and try another
- **Recursion**: Solve one row at a time
- **Constraint checking**: Verify no attacks before placing

## Complexity
- **Time**: O(N!) - tries many combinations, pruned by is_safe
- **Space**: O(N) - recursion depth + board storage
- 

# Generate Parentheses - BFS

## Overview
Generates all valid combinations of n pairs of parentheses using breadth-first search.

## Input/Output
**Input**: Integer (number of pairs)  
**Output**: List of all valid parentheses combinations

## Example
```python
gen_parentheses(3)
# Returns: ['((()))', '(()())', '(())()', '()(())', '()()()']
```

## Algorithm
1. Start with empty string and counters (opens_used=0, closes_used=0)
2. Use queue for BFS: stores tuples of (current_string, opens, closes)
3. While queue not empty:
   - Pop first element
   - If string length == 2*pairs: add to results (complete solution)
   - If can add '(': append new state with incremented opens
   - If can add ')': append new state with incremented closes
4. Rules:
   - Can add '(' if opens_used < pairs
   - Can add ')' if closes_used < opens_used (keeps valid)

## Why It Works
BFS explores all possible valid paths level by level. Only adds ')' when there are more '(' to ensure validity.

## Complexity
- **Time**: O(4^n / √n) - Catalan number growth
- **Space**: O(4^n / √n) - storing all valid combinations


# DFS - Depth-First Search

## Overview
Traverses a graph using depth-first search, visiting all reachable nodes from a starting node.

## Input/Output
**Input**: Adjacency matrix (2D array) + starting node  
**Output**: List of visited nodes in DFS order

## Example
```python
graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [0, 0, 1, 0]]

dfs(graph, 1)  # Returns [1, 2, 3, 0]
```

## Algorithm
1. Initialize:
   - `visited`: list to store traversal order
   - `stack`: starts with start_node
   - `seen`: set to track visited nodes
2. While stack not empty:
   - Pop last node from stack (LIFO - depth-first)
   - If not seen: mark as seen, add to visited
   - Check all neighbors in adjacency matrix
   - Push unvisited neighbors to stack
3. Return visited nodes in order

## Key Differences: DFS vs BFS
- **DFS**: Uses stack (LIFO), goes deep first
- **BFS**: Uses queue (FIFO), goes level by level
- **DFS**: `stack.pop()` removes from end
- **BFS**: `queue.pop(0)` removes from front

## Complexity
- **Time**: O(V + E) where V=vertices, E=edges
- **Space**: O(V) for stack and seen set




# Contributing

Contributions are welcome! If you'd like to improve the codes or add new features, please submit a pull request.
