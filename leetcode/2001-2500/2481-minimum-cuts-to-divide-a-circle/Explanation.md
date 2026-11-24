# LeetCode 2481: Minimum Cuts to Divide a Circle

**LeetCode Problem #2481 — Minimum Cuts to Divide a Circle**
Solve LeetCode Minimum Cuts to Divide a Circle using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cuts to Divide a Circle |
| LeetCode | #2481 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **valid cut** in a circle can be:

A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or 
 A cut that is represented by a straight line that touches one point on the edge of the circle and its center.

Some valid and invalid cuts are shown in the figures below.

Given the integer `n`, return *the **minimum** number of cuts needed to divide a circle into *`n`* equal slices*.

## Constraints
- `1 <= n <= 100`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `2`
- **Explanation:** The above figure shows how cutting the circle twice through the middle divides it into 4 equal slices.

### Example 2
- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** At least 3 cuts are needed to divide the circle into 3 equal slices. 
It can be shown that less than 3 cuts cannot result in 3 slices of equal size and shape.
Also note that the first cut will not divide the circle into distinct parts.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Cuts to Divide a Circle**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The above figure shows how cutting the circle twice through the middle divides it into 4 equal slices.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3010-divide-an-array-into-subarrays-with-minimum-cost-i/)
- [3013. Divide an Array Into Subarrays With Minimum Cost II](../../3001-3500/3013-divide-an-array-into-subarrays-with-minimum-cost-ii/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/)
