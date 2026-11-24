# LeetCode 2830: Maximize the Profit as the Salesman

**LeetCode Problem #2830 — Maximize the Profit as the Salesman**
Solve LeetCode Maximize the Profit as the Salesman using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Profit as the Salesman |
| LeetCode | #2830 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` representing the number of houses on a number line, numbered from `0` to `n - 1`.

Additionally, you are given a 2D integer array `offers` where `offers[i] = [start_i, end_i, gold_i]`, indicating that `i^th` buyer wants to buy all the houses from `start_i` to `end_i` for `gold_i` amount of gold.

As a salesman, your goal is to **maximize** your earnings by strategically selecting and selling houses to buyers.

Return *the maximum amount of gold you can earn*.

**Note** that different buyers can't buy the same house, and some houses may remain unsold.

## Constraints
- `1 <= n <= 10^5`
- `1 <= offers.length <= 10^5`
- `offers[i].length == 3`
- `0 <= start_i <= end_i <= n - 1`
- `1 <= gold_i <= 10^3`

## Examples
### Example 1
- **Input:** `n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]`
- **Output:** `3`
- **Explanation:** There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,0] to 1^st buyer for 1 gold and houses in the range [1,3] to 3^rd buyer for 2 golds.
It can be proven that 3 is the maximum amount of gold we can achieve.

### Example 2
- **Input:** `n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]`
- **Output:** `10`
- **Explanation:** There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,2] to 2^nd buyer for 10 golds.
It can be proven that 10 is the maximum amount of gold we can achieve.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Profit as the Salesman**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,0] to 1^st buyer for 1 gold and houses in the range [1,3] to 3^rd buyer for 2 golds.
It can be proven that 3 is the maximum amount of gold we can achieve.

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

class Solution:
    def maximizeTheProfit(self, n, offers):
        offers.sort(key=lambda o: o[1])
        ends = [-1]
        best = [0]
        for s, e, g in offers:
            idx = bisect_left(ends, s) - 1   # last end < s
            best.append(max(best[-1], best[idx] + g))
            ends.append(e)
        return best[-1]
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
- [826. Most Profit Assigning Work](../../0501-1000/0826-most-profit-assigning-work/)
- [1235. Maximum Profit in Job Scheduling](../../1001-1500/1235-maximum-profit-in-job-scheduling/)
- [1599. Maximum Profit of Operating a Centennial Wheel](../../1501-2000/1599-maximum-profit-of-operating-a-centennial-wheel/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/)
