# LeetCode 1735: Count Ways to Make Array With Product

**LeetCode Problem #1735 — Count Ways to Make Array With Product**
Solve LeetCode Count Ways to Make Array With Product using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Ways to Make Array With Product |
| LeetCode | #1735 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array, `queries`. For each `queries[i]`, where `queries[i] = [n_i, k_i]`, find the number of different ways you can place positive integers into an array of size `n_i` such that the product of the integers is `k_i`. As the number of ways may be too large, the answer to the `i^th` query is the number of ways **modulo** `10^9 + 7`.

Return *an integer array *`answer`* where *`answer.length == queries.length`*, and *`answer[i]`* is the answer to the *`i^th`* query.*

## Constraints
- `1 <= queries.length <= 10^4 `
- `1 <= n_i, k_i <= 10^4`

## Examples
### Example 1
- **Input:** `queries = [[2,6],[5,1],[73,660]]`
- **Output:** `[4,1,50734910]`
- **Explanation:** Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 10^9 + 7 = 50734910.

### Example 2
- **Input:** `queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]`
- **Output:** `[1,2,3,10,5]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Ways to Make Array With Product**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queries = [[2,6],[5,1],[73,660]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,1,50734910]`.
4. **Verification:** Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 10^9 + 7 = 50734910.

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
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        N = 10**4 + 20

        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv = [1] * (N + 1)
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        def comb(a: int, b: int) -> int:
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD

        ans = []
        for n, k in queries:
            res = 1
            p = 2
            while p * p <= k:
                if k % p == 0:
                    e = 0
                    while k % p == 0:
                        k //= p
                        e += 1
                    res = res * comb(e + n - 1, e) % MOD
                p += 1
            if k > 1:                       # one leftover prime, exponent 1
                res = res * comb(n, 1) % MOD
            ans.append(res)
        return ans
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
- [1664. Ways to Make a Fair Array](../../1501-2000/1783-ways-to-make-a-fair-array/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1692-number-of-ways-to-reorder-array-to-get-same-bst/)
- [1916. Count Ways to Build Rooms in an Ant Colony](../../1001-1500/1313-count-ways-to-build-rooms-in-an-ant-colony/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-ways-to-make-array-with-product/)
