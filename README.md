# Beginner-solving-algorithms
This repository is focused on python programs for learning and solving algorithms. It is ideal for beginner Python programmers.


# HashTable Implementation

Overview
A Python class implementing a basic hash table with separate chaining for collision resolution.

## Methods
- `__init__`: Initializes the hash table.
- `hash(key)`: Computes a hash value for a given key.
- `add(key, value)`: Adds a key-value pair to the table.
- `remove(key)`: Removes a key-value pair from the table.
- `lookup(key)`: Retrieves the value associated with a key.




# Binary Search Implementation

Overview
A Python function that performs binary search on a sorted list and returns the path to the target value.

## Usage
- Call `binary_search` with a sorted list and a target value.
- Returns a tuple: (path to target, result message).




# Luhn Algorithm Credit Card Validator

## Overview
A Python function that validates credit card numbers using the Luhn algorithm.

## Usage
- Call `verify_card_number` with a credit card number (string).
- Returns `'VALID!'` if the number is valid, `'INVALID!'` otherwise.




# Square Root Bisection Method

## Overview
A Python function that calculates the square root of a number using the bisection method.

## Usage
- Call `square_root_bisection` with a number and optional tolerance and max iterations.
- Returns the approximate square root or None if it fails to converge.

## Parameters
- `number`: The input number (must be non-negative).
- `tolerance`: The desired precision (default=0.01).
- `max_iteration`: Max iterations before giving up (default=100).
