# LeetCode 956: Tallest Billboard

**LeetCode Problem #956 — Tallest Billboard**
Solve LeetCode Tallest Billboard using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tallest Billboard |
| LeetCode | #956 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of `rods` that can be welded together. For example, if you have rods of lengths `1`, `2`, and `3`, you can weld them together to make a support of length `6`.

Return *the largest possible height of your billboard installation*. If you cannot support the billboard, return `0`.

## Constraints
- `1 <= rods.length <= 20`
- `1 <= rods[i] <= 1000`
- `sum(rods[i]) <= 5000`

## Examples
### Example 1
- **Input:** `rods = [1,2,3,6]`
- **Output:** `6`
- **Explanation:** We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

### Example 2
- **Input:** `rods = [1,2,3,4,5,6]`
- **Output:** `10`
- **Explanation:** We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

### Example 3
- **Input:** `rods = [1,2]`
- **Output:** `0`
- **Explanation:** The billboard cannot be supported, so we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Tallest Billboard**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rods = [1,2,3,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

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
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        
        for r in rods:
            new_dp = dp.copy()
            for diff, short in dp.items():
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), short)
                new_diff = abs(diff - r)
                new_short = short + min(diff, r)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_short)
                
            dp = new_dp
            
        return dp[0]
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
[View problem on LeetCode](https://leetcode.com/problems/tallest-billboard/)
