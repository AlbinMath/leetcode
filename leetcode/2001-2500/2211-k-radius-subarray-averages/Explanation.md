# LeetCode 2090: K Radius Subarray Averages

**LeetCode Problem #2090 — K Radius Subarray Averages**
Solve LeetCode K Radius Subarray Averages using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K Radius Subarray Averages |
| LeetCode | #2090 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` of `n` integers, and an integer `k`.

The **k-radius average** for a subarray of `nums` **centered** at some index `i` with the **radius** `k` is the average of **all** elements in `nums` between the indices `i - k` and `i + k` (**inclusive**). If there are less than `k` elements before **or** after the index `i`, then the **k-radius average** is `-1`.

Build and return *an array *`avgs`* of length *`n`* where *`avgs[i]`* is the **k-radius average** for the subarray centered at index *`i`.

The **average** of `x` elements is the sum of the `x` elements divided by `x`, using **integer division**. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements `2`, `3`, `1`, and `5` is `(2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75`, which truncates to `2`.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `0 <= nums[i], k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [7,4,3,9,1,8,5,2,6], k = 3`
- **Output:** `[-1,-1,-1,5,4,4,-1,-1,-1]`
- **Explanation:** - avg[0], avg[1], and avg[2] are -1 because there are less than k elements

### Example 2
- **Input:** `nums = [100000], k = 0`
- **Output:** `[100000]`
- **Explanation:** - The sum of the subarray centered at index 0 with radius 0 is: 100000.
 avg[0] = 100000 / 1 = 100000.

### Example 3
- **Input:** `nums = [8], k = 100000`
- **Output:** `[-1]`
- **Explanation:** - avg[0] is -1 because there are less than k elements before and after index 0.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **K Radius Subarray Averages**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [7,4,3,9,1,8,5,2,6], k = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-1,-1,-1,5,4,4,-1,-1,-1]`.
4. **Verification:** - avg[0], avg[1], and avg[2] are -1 because there are less than k elements

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
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        diameter = 2 * k + 1
        
        if diameter > n:
            return avgs
            
        window_sum = sum(nums[:diameter])
        avgs[k] = window_sum // diameter
        
        for right in range(diameter, n):
            window_sum += nums[right] - nums[right - diameter]
            avgs[right - k] = window_sum // diameter
            
        return avgs
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
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)
- [713. Subarray Product Less Than K](../../0501-1000/0713-subarray-product-less-than-k/)
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0892-shortest-subarray-with-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-radius-subarray-averages/)
