# LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

**LeetCode Problem #1343 — Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold**
Solve LeetCode Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold |
| LeetCode | #1343 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr` and two integers `k` and `threshold`, return *the number of sub-arrays of size *`k`* and average greater than or equal to *`threshold`.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^4`
- `1 <= k <= arr.length`
- `0 <= threshold <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4`
- **Output:** `3`
- **Explanation:** Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

### Example 2
- **Input:** `arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5`
- **Output:** `6`
- **Explanation:** The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

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
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0
        
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1
                
        return count
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
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](../../3001-3500/3328-apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1631-number-of-sub-arrays-with-odd-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
