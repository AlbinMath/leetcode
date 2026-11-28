# LeetCode 4058: Maximum Pulse Value After One Subarray Rotation

**LeetCode Problem #4058 — Maximum Pulse Value After One Subarray Rotation**
Solve LeetCode Maximum Pulse Value After One Subarray Rotation using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Pulse Value After One Subarray Rotation |
| LeetCode | #4058 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Define the **pulse value** of an integer array `arr` as the **alternating sum** starting at index 0: `pulse(arr) = arr[0] - arr[1] + arr[2] - arr[3] + ...`.

You may perform **at most** one operation on `nums`:

Choose two indices `l` and `r` such that `0 <= l < r < n`. 
 **Left-rotate** the subarray `nums[l..r]` by **exactly** one position. For example, `[a, b, c, d]` becomes `[b, c, d, a]`.

Return the **maximum pulse value** that can be obtained after performing **at most** one such operation.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,5,2]`
- **Output:** `6`
- **Explanation:** The original pulse value is `1 - 5 + 2 = -2`. 
 Rotate the subarray `nums[0..1]` from `[1, 5]` to `[5, 1]`. 
 The resulting array is `[5, 1, 2]` and its pulse value is `5 - 1 + 2 = 6`, which is the maximum possible.

### Example 2
- **Input:** `nums = [6,4,3]`
- **Output:** `7`
- **Explanation:** The original pulse value is `6 - 4 + 3 = 5`. 
 Rotate the subarray `nums[1..2]` from `[4, 3]` to `[3, 4]`. 
 The resulting array is `[6, 3, 4]` and its pulse value is `6 - 3 + 4 = 7`, which is the maximum possible.

### Example 3
- **Input:** `nums = [9,7]`
- **Output:** `2`
- **Explanation:** The original pulse value is `9 - 7 = 2`, which is already maximum. Thus, no rotation is required.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Pulse Value After One Subarray Rotation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The original pulse value is `1 - 5 + 2 = -2`. 
 Rotate the subarray `nums[0..1]` from `[1, 5]` to `[5, 1]`. 
 The resulting array is `[5, 1, 2]` and its pulse value is `5 - 1 + 2 = 6`, which is the maximum possible.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + (v if i % 2 == 0 else -v)
        base = P[n]

        best_gain = 0
        NEG = float('-inf')
        mx = [NEG, NEG]  # max P[l] per index parity, over l <= e - 2
        for e in range(2, n + 1):
            l = e - 2
            mx[l % 2] = max(mx[l % 2], P[l])
            if mx[e % 2] > NEG:
                best_gain = max(best_gain, 2 * (mx[e % 2] - P[e]))

        return base + best_gain
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [1881. Maximum Value after Insertion](../../1501-2000/1881-maximum-value-after-insertion/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-pulse-value-after-one-subarray-rotation/)
