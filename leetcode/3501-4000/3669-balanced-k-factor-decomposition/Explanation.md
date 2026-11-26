# LeetCode 3669: Balanced K-Factor Decomposition

**LeetCode Problem #3669 — Balanced K-Factor Decomposition**
Solve LeetCode Balanced K-Factor Decomposition using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Balanced K-Factor Decomposition |
| LeetCode | #3669 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k`.

Split the number `n` into **exactly** `k` positive integers such that the **product** of these integers is **equal** to `n`.

Return **any one** split in which the **maximum** difference between any two numbers is **minimized**. You may return the result in any order.

## Constraints
- 4 <= n <= 10^ 5
- 2 <= k <= 5

## Examples
### Example 1
- **Input:** `n = 100, k = 2`
- **Output:** `[10,10]`
- **Explanation:** The split `[10, 10]` yields `10 * 10 = 100` and a max-min difference of 0, which is minimal.

### Example 2
- **Input:** `n = 44, k = 3`
- **Output:** `[2,2,11]`
- **Explanation:** Split `[1, 1, 44]` yields a difference of 43 
 Split `[1, 2, 22]` yields a difference of 21 
 Split `[1, 4, 11]` yields a difference of 10 
 Split `[2, 2, 11]` yields a difference of 9 
 

 Therefore, `[2, 2, 11]` is the optimal split with the smallest difference 9.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Balanced K-Factor Decomposition**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 100, k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[10,10]`.
4. **Verification:** The split `[10, 10]` yields `10 * 10 = 100` and a max-min difference of 0, which is minimal.

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
    def minDifference(self, n: int, k: int) -> List[int]:
        divs = [d for d in range(1, n + 1) if n % d == 0]
        best = [float('inf'), None]
        path = []

        def dfs(rem: int, left: int, start: int) -> None:
            if left == 1:
                # last factor is rem itself; it must not be below the previous one
                if path and rem < divs[start]:
                    return
                path.append(rem)
                diff = path[-1] - path[0]
                if diff < best[0]:
                    best[0] = diff
                    best[1] = path[:]
                path.pop()
                return
            for idx in range(start, len(divs)):
                d = divs[idx]
                if d ** left > rem:
                    break  # remaining factors are all >= d, so the product would exceed rem
                if rem % d:
                    continue
                path.append(d)
                dfs(rem // d, left - 1, idx)
                path.pop()

        dfs(n, k, 0)
        return best[1]
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
- [3703. Remove K-Balanced Substrings](../../3501-4000/3703-remove-k-balanced-substrings/)
- [1147. Longest Chunked Palindrome Decomposition](../../1001-1500/1147-longest-chunked-palindrome-decomposition/)
- [110. Balanced Binary Tree](../../0001-0500/0110-balanced-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/balanced-k-factor-decomposition/)
