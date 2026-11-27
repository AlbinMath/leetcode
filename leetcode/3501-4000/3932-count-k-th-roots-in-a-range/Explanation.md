# LeetCode 3932: Count K-th Roots in a Range

**LeetCode Problem #3932 — Count K-th Roots in a Range**
Solve LeetCode Count K-th Roots in a Range using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count K-th Roots in a Range |
| LeetCode | #3932 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `l`, `r`, and `k`.

An integer `y` is said to be a **perfect k^th power** if there exists an integer `x` such that `y = x^k`.

Return the number of integers `y` in the range `[l, r]` (inclusive) that are **perfect k^th powers**.

## Constraints
- `0 <= l <= r <= 10^9`
- `1 <= k <= 30`

## Examples
### Example 1
- **Input:** `l = 1, r = 9, k = 3`
- **Output:** `2`
- **Explanation:** The perfect cubes in the range `[1, 9]` are:

 
 `1 = 1^3` 
 `8 = 2^3` 
 
Hence, the answer is 2.

### Example 2
- **Input:** `l = 8, r = 30, k = 2`
- **Output:** `3`
- **Explanation:** The perfect squares in the range `[8, 30]` are:

 
 `9 = 3^2` 
 `16 = 4^2` 
 `25 = 5^2` 
 
Hence, the answer is 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count K-th Roots in a Range**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `l = 1, r = 9, k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The perfect cubes in the range `[1, 9]` are:

 
 `1 = 1^3` 
 `8 = 2^3` 
 
Hence, the answer is 2.

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
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if mid ** k <= n:
                    lo = mid
                else:
                    hi = mid - 1
            return lo + 1          # x in [0, lo]

        return count(r) - count(l - 1)
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
- [779. K-th Symbol in Grammar](../../0501-1000/0779-k-th-symbol-in-grammar/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-k-th-roots-in-a-range/)
