# LeetCode 823: Binary Trees With Factors

**LeetCode Problem #823 — Binary Trees With Factors**
Solve LeetCode Binary Trees With Factors using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Trees With Factors |
| LeetCode | #823 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of unique integers, `arr`, where each integer `arr[i]` is strictly greater than `1`.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return *the number of binary trees we can make*. The answer may be too large so return the answer **modulo** `10^9 + 7`.

## Constraints
- `1 <= arr.length <= 1000`
- `2 <= arr[i] <= 10^9`
- All the values of `arr` are **unique**.

## Examples
### Example 1
- **Input:** `arr = [2,4]`
- **Output:** `3`
- **Explanation:** We can make these trees: `[2], [4], [4, 2, 2]`

### Example 2
- **Input:** `arr = [2,4,5,10]`
- **Output:** `7`
- **Explanation:** We can make these trees: `[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]`.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Binary Trees With Factors**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,4]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can make these trees: `[2], [4], [4, 2, 2]`

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}
        
        for i, x in enumerate(arr):
            for j in range(i):
                a = arr[j]
                if a * a > x:
                    break
                    
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        if a == b:
                            dp[x] = (dp[x] + dp[a] * dp[a]) % MOD
                        else:
                            dp[x] = (dp[x] + 2 * dp[a] * dp[b]) % MOD
                            
        return sum(dp.values()) % MOD
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [95. Unique Binary Search Trees II](../../0001-0500/0095-unique-binary-search-trees-ii/)
- [96. Unique Binary Search Trees](../../0001-0500/0096-unique-binary-search-trees/)
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../../0501-1000/0558-logical-or-of-two-binary-grids-represented-as-quad-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-trees-with-factors/)
