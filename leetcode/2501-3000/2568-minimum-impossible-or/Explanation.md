# LeetCode 2568: Minimum Impossible OR

**LeetCode Problem #2568 — Minimum Impossible OR**
Solve LeetCode Minimum Impossible OR using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Impossible OR |
| LeetCode | #2568 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

We say that an integer x is **expressible** from `nums` if there exist some integers `0 <= index_1 < index_2 < ... < index_k < nums.length` for which `nums[index_1] | nums[index_2] | ... | nums[index_k] = x`. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of `nums`.

Return *the minimum **positive non-zero integer** that is not **expressible from *`nums`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1]`
- **Output:** `4`
- **Explanation:** 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.

### Example 2
- **Input:** `nums = [5,3,2]`
- **Output:** `1`
- **Explanation:** We can show that 1 is the smallest number that is not expressible.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Impossible OR**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.

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
from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        p = 1
        while p in s:
            p <<= 1
        return p
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
- [2350. Shortest Impossible Sequence of Rolls](../../2001-2500/2350-shortest-impossible-sequence-of-rolls/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-impossible-or/)
