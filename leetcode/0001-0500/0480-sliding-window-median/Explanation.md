# LeetCode 480: Sliding Window Median

**LeetCode Problem #480 — Sliding Window Median**
Solve LeetCode Sliding Window Median using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Window Median |
| LeetCode | #480 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if `arr = [2, 3 ,4]`, the median is `3`. 
 For examples, if `arr = [1, 2,3 ,4]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the median array for each window in the original array*. Answers within `10^-5` of the actual value will be accepted.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output:** `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`
- **Explanation:** Window position Median
--------------- -----
[

### Example 2
- **Input:** `nums = [1,2,3,4,2,3,1,4,2], k = 3`
- **Output:** `[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Sliding Window Median**, we observe the problem requirements and utilize the **Sliding Window** technique. We maintain a contiguous window defined by `left` and `right` pointers. The right pointer expands the window by adding incoming elements, while the left pointer advances to restore window invariants whenever duplicates or constraint limits are exceeded.

## Algorithm
1. Initialize `left = 0` and window tracking data structures.
2. Expand `right` pointer over input elements.
3. Contract `left` pointer when window invariants are breached.
4. Update global best metric for valid window intervals.
5. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,-1,-3,5,3,6,7], k = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`.
4. **Verification:** Window position Median
--------------- -----
[

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
from bisect import bisect_left, insort
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        w = sorted(nums[:k])
        res = []
        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(w[k // 2]))
            else:
                res.append((w[k // 2 - 1] + w[k // 2]) / 2.0)
            if i == len(nums):
                break
            del w[bisect_left(w, nums[i - k])]
            insort(w, nums[i])
        return res
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
- [239. Sliding Window Maximum](../../0001-0500/0239-sliding-window-maximum/)
- [773. Sliding Puzzle](../../0501-1000/0773-sliding-puzzle/)
- [2653. Sliding Subarray Beauty](../../2501-3000/2653-sliding-subarray-beauty/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-window-median/)
