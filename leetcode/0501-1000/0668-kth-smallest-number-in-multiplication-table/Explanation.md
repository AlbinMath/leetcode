# LeetCode 668: Kth Smallest Number in Multiplication Table

**LeetCode Problem #668 — Kth Smallest Number in Multiplication Table**
Solve LeetCode Kth Smallest Number in Multiplication Table using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Number in Multiplication Table |
| LeetCode | #668 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Nearly everyone has used the Multiplication Table . The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (**1-indexed**).

Given three integers `m`, `n`, and `k`, return *the *`k^th`* smallest element in the *`m x n`* multiplication table*.

## Constraints
- `1 <= m, n <= 3 * 10^4`
- `1 <= k <= m * n`

## Examples
### Example 1
- **Input:** `m = 3, n = 3, k = 5`
- **Output:** `3`
- **Explanation:** The 5^th smallest number is 3.

### Example 2
- **Input:** `m = 2, n = 3, k = 6`
- **Output:** `6`
- **Explanation:** The 6^th smallest number is 6.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Kth Smallest Number in Multiplication Table**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 3, n = 3, k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The 5^th smallest number is 3.

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
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) >= k:
                r = mid
            else:
                l = mid + 1
        return l
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
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1978-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)
- [2343. Query Kth Smallest Trimmed Number](../../2001-2500/2422-query-kth-smallest-trimmed-number/)
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)
