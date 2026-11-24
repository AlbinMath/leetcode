# LeetCode 967: Numbers With Same Consecutive Differences

**LeetCode Problem #967 — Numbers With Same Consecutive Differences**
Solve LeetCode Numbers With Same Consecutive Differences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Numbers With Same Consecutive Differences |
| LeetCode | #967 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers n and k, return *an array of all the integers of length *`n`* where the difference between every two consecutive digits is *`k`. You may return the answer in **any order**.

Note that the integers should not have leading zeros. Integers as `02` and `043` are not allowed.

## Constraints
- `2 <= n <= 9`
- `0 <= k <= 9`

## Examples
### Example 1
- **Input:** `n = 3, k = 7`
- **Output:** `[181,292,707,818,929]`
- **Explanation:** Note that 070 is not a valid number, because it has leading zeroes.

### Example 2
- **Input:** `n = 2, k = 1`
- **Output:** `[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Numbers With Same Consecutive Differences**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 7`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[181,292,707,818,929]`.
4. **Verification:** Note that 070 is not a valid number, because it has leading zeroes.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = list(range(1, 10))
        for _ in range(n - 1):
            nxt = []
            for num in res:
                last = num % 10
                nxt_digits = {last + k, last - k}  # a set dedups when k == 0
                for d in nxt_digits:
                    if 0 <= d <= 9:
                        nxt.append(num * 10 + d)
            res = nxt
        return res
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [180. Consecutive Numbers](../../0001-0500/0180-consecutive-numbers/)
- [829. Consecutive Numbers Sum](../../0501-1000/0829-consecutive-numbers-sum/)
- [1680. Concatenation of Consecutive Binary Numbers](../../1501-2000/1680-concatenation-of-consecutive-binary-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)
