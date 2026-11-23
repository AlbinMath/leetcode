# LeetCode 239: Sliding Window Maximum

**LeetCode Problem #239 — Sliding Window Maximum**
Solve LeetCode Sliding Window Maximum using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sliding Window Maximum |
| LeetCode | #239 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **Output:** `[3,3,5,5,6,7]`
- **Explanation:** Window position Max
--------------- -----
[1 3 -1] -3 5 3 6 7

### Example 2
- **Input:** `nums = [1], k = 1`
- **Output:** `[1]`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Sliding Window Maximum**, we observe the problem requirements and utilize the **Sliding Window** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,-1,-3,5,3,6,7], k = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3,5,5,6,7]`.
4. **Verification:** Window position Max
--------------- -----
[1 3 -1] -3 5 3 6 7

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
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        q, res = deque(), []
        for i, x in enumerate(nums):
            while q and q[0] <= i-k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
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
- [480. Sliding Window Median](../../0001-0500/0480-sliding-window-median/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)
- [773. Sliding Puzzle](../../0501-1000/0787-sliding-puzzle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sliding-window-maximum/)
