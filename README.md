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


## Contributing

Contributions are welcome! If you'd like to improve the codes or add new features, please submit a pull request.
