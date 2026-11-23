# LeetCode 598: Range Addition II

**LeetCode Problem #598 — Range Addition II**
Solve LeetCode Range Addition II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Range Addition II |
| LeetCode | #598 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `M` initialized with all `0`'s and an array of operations `ops`, where `ops[i] = [a_i, b_i]` means `M[x][y]` should be incremented by one for all `0 <= x < a_i` and `0 <= y < b_i`.

Count and return *the number of maximum integers in the matrix after performing all the operations*.

## Constraints
- `1 <= m, n <= 4 * 10^4`
- `0 <= ops.length <= 10^4`
- `ops[i].length == 2`
- `1 <= a_i <= m`
- `1 <= b_i <= n`

## Examples
### Example 1
- **Input:** `m = 3, n = 3, ops = [[2,2],[3,3]]`
- **Output:** `4`
- **Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

### Example 2
- **Input:** `m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]`
- **Output:** `4`

### Example 3
- **Input:** `m = 3, n = 3, ops = []`
- **Output:** `9`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Range Addition II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 3, n = 3, ops = [[2,2],[3,3]]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The maximum integer in M is 2, and there are four of it in M. So return 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n

        min_rows = m
        min_cols = n

        for a, b in ops:
            min_rows = min(min_rows, a)
            min_cols = min(min_cols, b)

        return min_rows * min_cols
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)
- [303. Range Sum Query - Immutable](../../0001-0500/0303-range-sum-query---immutable/)
- [304. Range Sum Query 2D - Immutable](../../0001-0500/0304-range-sum-query-2d---immutable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/range-addition-ii/)
