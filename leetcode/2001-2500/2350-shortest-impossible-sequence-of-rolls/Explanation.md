# LeetCode 2350: Shortest Impossible Sequence of Rolls

**LeetCode Problem #2350 — Shortest Impossible Sequence of Rolls**
Solve LeetCode Shortest Impossible Sequence of Rolls using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Impossible Sequence of Rolls |
| LeetCode | #2350 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `rolls` of length `n` and an integer `k`. You roll a `k` sided dice numbered from `1` to `k`, `n` times, where the result of the `i^th` roll is `rolls[i]`.

Return* the length of the **shortest** sequence of rolls so that there's no such subsequence in *`rolls`.

A **sequence of rolls** of length `len` is the result of rolling a `k` sided dice `len` times.

## Constraints
- `n == rolls.length`
- `1 <= n <= 10^5`
- `1 <= rolls[i] <= k <= 10^5`

## Examples
### Example 1
- **Input:** `rolls = [4,2,1,2,3,3,2,4,1], k = 4`
- **Output:** `3`
- **Explanation:** Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls.
Every sequence of rolls of length 2, [1, 1], [1, 2], ..., [4, 4], can be taken from rolls.
The sequence [1, 4, 2] cannot be taken from rolls, so we return 3.
Note that there are other sequences that cannot be taken from rolls.

### Example 2
- **Input:** `rolls = [1,1,2,2], k = 2`
- **Output:** `2`
- **Explanation:** Every sequence of rolls of length 1, [1], [2], can be taken from rolls.
The sequence [2, 1] cannot be taken from rolls, so we return 2.
Note that there are other sequences that cannot be taken from rolls but [2, 1] is the shortest.

### Example 3
- **Input:** `rolls = [1,1,3,2,2,2,3,3], k = 4`
- **Output:** `1`
- **Explanation:** The sequence [4] cannot be taken from rolls, so we return 1.
Note that there are other sequences that cannot be taken from rolls but [4] is the shortest.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Impossible Sequence of Rolls**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rolls = [4,2,1,2,3,3,2,4,1], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls.
Every sequence of rolls of length 2, [1, 1], [1, 2], ..., [4, 4], can be taken from rolls.
The sequence [1, 4, 2] cannot be taken from rolls, so we return 3.
Note that there are other sequences that cannot be taken from rolls.

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
from typing import List

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        segments = 0
        for x in rolls:
            seen.add(x)
            if len(seen) == k:
                segments += 1
                seen.clear()
        return segments + 1
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
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)
- [128. Longest Consecutive Sequence](../../0001-0500/0128-longest-consecutive-sequence/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/)
