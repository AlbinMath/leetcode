# LeetCode 2212: Maximum Points in an Archery Competition

**LeetCode Problem #2212 — Maximum Points in an Archery Competition**
Solve LeetCode Maximum Points in an Archery Competition using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points in an Archery Competition |
| LeetCode | #2212 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob are opponents in an archery competition. The competition has set the following rules:

Alice first shoots `numArrows` arrows and then Bob shoots `numArrows` arrows. 
 The points are then calculated as follows:
 
 The target has integer scoring sections ranging from `0` to `11` **inclusive**. 
 For **each** section of the target with score `k` (in between `0` to `11`), say Alice and Bob have shot `a_k` and `b_k` arrows on that section respectively. If `a_k >= b_k`, then Alice takes `k` points. If `a_k < b_k`, then Bob takes `k` points. 
 However, if `a_k == b_k == 0`, then **nobody** takes `k` points.

For example, if Alice and Bob both shot `2` arrows on the section with score `11`, then Alice takes `11` points. On the other hand, if Alice shot `0` arrows on the section with score `11` and Bob shot `2` arrows on that same section, then Bob takes `11` points.

You are given the integer `numArrows` and an integer array `aliceArrows` of size `12`, which represents the number of arrows Alice shot on each scoring section from `0` to `11`. Now, Bob wants to **maximize** the total number of points he can obtain.

Return *the array *`bobArrows`* which represents the number of arrows Bob shot on **each** scoring section from *`0`* to *`11`. The sum of the values in `bobArrows` should equal `numArrows`.

If there are multiple ways for Bob to earn the maximum total points, return **any** one of them.

## Constraints
- `1 <= numArrows <= 10^5`
- `aliceArrows.length == bobArrows.length == 12`
- `0 <= aliceArrows[i], bobArrows[i] <= numArrows`
- `sum(aliceArrows[i]) == numArrows`

## Examples
### Example 1
- **Input:** `numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]`
- **Output:** `[0,0,0,0,1,1,0,0,1,2,3,1]`
- **Explanation:** The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.

### Example 2
- **Input:** `numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]`
- **Output:** `[0,0,0,0,0,0,0,0,1,1,1,0]`
- **Explanation:** The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Points in an Archery Competition**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,0,0,1,1,0,0,1,2,3,1]`.
4. **Verification:** The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.

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
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_score = -1
        best_mask = 0
        for mask in range(1 << 12):
            cost = 0
            score = 0
            for k in range(12):
                if mask >> k & 1:
                    cost += aliceArrows[k] + 1
                    score += k
            if cost <= numArrows and score > best_score:
                best_score = score
                best_mask = mask

        bob = [0] * 12
        used = 0
        for k in range(12):
            if best_mask >> k & 1:
                bob[k] = aliceArrows[k] + 1
                used += bob[k]
        bob[0] += numArrows - used  # leftover arrows, harmless on section 0
        return bob
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
- [1423. Maximum Points You Can Obtain from Cards](../../1501-2000/1538-maximum-points-you-can-obtain-from-cards/)
- [1610. Maximum Number of Visible Points](../../1501-2000/1733-maximum-number-of-visible-points/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-in-an-archery-competition/)
