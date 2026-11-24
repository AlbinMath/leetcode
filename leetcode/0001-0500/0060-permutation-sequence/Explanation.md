# LeetCode 60: Permutation Sequence

**LeetCode Problem #60 — Permutation Sequence**
Solve LeetCode Permutation Sequence using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Permutation Sequence |
| LeetCode | #60 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

`"123"` 
 `"132"` 
 `"213"` 
 `"231"` 
 `"312"` 
 `"321"`

Given `n` and `k`, return the `k^th` permutation sequence.

## Constraints
- `1 <= n <= 9`
- `1 <= k <= n!`

## Examples
### Example 1
- **Input:** `n = 3, k = 3`
- **Output:** `"213"`

### Example 2
- **Input:** `n = 4, k = 9`
- **Output:** `"2314"`

### Example 3
- **Input:** `n = 3, k = 1`
- **Output:** `"123"`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Permutation Sequence**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 3`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"213"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1, n + 1)))
        k -= 1
        res = ""
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            res += nums.pop(k // f)
            k %= f
        return res
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [128. Longest Consecutive Sequence](../../0001-0500/0128-longest-consecutive-sequence/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0903-valid-permutations-for-di-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/permutation-sequence/)
