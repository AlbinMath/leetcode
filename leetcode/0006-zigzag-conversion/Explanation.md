# LeetCode 6: Zigzag Conversion

**LeetCode Problem #6 — Zigzag Conversion**
Solve LeetCode Zigzag Conversion using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zigzag Conversion |
| LeetCode | #6 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
The string  "PAYPALISHIRING"  is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code simulates the process of writing characters into rows, changing direction when it hits the top or bottom row.
1. Edge cases are handled first: If `numRows` is 1 or greater than or equal to the length of the string, the string is returned as is, since a zigzag pattern isn't possible or wouldn't change the string.
2. It initializes a list of strings called `rows`, with one empty string for each row.
3. It uses a `current_row` variable to keep track of which row to place the current character in, and a `direction` variable (`1` for moving down, `-1` for moving up).
4. It iterates through each character `char` in the string `s`:
   - It appends the character to the string at `rows[current_row]`.
   - It checks if we are at the top row (`current_row == 0`). If so, we need to change direction to move downwards (`direction = 1`).
   - It checks if we are at the bottom row (`current_row == numRows - 1`). If so, we change direction to move upwards (`direction = -1`).
   - It updates `current_row` by adding the `direction` to move to the next row for the next character.
5. After all characters are placed in their respective rows, it joins all strings in the `rows` list together using `"".join(rows)` and returns the resulting string.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Zigzag Conversion**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3497. Analyze Subscription Conversion ](../3848-analyze-subscription-conversion-/)
- [3699. Number of ZigZag Arrays I](../3962-number-of-zigzag-arrays-i/)
- [3700. Number of ZigZag Arrays II](../3964-number-of-zigzag-arrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zigzag-conversion/)
