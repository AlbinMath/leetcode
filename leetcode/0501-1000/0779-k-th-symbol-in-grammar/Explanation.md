# LeetCode 779: K-th Symbol in Grammar

**LeetCode Problem #779 — K-th Symbol in Grammar**
Solve LeetCode K-th Symbol in Grammar using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Symbol in Grammar |
| LeetCode | #779 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We build a table of `n` rows (**1-indexed**). We start by writing `0` in the `1^st` row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

For example, for `n = 3`, the `1^st` row is `0`, the `2^nd` row is `01`, and the `3^rd` row is `0110`.

Given two integer `n` and `k`, return the `k^th` (**1-indexed**) symbol in the `n^th` row of a table of `n` rows.

## Constraints
- `1 <= n <= 30`
- `1 <= k <= 2^n - 1`

## Examples
### Example 1
- **Input:** `n = 1, k = 1`
- **Output:** `0`
- **Explanation:** row 1: 0

### Example 2
- **Input:** `n = 2, k = 1`
- **Output:** `0`
- **Explanation:** row 1: 0
row 2: 0 1

### Example 3
- **Input:** `n = 2, k = 2`
- **Output:** `1`
- **Explanation:** row 1: 0
row 2: 0 1

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **K-th Symbol in Grammar**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** row 1: 0

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
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2
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
- [440. K-th Smallest in Lexicographical Order](../../0001-0500/0440-k-th-smallest-in-lexicographical-order/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [786. K-th Smallest Prime Fraction](../../0501-1000/0786-k-th-smallest-prime-fraction/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/)
