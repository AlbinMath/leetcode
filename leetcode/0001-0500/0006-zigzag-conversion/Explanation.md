# LeetCode 6: Zigzag Conversion

**LeetCode Problem #6 — Zigzag Conversion**
Solve LeetCode Zigzag Conversion using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zigzag Conversion |
| LeetCode | #6 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P A H N
A P L S I I G
Y I R

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

## Examples
### Example 1
- **Input:** `s = "PAYPALISHIRING", numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`

### Example 2
- **Input:** `s = "PAYPALISHIRING", numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`
- **Explanation:** P I N
A L S I G
Y A H R
P I

### Example 3
- **Input:** `s = "A", numRows = 1`
- **Output:** `"A"`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

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
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "PAYPALISHIRING", numRows = 3`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"PAHNAPLSIIGYIR"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3497. Analyze Subscription Conversion ](../../3501-4000/3848-analyze-subscription-conversion-/)
- [3528. Unit Conversion I](../../3501-4000/3729-unit-conversion-i/)
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zigzag-conversion/)
