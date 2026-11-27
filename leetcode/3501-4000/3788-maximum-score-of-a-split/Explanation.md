# LeetCode 3788: Maximum Score of a Split

**LeetCode Problem #3788 — Maximum Score of a Split**
Solve LeetCode Maximum Score of a Split using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score of a Split |
| LeetCode | #3788 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Choose an index `i` such that `0 <= i < n - 1`.

For a chosen split index `i`:

Let `prefixSum(i)` be the sum of `nums[0] + nums[1] + ... + nums[i]`. 
 Let `suffixMin(i)` be the minimum value among `nums[i + 1], nums[i + 2], ..., nums[n - 1]`.

The **score** of a split at index `i` is defined as:

`score(i) = prefixSum(i) - suffixMin(i)`

Return an integer denoting the **maximum** score over all valid split indices.

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^9​​​​​​​ <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [10,-1,3,-4,-5]`
- **Output:** `17`
- **Explanation:** The optimal split is at `i = 2`, `score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17`.

### Example 2
- **Input:** `nums = [-7,-5,3]`
- **Output:** `-2`
- **Explanation:** The optimal split is at `i = 0`, `score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2`.

### Example 3
- **Input:** `nums = [1,1]`
- **Output:** `0`
- **Explanation:** The only valid split is at `i = 0`, `score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Score of a Split**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,-1,3,-4,-5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** The optimal split is at `i = 2`, `score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17`.

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
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])

        pre = 0
        best = float('-inf')
        for i in range(n - 1):
            pre += nums[i]
            best = max(best, pre - suf[i + 1])
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
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1255-maximum-score-words-formed-by-letters/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-of-a-split/)
