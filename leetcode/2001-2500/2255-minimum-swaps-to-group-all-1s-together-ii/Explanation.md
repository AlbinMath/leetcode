# LeetCode 2134: Minimum Swaps to Group All 1's Together II

**LeetCode Problem #2134 — Minimum Swaps to Group All 1's Together II**
Solve LeetCode Minimum Swaps to Group All 1's Together II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Group All 1's Together II |
| LeetCode | #2134 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **swap** is defined as taking two **distinct** positions in an array and swapping the values in them.

A **circular** array is defined as an array where we consider the **first** element and the **last** element to be **adjacent**.

Given a **binary** **circular** array `nums`, return *the minimum number of swaps required to group all *`1`*'s present in the array together at **any location***.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `nums = [0,1,0,1,1,0,0]`
- **Output:** `1`
- **Explanation:** Here are a few of the ways to group all the 1's together:
[0, 0 , 1 ,1,1,0,0] using 1 swap.
[0,1, 1 ,1, 0 ,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

### Example 2
- **Input:** `nums = [0,1,1,1,0,0,1,1,0]`
- **Output:** `2`
- **Explanation:** Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

### Example 3
- **Input:** `nums = [1,1,0,0,1]`
- **Output:** `0`
- **Explanation:** All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Swaps to Group All 1's Together II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,0,1,1,0,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Here are a few of the ways to group all the 1's together:
[0, 0 , 1 ,1,1,0,0] using 1 swap.
[0,1, 1 ,1, 0 ,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

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
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        
        if k <= 1 or k == n:
            return 0
            
        curr_ones = sum(nums[:k])
        max_ones = curr_ones
        
        for i in range(1, n):
            right = i + k - 1
            if right >= n:
                right -= n
            curr_ones += nums[right] - nums[i - 1]
            if curr_ones > max_ones:
                max_ones = curr_ones
                
        return k - max_ones
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
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1369-minimum-swaps-to-make-strings-equal/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1536. Minimum Swaps to Arrange a Binary Grid](../../1501-2000/1658-minimum-swaps-to-arrange-a-binary-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/)
