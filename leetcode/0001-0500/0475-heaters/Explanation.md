# LeetCode 475: Heaters

**LeetCode Problem #475 — Heaters**
Solve LeetCode Heaters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Heaters |
| LeetCode | #475 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of `houses` and `heaters` on a horizontal line, return *the minimum radius standard of heaters so that those heaters could cover all houses.*

**Notice** that all the `heaters` follow your radius standard, and the warm radius will be the same.

## Constraints
- `1 <= houses.length, heaters.length <= 3 * 10^4`
- `1 <= houses[i], heaters[i] <= 10^9`

## Examples
### Example 1
- **Input:** `houses = [1,2,3], heaters = [2]`
- **Output:** `1`
- **Explanation:** The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

### Example 2
- **Input:** `houses = [1,2,3,4], heaters = [1,4]`
- **Output:** `1`
- **Explanation:** The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.

### Example 3
- **Input:** `houses = [1,5], heaters = [2]`
- **Output:** `3`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Heaters**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `houses = [1,2,3], heaters = [2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

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
from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0

        for h in houses:
            i = bisect_left(heaters, h)
            left = h - heaters[i - 1] if i > 0 else float('inf')
            right = heaters[i] - h if i < len(heaters) else float('inf')
            radius = max(radius, min(left, right))

        return radius
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/heaters/)
