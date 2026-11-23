# LeetCode 3001: Minimum Moves to Capture The Queen

**LeetCode Problem #3001 — Minimum Moves to Capture The Queen**
Solve LeetCode Minimum Moves to Capture The Queen using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Capture The Queen |
| LeetCode | #3001 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **1-indexed** `8 x 8` chessboard containing `3` pieces.

You are given `6` integers `a`, `b`, `c`, `d`, `e`, and `f` where:

`(a, b)` denotes the position of the white rook. 
 `(c, d)` denotes the position of the white bishop. 
 `(e, f)` denotes the position of the black queen.

Given that you can only move the white pieces, return *the **minimum** number of moves required to capture the black queen*.

**Note** that:

Rooks can move any number of squares either vertically or horizontally, but cannot jump over other pieces. 
 Bishops can move any number of squares diagonally, but cannot jump over other pieces. 
 A rook or a bishop can capture the queen if it is located in a square that they can move to. 
 The queen does not move.

## Constraints
- `1 <= a, b, c, d, e, f <= 8`
- No two pieces are on the same square.

## Examples
### Example 1
- **Input:** `a = 1, b = 1, c = 8, d = 8, e = 2, f = 3`
- **Output:** `2`
- **Explanation:** We can capture the black queen in two moves by moving the white rook to (1, 3) then to (2, 3).
It is impossible to capture the black queen in less than two moves since it is not being attacked by any of the pieces at the beginning.

### Example 2
- **Input:** `a = 5, b = 3, c = 3, d = 4, e = 5, f = 2`
- **Output:** `1`
- **Explanation:** We can capture the black queen in a single move by doing one of the following: 
- Move the white rook to (5, 2).
- Move the white bishop to (5, 2).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Moves to Capture The Queen**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 1, b = 1, c = 8, d = 8, e = 2, f = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can capture the black queen in two moves by moving the white rook to (1, 3) then to (2, 3).
It is impossible to capture the black queen in less than two moves since it is not being attacked by any of the pieces at the beginning.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def between(x, lo, hi):
            return min(lo, hi) < x < max(lo, hi)

        # Rook (a, b) -> queen (e, f)
        if a == e and not (c == a and between(d, b, f)):
            return 1
        if b == f and not (d == b and between(c, a, e)):
            return 1

        # Bishop (c, d) -> queen (e, f)
        if abs(c - e) == abs(d - f):
            # Rook blocks if it is on the same diagonal, strictly between
            if not (abs(a - c) == abs(b - d)
                    and abs(a - e) == abs(b - f)
                    and between(a, c, e)):
                return 1

        return 2
```

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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1322-minimum-moves-to-reach-target-with-rotations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-capture-the-queen/)
