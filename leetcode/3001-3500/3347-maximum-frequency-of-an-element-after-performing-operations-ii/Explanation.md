# LeetCode 3347: Maximum Frequency of an Element After Performing Operations II

**LeetCode Problem #3347 — Maximum Frequency of an Element After Performing Operations II**
Solve LeetCode Maximum Frequency of an Element After Performing Operations II using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Frequency of an Element After Performing Operations II |
| LeetCode | #3347 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an **operation** `numOperations` times on `nums`, where in each operation you:

Select an index `i` that was **not** selected in any previous operations. 
 Add an integer in the range `[-k, k]` to `nums[i]`.

Return the **maximum** possible frequency of any element in `nums` after performing the **operations**.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`
- `0 <= numOperations <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,4,5], k = 1, numOperations = 2`
- **Output:** `2`
- **Explanation:** We can achieve a maximum frequency of two by: 

 
 Adding 0 to `nums[1]`, after which `nums` becomes `[1, 4, 5]`. 
 Adding -1 to `nums[2]`, after which `nums` becomes `[1, 4, 4]`.

### Example 2
- **Input:** `nums = [5,11,20,20], k = 5, numOperations = 1`
- **Output:** `2`
- **Explanation:** We can achieve a maximum frequency of two by: 

 
 Adding 0 to `nums[1]`.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Maximum Frequency of an Element After Performing Operations II**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,5], k = 1, numOperations = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can achieve a maximum frequency of two by: 

 
 Adding 0 to `nums[1]`, after which `nums` becomes `[1, 4, 5]`. 
 Adding -1 to `nums[2]`, after which `nums` becomes `[1, 4, 4]`.

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
from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = Counter(nums)
        ans = 0

        # Case 1: target is an existing value
        for v, c in cnt.items():
            inr = bisect_right(nums, v + k) - bisect_left(nums, v - k)
            ans = max(ans, c + min(numOperations, inr - c))

        # Case 2: target is any value; need a window of width 2k
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            ans = max(ans, min(numOperations, r - l + 1))

        return ans
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
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3001-3500/3346-maximum-frequency-of-an-element-after-performing-operations-i/)
- [3434. Maximum Frequency After Subarray Operation](../../3001-3500/3434-maximum-frequency-after-subarray-operation/)
- [2011. Final Value of Variable After Performing Operations](../../2001-2500/2011-final-value-of-variable-after-performing-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/)
