# LeetCode 1387: Sort Integers by The Power Value

**LeetCode Problem #1387 — Sort Integers by The Power Value**
Solve LeetCode Sort Integers by The Power Value using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Integers by The Power Value |
| LeetCode | #1387 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The power of an integer `x` is defined as the number of steps needed to transform `x` into `1` using the following steps:

if `x` is even then `x = x / 2` 
 if `x` is odd then `x = 3 * x + 1`

For example, the power of `x = 3` is `7` because `3` needs `7` steps to become `1` (`3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1`).

Given three integers `lo`, `hi` and `k`. The task is to sort all integers in the interval `[lo, hi]` by the power value in **ascending order**, if two or more integers have **the same** power value sort them by **ascending order**.

Return the `k^th` integer in the range `[lo, hi]` sorted by the power value.

Notice that for any integer `x` `(lo <= x <= hi)` it is **guaranteed** that `x` will transform into `1` using these steps and that the power of `x` is will **fit** in a 32-bit signed integer.

## Constraints
- `1 <= lo <= hi <= 1000`
- `1 <= k <= hi - lo + 1`

## Examples
### Example 1
- **Input:** `lo = 12, hi = 15, k = 2`
- **Output:** `13`
- **Explanation:** The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.

### Example 2
- **Input:** `lo = 7, hi = 11, k = 4`
- **Output:** `7`
- **Explanation:** The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort Integers by The Power Value**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `lo = 12, hi = 15, k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.

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
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}

        def power(x):
            path = []
            while x not in cache:
                path.append(x)
                x = x // 2 if x % 2 == 0 else 3 * x + 1
            steps = cache[x]
            for v in reversed(path):
                steps += 1
                cache[v] = steps
            return cache[path[0]] if path else steps

        nums = sorted(range(lo, hi + 1), key=lambda v: (power(v), v))
        return nums[k - 1]
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
- [1356. Sort Integers by The Number of 1 Bits](../../1001-1500/1458-sort-integers-by-the-number-of-1-bits/)
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-integers-by-the-power-value/)
