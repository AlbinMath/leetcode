# LeetCode 2427: Number of Common Factors

**LeetCode Problem #2427 — Number of Common Factors**
Solve LeetCode Number of Common Factors using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Common Factors |
| LeetCode | #2427 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two positive integers `a` and `b`, return *the number of **common** factors of *`a`* and *`b`.

An integer `x` is a **common factor** of `a` and `b` if `x` divides both `a` and `b`.

## Constraints
- `1 <= a, b <= 1000`

## Examples
### Example 1
- **Input:** `a = 12, b = 6`
- **Output:** `4`
- **Explanation:** The common factors of 12 and 6 are 1, 2, 3, 6.

### Example 2
- **Input:** `a = 25, b = 30`
- **Output:** `2`
- **Explanation:** The common factors of 25 and 30 are 1, 5.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Number of Common Factors**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 12, b = 6`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The common factors of 12 and 6 are 1, 2, 3, 6.

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
from math import gcd
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(gcd(a,b)%i==0 for i in range(1,gcd(a,b)+1))
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
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [235. Lowest Common Ancestor of a Binary Search Tree](../../0001-0500/0235-lowest-common-ancestor-of-a-binary-search-tree/)
- [236. Lowest Common Ancestor of a Binary Tree](../../0001-0500/0236-lowest-common-ancestor-of-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-common-factors/)
