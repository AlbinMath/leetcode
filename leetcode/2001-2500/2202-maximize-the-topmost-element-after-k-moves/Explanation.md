# LeetCode 2202: Maximize the Topmost Element After K Moves

**LeetCode Problem #2202 — Maximize the Topmost Element After K Moves**
Solve LeetCode Maximize the Topmost Element After K Moves using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Topmost Element After K Moves |
| LeetCode | #2202 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` representing the contents of a pile , where `nums[0]` is the topmost element of the pile.

In one move, you can perform **either** of the following:

If the pile is not empty, **remove** the topmost element of the pile. 
 If there are one or more removed elements, **add** any one of them back onto the pile. This element becomes the new topmost element.

You are also given an integer `k`, which denotes the total number of moves to be made.

Return *the **maximum value** of the topmost element of the pile possible after **exactly*** `k` *moves*. In case it is not possible to obtain a non-empty pile after `k` moves, return `-1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i], k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,2,2,4,0,6], k = 4`
- **Output:** `5`
- **Explanation:** One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.

### Example 2
- **Input:** `nums = [2], k = 1`
- **Output:** `-1`
- **Explanation:** In the first move, our only option is to pop the topmost element of the pile.
Since it is not possible to obtain a non-empty pile after one move, we return -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Topmost Element After K Moves**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,2,2,4,0,6], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.

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
from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]
        best = -1
        if k >= 2:
            best = max(nums[:min(k - 1, n)])
        if k < n:
            best = max(best, nums[k])
        return best
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
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)
- [3767. Maximize Points After Choosing K Tasks](../../3501-4000/3767-maximize-points-after-choosing-k-tasks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/)
