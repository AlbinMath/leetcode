# LeetCode 3878: Count Good Subarrays

**LeetCode Problem #3878 — Count Good Subarrays**
Solve LeetCode Count Good Subarrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Subarrays |
| LeetCode | #3878 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** is called **good** if the **bitwise OR** of all its elements is equal to **at least one** element present in that subarray.

Return the number of good subarrays in `nums`.

Here, the bitwise OR of two integers `a` and `b` is denoted by `a | b`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [4,2,3]`
- **Output:** `4`
- **Explanation:** The subarrays of `nums` are: 

 
 
 
 Subarray 
 Bitwise OR 
 Present in Subarray 
 
 
 `[4]` 
 `4 = 4` 
 Yes 
 
 
 `[2]` 
 `2 = 2` 
 Yes 
 
 
 `[3]` 
 `3 = 3` 
 Yes 
 
 
 `[4, 2]` 
 `4 | 2 = 6` 
 No 
 
 
 `[2, 3]` 
 `2 | 3 = 3` 
 Yes 
 
 
 `[4, 2, 3]` 
 `4 | 2 | 3 = 7` 
 No 
 
 
 

 Thus, the good subarrays of `nums` are `[4]`, `[2]`, `[3]` and `[2, 3]`. Thus, the answer is 4.

### Example 2
- **Input:** `nums = [1,3,1]`
- **Output:** `6`
- **Explanation:** Any subarray of `nums` containing 3 has bitwise OR equal to 3, and subarrays containing only 1 have bitwise OR equal to 1. 

 In both cases, the result is present in the subarray, so all subarrays are good, and the answer is 6.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Good Subarrays**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The subarrays of `nums` are: 

 
 
 
 Subarray 
 Bitwise OR 
 Present in Subarray 
 
 
 `[4]` 
 `4 = 4` 
 Yes 
 
 
 `[2]` 
 `2 = 2` 
 Yes 
 
 
 `[3]` 
 `3 = 3` 
 Yes 
 
 
 `[4, 2]` 
 `4 | 2 = 6` 
 No 
 
 
 `[2, 3]` 
 `2 | 3 = 3` 
 Yes 
 
 
 `[4, 2, 3]` 
 `4 | 2 | 3 = 7` 
 No 
 
 
 

 Thus, the good subarrays of `nums` are `[4]`, `[2]`, `[3]` and `[2, 3]`. Thus, the answer is 4.

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
    def countGoodSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        B = 30

        # L: previous index with value >= nums[i]; R: next index with value > nums[i]
        L = [-1] * n
        R = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)

        # badL / badR: nearest index holding a bit that nums[i] lacks
        badL = [-1] * n
        last = [-1] * B
        for i in range(n):
            x = nums[i]
            m = -1
            for b in range(B):
                if not (x >> b) & 1 and last[b] > m:
                    m = last[b]
            badL[i] = m
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i

        badR = [n] * n
        nxt = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            m = n
            for b in range(B):
                if not (x >> b) & 1 and nxt[b] < m:
                    m = nxt[b]
            badR[i] = m
            for b in range(B):
                if (x >> b) & 1:
                    nxt[b] = i

        ans = 0
        for i in range(n):
            left = i - max(L[i], badL[i])
            right = min(R[i], badR[i]) - i
            ans += left * right
        return ans
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
- [2537. Count the Number of Good Subarrays](../../2501-3000/2537-count-the-number-of-good-subarrays/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-subarrays/)
