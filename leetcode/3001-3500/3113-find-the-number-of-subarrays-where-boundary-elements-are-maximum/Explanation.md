# LeetCode 3113: Find the Number of Subarrays Where Boundary Elements Are Maximum

**LeetCode Problem #3113 — Find the Number of Subarrays Where Boundary Elements Are Maximum**
Solve LeetCode Find the Number of Subarrays Where Boundary Elements Are Maximum using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Subarrays Where Boundary Elements Are Maximum |
| LeetCode | #3113 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **positive** integers `nums`.

Return the number of subarrays of `nums`, where the **first** and the **last** elements of the subarray are *equal* to the **largest** element in the subarray.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,4,3,3,2]`
- **Output:** `6`
- **Explanation:** There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray: 

 
 subarray [

### Example 2
- **Input:** `nums = [3,3,3]`
- **Output:** `6`
- **Explanation:** There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray: 

 
 subarray [

### Example 3
- **Input:** `nums = [1]`
- **Output:** `1`
- **Explanation:** There is a single subarray of `nums` which is [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Number of Subarrays Where Boundary Elements Are Maximum**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,3,3,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray: 

 
 subarray [

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
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []  # [value, count], values non-increasing
        ans = 0
        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
            ans += stack[-1][1]
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
- [3020. Find the Maximum Number of Elements in Subset](../../3001-3500/3020-find-the-maximum-number-of-elements-in-subset/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/)
